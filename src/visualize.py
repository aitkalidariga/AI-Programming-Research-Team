"""Scientific figures for Task 3. Bundled data are synthetic only."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from src.process_data import GROUPS, bootstrap_ci

COLORS={'no_ai':'#0072B2','ai_hints':'#009E73','ai_solutions':'#D55E00'}
LABELS={'no_ai':'No AI (baseline)','ai_hints':'AI hints','ai_solutions':'AI solutions'}
MARKERS={'no_ai':'o','ai_hints':'s','ai_solutions':'^'}
STYLES={'no_ai':'-','ai_hints':'--','ai_solutions':':' }


def generate_figures(success,output_dir='reports/figures'):
    out=Path(output_dir);out.mkdir(parents=True,exist_ok=True)
    plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False,'savefig.bbox':'tight'})
    # The required filename retains the assignment template's "latency_vs_load" convention;
    # domain-appropriate units are programming-task completion time in minutes.
    fig,ax=plt.subplots(figsize=(8.4,5.2))
    for gi,group in enumerate(GROUPS):
        part=success.loc[success.group.eq(group)]
        x=[]; y=[]; lo=[]; hi=[]
        for load in (1,2,3):
            vals=part.loc[part.task_load.eq(load),'completion_time_min'].to_numpy()
            if not len(vals):continue
            mean=vals.mean();a,b=bootstrap_ci(vals,seed=42+gi*100+load)
            x.append(load);y.append(mean);lo.append(mean-a);hi.append(b-mean)
        ax.errorbar(x,y,yerr=np.array([lo,hi]),color=COLORS[group],label=LABELS[group],
                    marker=MARKERS[group],linestyle=STYLES[group],capsize=4,linewidth=1.8)
    ax.set_xticks([1,2,3],['Low','Medium','High'])
    ax.set_xlabel('Programming task load (difficulty category)')
    ax.set_ylabel('Mean completion time (minutes)')
    ax.set_title('Completion time by task difficulty — synthetic demonstration')
    ax.grid(axis='y',alpha=0.22);ax.legend(loc='upper left')
    fig.savefig(out/'fig1_latency_vs_load.pdf');fig.savefig(out/'fig1_latency_vs_load.png',dpi=320)
    plt.close(fig)

    fig,ax=plt.subplots(figsize=(8.4,5.2))
    data=[success.loc[success.group.eq(g),'independent_score_pct'].to_numpy() for g in GROUPS]
    bp=ax.boxplot(data,positions=[1,2,3],widths=.48,patch_artist=True,showfliers=True)
    for patch,g in zip(bp['boxes'],GROUPS):patch.set_facecolor(COLORS[g]);patch.set_alpha(.25)
    for med in bp['medians']: med.set_color('#222222');med.set_linewidth(2)
    for i,(g,v) in enumerate(zip(GROUPS,data),1):
        ci=bootstrap_ci(v,seed=500+i)
        ax.errorbar([i],[v.mean()],yerr=[[v.mean()-ci[0]],[ci[1]-v.mean()]],
                    fmt=MARKERS[g],color=COLORS[g],capsize=6,markersize=7,label=f'{LABELS[g]} mean ± 95% CI')
    ax.set_xticks([1,2,3],[LABELS[g] for g in GROUPS])
    ax.set_ylabel('Independent programming task score (%)')
    ax.set_xlabel('Assigned practice condition')
    ax.set_ylim(0,105)
    ax.set_title('Independent performance after AI removal — synthetic demonstration')
    ax.grid(axis='y',alpha=.22);ax.legend(fontsize=8,loc='lower right')
    fig.savefig(out/'fig2_distribution_boxplot.pdf');fig.savefig(out/'fig2_distribution_boxplot.png',dpi=320)
    plt.close(fig)
    return [out/'fig1_latency_vs_load.pdf',out/'fig2_distribution_boxplot.pdf']
