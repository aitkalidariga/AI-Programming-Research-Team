
# The Impact of Generative AI Assistance on Programming Learning Effectiveness Among Undergraduate Students

**Authors:** Yerkindik Ailen and Aitkali Dariga  
**Research Type:** Quantitative Experimental Study  
**Repository:** https://github.com/aitkalidariga/AI-Programming-Research-Team

## 1. Project Overview

This research investigates how generative AI assistance influences programming learning effectiveness among undergraduate students.

The study compares three learning conditions:

- **Group A (No AI):** Students complete programming tasks without AI assistance.
- **Group B (AI Hints):** Students receive AI-generated hints and explanations.
- **Group C (AI Solutions):** Students receive direct AI-generated solutions.

The study evaluates programming performance, task completion time, conceptual understanding, and independent problem-solving skills.

## 2. Research Questions

**RQ1:** How does access to generative AI during programming exercises affect students' task performance and completion time compared with learning without AI?

**RQ2:** How does the use of generative AI during programming practice affect students' understanding and retention when AI assistance is later removed?

**RQ3:** Which type of AI support, explanations and hints or direct solution generation, leads to better independent programming performance?

## 3. Research Methodology

**Research Approach:** Quantitative Research

**Research Design:** Planned comparative experiment with three student groups.

### Independent Variables

- Access to generative AI assistance
- Type of AI assistance: no AI, hints and explanations, or direct solutions

### Dependent Variables

- Programming task score (%)
- Task completion time (minutes)
- Concept test score (%)
- Number of programming errors
- Independent programming performance after AI assistance is removed

### Controlled Variables

- Programming language
- Task difficulty
- Time limits
- Learning materials
- Evaluation criteria

Prior programming experience will also be measured and considered during analysis.

## 4. Research Hypotheses

### RQ1: AI Assistance and Programming Performance

**H0₁:** There is no statistically significant difference in programming task performance and completion time between students using AI assistance and students working without AI.

**H1₁:** Access to generative AI assistance improves programming task performance and reduces completion time compared with working without AI.

### RQ2: AI Assistance and Independent Learning

**H0₂:** Generative AI assistance during practice does not significantly affect students' later independent programming performance.

**H1₂:** Generative AI assistance during practice significantly affects students' later independent programming performance.

### RQ3: Hints Versus Direct Solutions

**H0₃:** There is no statistically significant difference in independent programming performance between students receiving AI-generated hints and students receiving direct AI-generated solutions.

**H1₃:** Students receiving AI-generated hints and explanations achieve higher independent programming performance than students receiving direct AI-generated solutions.

## 5. Evaluation Metrics and Baseline

| Metric | Description | Unit |
|---|---|---|
| Independent Task Score | Percentage of passed test cases without AI | % |
| Completion Time | Time needed to complete a programming task | Minutes |
| Concept Test Score | Percentage of correct answers | % |
| Programming Errors | Number of recorded programming errors | Count |
| Valid Results Rate | Percentage of correctly processed records | % |

**Primary Metric:** Independent Programming Task Score (%).

**Secondary Metrics:** Completion time, concept test score, and programming errors.

**Guardrail Metric:** Valid Results Rate (%).

**Baseline:** Students completing programming exercises without AI assistance.

## 6. Repository Structure

```text
AI-Programming-Research-Team/
├── .github/
│   └── workflows/
│       └── main.yml
├── configs/
│   ├── config.json
│   └── config.yaml
├── data/
│   └── sample/
│       └── sample_results.csv
├── docs/
│   └── Methodology_Passport_Card.pdf
├── src/
│   └── benchmark.py
├── .gitignore
├── Dockerfile
├── LICENSE
├── README.md
└── requirements.txt
```

## 7. System Requirements

- Python 3.11
- Docker Desktop (recommended)
- Windows, Linux, or macOS
- Internet connection for the initial installation

## 8. Quickstart Guide

### Option 1: Run with Docker

Open a terminal in the repository folder.

**Step 1: Build the Docker image**

```bash
docker build -t ai-programming-research .
```

**Step 2: Run the benchmark**

```bash
docker run --rm ai-programming-research
```

The benchmark reads the sample dataset and calculates average performance metrics for each group.

### Option 2: Run with Python

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the benchmark:

```bash
python src/benchmark.py
```

## 9. Planned Benchmark Matrix

| Factor | Values | Measurements |
|---|---|---|
| AI Assistance | No AI, AI Hints, AI Solutions | Programming performance |
| Task Performance | Passed test cases / Total test cases | Task score (%) |
| Completion Time | Time spent on programming tasks | Minutes |
| Concept Understanding | Concept test results | Concept score (%) |
| Programming Errors | Number of errors | Error count |

The benchmark compares the three groups using the same evaluation metrics.

## 10. Sample Benchmark Results

The repository contains nine synthetic student records: three records for each experimental group.

The following results were obtained from the illustrative sample dataset.

| Group | Average Task Score | Average Completion Time | Average Concept Score |
|---|---|---|---|
| No AI | 70.00% | 35.67 min | 70.00% |
| AI Hints | 86.67% | 25.67 min | 86.67% |
| AI Solutions | 76.67% | 20.33 min | 66.67% |

**Important:** These results are based on synthetic data created to test the benchmark pipeline. They are not real research findings and cannot be used to confirm the hypotheses.

## 11. Reproducibility

The project includes a Docker environment to support reproducible benchmark execution.

The benchmark uses:

- A predefined sample dataset
- Consistent evaluation metrics
- A specified Python environment
- Configuration files
- An automated GitHub Actions workflow

The same sample data and benchmark settings should produce consistent results.

### GitHub Actions

The repository includes an automated workflow named **Docker Benchmark Check**.

The workflow builds the Docker image and runs the benchmark after repository updates.

Successful workflow execution confirms that the sample benchmark pipeline can run in the configured environment. It does not validate the research hypotheses.

## 12. Smoke Test vs. Research Results

The nine-row sample dataset is used only for technical testing.

The purpose of the smoke test is to verify that:

- The benchmark script executes successfully.
- The CSV file is read correctly.
- Performance metrics are calculated.
- Docker runs the benchmark.
- GitHub Actions completes the automated check.

A larger dataset with real participants will be required for the actual research.

## 13. Methodology Passport Card

The Methodology Passport Card documents:

- Project information and research type
- Research questions and hypotheses
- Independent, dependent, and controlled variables
- Primary, secondary, and guardrail metrics
- Baseline condition
- Planned evaluation procedure

The document is intended to be stored in:

`docs/Methodology_Passport_Card.pdf`

## 14. Citation and License

Yerkindik, A., & Aitkali, D. (2026). *The Impact of Generative AI Assistance on Programming Learning Effectiveness Among Undergraduate Students*. Research Methods Course Project.

**License:** MIT License. See the LICENSE file.

## 15. Project Status

**Task 2: Methodology and Reproducible Benchmark Pipeline**

The initial benchmark pipeline has been tested using synthetic data.

Future research stages will involve collecting real experimental data, comparing student groups, and evaluating the proposed hypotheses.
