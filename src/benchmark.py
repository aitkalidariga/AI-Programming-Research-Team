
import csv
import json
from pathlib import Path
from collections import defaultdict
from statistics import mean

ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = ROOT / "configs" / "config.json"

with CONFIG_PATH.open("r", encoding="utf-8") as file:
    config = json.load(file)

data_path = ROOT / config["data_path"]
results = defaultdict(list)

with data_path.open("r", encoding="utf-8-sig", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        results[row["group"]].append(row)

print("AI Programming Research Benchmark")
print("Data type: synthetic")
print("-" * 40)

for group, rows in sorted(results.items()):
    print(f"\nGroup: {group}")
    print(f"Number of students: {len(rows)}")

    
    task_scores = [
        int(row["passed_tests"]) / int(row["total_tests"]) * 100
        for row in rows
    ]
    completion_times = [
        float(row["completion_time_min"]) for row in rows
    ]
    concept_scores = [
        float(row["concept_score"]) for row in rows
    ]
    programming_errors = [
        int(row["programming_errors"]) for row in rows
    ]

    print(f"Average task score: {mean(task_scores):.2f}%")
    print(f"Average completion time: {mean(completion_times):.2f} minutes")
    print(f"Average concept score: {mean(concept_scores):.2f}%")
    print(f"Average programming errors: {mean(programming_errors):.2f}")


print("\nBenchmark completed successfully.")
print("Note: Synthetic data, not real research results.")
