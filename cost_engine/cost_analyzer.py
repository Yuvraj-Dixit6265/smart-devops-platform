from statistics import mean

def analyze_costs(cost_data):
    daily_costs = [c["cost"] for c in cost_data]

    if len(daily_costs) < 3:
        return {
            "status": "insufficient_data",
            "message": "Not enough data to analyze costs"
        }

    avg_cost = mean(daily_costs[:-1])
    latest_cost = daily_costs[-1]

    return {
        "average_cost": round(avg_cost, 2),
        "latest_cost": latest_cost,
        "increase_percent": round(
            ((latest_cost - avg_cost) / avg_cost) * 100, 2
        )
    }
