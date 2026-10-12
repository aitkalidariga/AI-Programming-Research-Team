# The Impact of Generative AI Assistance on Programming Learning Effectiveness Among Undergraduate Students

**Authors:** Yerkindik Ailen and Aitkali Dariga  
**Research Type:** Quantitative Experimental Study  
**Course Project:** Research Methods, 2026

## 1. Project Overview

This project studies how generative AI affects undergraduate students when they learn programming.

We plan to compare three groups:

- **Group A (No AI):** Students solve programming tasks without AI.
- **Group B (AI Hints):** Students can use AI for hints and explanations.
- **Group C (AI Solutions):** Students can use AI-generated solutions.

We want to find out whether AI helps students complete tasks faster and understand programming better. We also want to check if students can solve similar problems independently after using AI.

## 2. Research Questions

**RQ1:** How does access to generative AI during programming exercises affect students' task performance and completion time compared with learning without AI?

**RQ2:** How does the use of generative AI during programming practice affect students' understanding and retention when AI assistance is later removed?

**RQ3:** Which type of AI support, explanations and hints or direct solution generation, leads to better independent programming performance?

## 3. Research Methodology

**Research Approach:** Quantitative Research

**Research Design:** Planned comparative experiment with three student groups.

### Independent Variables
- Access to generative AI
- Type of AI assistance (No AI, AI Hints, AI Solutions)

### Dependent Variables
- Programming task score (%)
- Task completion time (minutes)
- Concept test score (%)
- Number of programming errors
- Independent programming performance without AI

### Controlled Variables
- Programming language
- Task difficulty
- Time limits
- Learning materials
- Evaluation criteria

We will also consider students' previous programming experience when analyzing the results.

### Planned Experiment

The experiment will have three main stages:

1. **Initial assessment:** Check students' programming knowledge before the experiment.
2. **Programming practice:** Students complete tasks using their assigned AI assistance conditions.
3. **Independent assessment:** Students complete new programming tasks without AI assistance.

The results will be compared to understand how different types of AI support affect learning.

The number of participants and the final statistical analysis method will be determined before collecting real data.

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

## 5. Evaluation Metrics

We use the following metrics to compare the three groups.

| Metric | Description | Unit |
|---|---|---|
| Task Score | Percentage of passed programming test cases | % |
| Completion Time | Time needed to finish a task | Minutes |
| Concept Test Score | Percentage of correct concept test answers | % |
| Programming Errors | Number of errors made during programming | Count |
| Independent Task Score | Task score measured without AI assistance | % |
| Valid Results Rate | Percentage of valid dataset records | % |

**Primary Research Metric:** Independent Programming Task Score (%).

**Secondary Metrics:** Completion time, concept test score, and programming errors.

**Guardrail Metric:** Valid Results Rate (%).

**Baseline:** Students working without AI assistance.

The current sample benchmark calculates task scores, completion times, concept scores, and programming errors.

Independent task performance and the valid results rate are planned for the full experiment and are not yet calculated by the current script.

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
├── src/
│   └── benchmark.py
├── .gitignore
├── Dockerfile
├── LICENSE
├── README.md
└── requirements.txt
```

The repository contains a Python benchmark, sample data, configuration files, and a Docker environment.

The benchmark currently reads its dataset path from `configs/config.json`. The YAML file contains additional planned settings but is not used by the current script.

## 7. System Requirements

- Python 3.11
- Docker Desktop (optional)
- Windows, Linux, or macOS
- Internet connection for installing dependencies

## 8. How to Run the Project

There are two ways to run the benchmark.

### Option 1: Using Docker

Open a terminal in the repository folder.

Build the Docker image:

```bash
docker build -t ai-programming-research .
```

Run the benchmark:

```bash
docker run --rm ai-programming-research
```

### Option 2: Using Python

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the benchmark:

```bash
python src/benchmark.py
```

The program reads the sample CSV file and calculates average results for each group.

## 9. Sample Benchmark Results

We created a small synthetic dataset to test our benchmark.

The dataset contains nine student records, with three records in each group.

| Group | Average Task Score | Average Completion Time | Average Concept Score |
|---|---|---|---|
| No AI | 70.00% | 35.67 min | 70.00% |
| AI Hints | 86.67% | 25.67 min | 86.67% |
| AI Solutions | 76.67% | 20.33 min | 66.67% |

In this sample, the AI Hints group has the highest average task and concept scores. The AI Solutions group has the shortest completion time.

**Important:** These results are based on synthetic data, not real students. They are only used to test the program and cannot confirm our research hypotheses.

## 10. Reproducibility and Testing

We use Docker to make the benchmark easier to run on different computers.

The project includes:

- A sample CSV dataset
- A Python benchmark script
- Configuration files
- A Dockerfile
- A GitHub Actions workflow

Running the benchmark with the same dataset produces the same results.

### GitHub Actions

The repository includes a workflow called **Docker Benchmark Check**.

It is configured to:

1. Download the repository.
2. Build the Docker image.
3. Run the benchmark.

The workflow runs after pushes and pull requests. It can also be started manually.

This helps us check whether the benchmark runs correctly after changes to the repository.

### Smoke Test

The nine synthetic records are used for a basic technical test.

We check whether:

- The CSV file can be read.
- The benchmark runs without errors.
- Average metrics are calculated correctly.
- Docker can execute the benchmark.

These tests check the technical part of the project, not the research hypotheses.

## 11. Current Project Status

**Task 2: Methodology and Reproducible Benchmark Pipeline**

We have prepared the research methodology, hypotheses, evaluation metrics, and initial benchmark.

The Python script can calculate group averages using the synthetic dataset.

Our next steps are to:

1. Prepare the final experimental procedure.
2. Collect data from real undergraduate students.
3. Test independent programming performance without AI.
4. Compare the three groups using statistical analysis.
5. Evaluate the research hypotheses.

The project is still in the preparation and technical testing stage.

## 12. Citation and License

Yerkindik, A., & Aitkali, D. (2026). *The Impact of Generative AI Assistance on Programming Learning Effectiveness Among Undergraduate Students*. Research Methods Course Project.

**License:** MIT License. See the LICENSE file.
