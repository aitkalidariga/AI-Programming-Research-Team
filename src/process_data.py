"""Task 3: validated, reproducible analysis of programming-study run logs.
All bundled raw records are SYNTHETIC and not research evidence.
"""
import argparse
import json
from pathlib import Path
import numpy as np
import pandas as pd

GROUPS = ('no_ai', 'ai_hints', 'ai_solutions')
METRICS = ('practice_score_pct', 'independent_score_pct', 'completion_time_min', 'concept_score_pct', 'programming_errors')
REQUIRED = {'run_id','group','phase','task_load','practice_score_pct','independent_score_pct',
            'completion_time_min','concept_score_pct','programming_errors','execution_success','data_type'}


def load_jsonl(path):
    records=[]
    with Path(path).open(encoding='utf-8') as handle:
        for line_number, line in enumerate(handle,1):
            if line.strip():
                try: records.append(json.loads(line))
                except json.JSONDecodeError as exc: raise ValueError(f'Invalid JSON at line {line_number}') from exc
    if not records: raise ValueError('No records found')
    df=pd.DataFrame.from_records(records)
    missing=REQUIRED-set(df.columns)
    if missing: raise ValueError(f'Missing fields: {sorted(missing)}')
    if df['run_id'].duplicated().any(): raise ValueError('Duplicate run_id values')
    return df


def validate_and_filter(df):
    """Exclude warm-up, invalid rows, and failed executions from performance estimates.
    Failure prevalence is still computed over ALL evaluation rows.
    """
    if not df.group.isin(GROUPS).all(): raise ValueError('Unexpected group')
    if not df.phase.isin(['warmup','evaluation']).all(): raise ValueError('Invalid phase')
    if not df.task_load.isin([1,2,3]).all(): raise ValueError('Task load must be 1, 2 or 3')
    if not df.data_type.eq('synthetic').all(): raise ValueError('Demo pipeline accepts synthetic records only')
    eval_df=df.loc[df.phase.eq('evaluation')].copy()
    if eval_df.empty: raise ValueError('No evaluation records after warm-up filtering')
    valid=pd.Series(True,index=eval_df.index)
    for name in METRICS:
        eval_df[name]=pd.to_numeric(eval_df[name],errors='coerce')
        valid &= eval_df[name].notna()
    for name in ('practice_score_pct','independent_score_pct','concept_score_pct'):
        valid &= eval_df[name].between(0,100)
    valid &= eval_df['completion_time_min'].gt(0) & eval_df['programming_errors'].ge(0)
    valid &= eval_df['execution_success'].isin([True,False])
    eval_df['valid']=valid
    successful=eval_df.loc[valid & eval_df.execution_success.eq(True)].copy()
    return eval_df,successful


def bootstrap_ci(values, seed=42, repetitions=3000, func=np.mean):
    """Percentile bootstrap CI (95%), with a fixed seed for reproducibility."""
    a=np.asarray(values,dtype=float)
    if len(a)==0: return float('nan'),float('nan')
    if len(a)==1: return float(a[0]),float(a[0])
    rng=np.random.default_rng(seed)
    draws=rng.choice(a,size=(repetitions,len(a)),replace=True)
    estimates=np.asarray([func(sample) for sample in draws])
    return tuple(np.quantile(estimates,[0.025,0.975]).tolist())


def aggregate(all_eval,success):
    rows=[]
    for gi,group in enumerate(GROUPS):
        g_all=all_eval.loc[all_eval.group.eq(group)]
        g=success.loc[success.group.eq(group)]
        if g.empty: raise ValueError(f'No valid successful runs in {group}')
        entry={
            'group':group,
            'n_evaluation_runs':len(g_all),
            'n_analyzed':len(g),
            'valid_results_rate_pct':100*g_all.valid.mean(),
            'execution_error_rate_pct':100*(~g_all.execution_success.astype(bool)).mean(),
        }
        for mi,m in enumerate(METRICS):
            vals=g[m].to_numpy(dtype=float)
            low,high=bootstrap_ci(vals,seed=42+gi*100+mi)
            entry.update({f'{m}_mean':vals.mean(),f'{m}_sd':vals.std(ddof=1) if len(vals)>1 else 0.,
                          f'{m}_median':np.median(vals),f'{m}_p25':np.percentile(vals,25),
                          f'{m}_p75':np.percentile(vals,75),f'{m}_p95':np.percentile(vals,95),
                          f'{m}_p99':np.percentile(vals,99),f'{m}_ci_low':low,f'{m}_ci_high':high})
        rows.append(entry)
    return pd.DataFrame(rows)


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--input',default='data/raw/test_run.jsonl')
    parser.add_argument('--output',default='data/processed/metrics_summary.csv')
    args=parser.parse_args()
    df=load_jsonl(args.input)
    ev,success=validate_and_filter(df)
    summary=aggregate(ev,success)
    p=Path(args.output);p.parent.mkdir(parents=True,exist_ok=True)
    summary.to_csv(p,index=False,float_format='%.5f')
    print('SYNTHETIC DEMONSTRATION — not real student observations')
    print(f'Warm-up removed: {sum(df.phase.eq("warmup"))}; evaluation: {len(ev)}; analyzed: {len(success)}')
    print(summary[['group','n_analyzed','independent_score_pct_mean','completion_time_min_mean','execution_error_rate_pct']].to_string(index=False))

if __name__=='__main__': main()
