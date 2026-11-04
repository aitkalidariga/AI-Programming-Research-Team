# Task 3 — Data Analysis and Reproducibility Protocol

**Project:** The Impact of Generative AI Assistance on Programming Learning Effectiveness Among Undergraduate Students

**Authors:** Yerkindik Ailen and Aitkali Dariga

**Research Type:** Quantitative Research

**Data Status:** Synthetic demonstration only.

## 1. Research Design

The project compares three programming practice groups:

- Group A: No AI assistance (baseline)
- Group B: AI-generated hints and explanations
- Group C: Direct AI-generated solutions

The main research outcome is the Independent Programming Task Score (%).

In the planned study, all students complete an independent programming task without AI assistance after practice.

## 2. Data Sources

Task 2 dataset:

`data/sample/sample_results.csv`

This file contains nine synthetic demonstration records.

Task 3 dataset:

`data/raw/test_run.jsonl`

This file contains synthetic benchmark records with warm-up and evaluation phases.

The two datasets are separate demonstration datasets and are not treated as results from one real experiment.

## 3. Data Processing

Data processing is implemented in:

`src/process_data.py`

The pipeline performs the following steps:

1. Load JSONL records.
2. Check required fields and unique run identifiers.
3. Validate experimental groups.
4. Exclude warm-up records.
5. Validate numerical measurements.
6. Calculate execution error rates.
7. Calculate descriptive statistics.
8. Estimate bootstrap confidence intervals.
9. Export processed results to CSV.

## 4. Statistical Metrics

### Mean

The arithmetic average of observations.

### Standard Deviation

The sample standard deviation measures variation between observations.

### Median

The middle value of an ordered dataset.

### Percentiles

The 25th and 75th percentiles describe the central distribution.

The 95th and 99th percentiles describe upper-tail values.

### Bootstrap Confidence Intervals

The pipeline estimates 95% confidence intervals using:

- 3,000 bootstrap resamples
- Fixed random seeds
- The 2.5th and 97.5th percentiles of bootstrap means

## 5. Guardrail Metrics

### Execution Error Rate

Execution Error Rate (%) =
Failed Evaluation Runs / Total Evaluation Runs × 100

### Valid Results Rate

Valid Results Rate (%) =
Valid Evaluation Records / Total Evaluation Records × 100

## 6. Scientific Visualization

### Figure 1

Completion Time vs Task Load

- X-axis: Programming Task Load
- Y-axis: Completion Time (minutes)
- Error bars: Bootstrap 95% CI

### Figure 2

Independent Programming Task Score Distribution

- X-axis: Experimental Group
- Y-axis: Independent Task Score (%)
- Boxplots and 95% CI

Both figures are exported as PDF and PNG files.

## 7. Reproducibility

The project uses fixed random seeds for bootstrap calculations.

Automated checks cover:

- JSONL validation
- Warm-up filtering
- Experimental groups
- Statistical aggregation
- Bootstrap reproducibility
- Scientific figure exports

## 8. Research Limitations

All current Task 3 records are synthetic.

The results demonstrate that the research analysis pipeline works. They are not actual student observations and cannot confirm the research hypotheses.

Future research requires real participants, appropriate consent, standardized programming tasks, independent assessments, and statistical hypothesis testing.
