import csv

COST_FILE = "cost_engine/sample_cost_data.csv"

def collect_cost_data():
    costs = []

    with open(COST_FILE, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            costs.append({
                "date": row["date"],
                "service": row["service"],
                "cost": float(row["cost_usd"])
            })

    return costs
