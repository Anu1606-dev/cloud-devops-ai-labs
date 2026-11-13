import csv
from pathlib import Path

BUDGET = 25.00
WARNING_THRESHOLD = 80.0

with Path("sample-costs.csv").open() as file:
    rows = list(csv.DictReader(file))

total = sum(
    float(row["monthly_estimate_usd"])
    for row in rows
)

usage = (total / BUDGET) * 100

print("=== Monthly Cost Simulation ===")

for row in rows:
    print(
        f"{row['service']}: "
        f"${float(row['monthly_estimate_usd']):.2f}"
    )

print(f"\nBudget: ${BUDGET:.2f}")
print(f"Estimated spending: ${total:.2f}")
print(f"Budget utilisation: {usage:.1f}%")

if usage >= 100:
    print("ALERT: Budget exceeded!")
elif usage >= WARNING_THRESHOLD:
    print("WARNING: Spending reached the 80% threshold.")
else:
    print("OK: Spending is within the warning threshold.")
