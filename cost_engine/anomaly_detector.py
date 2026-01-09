from cost_engine.cost_collector import collect_cost_data
from cost_engine.cost_analyzer import analyze_costs

ANOMALY_THRESHOLD = 30  # percent

def detect_cost_anomaly():
    cost_data = collect_cost_data()
    analysis = analyze_costs(cost_data)

    if "increase_percent" not in analysis:
        return analysis

    if analysis["increase_percent"] > ANOMALY_THRESHOLD:
        return {
            "status": "anomaly_detected",
            "reason": f"Cloud cost increased by {analysis['increase_percent']}%",
            "possible_cause": "New deployment scaled pods or increased resource requests",
            "recommendation": "Review autoscaling rules, unused pods, and recent deployments"
        }

    return {
        "status": "normal",
        "message": "Cloud costs are within normal range"
    }


if __name__ == "__main__":
    print(detect_cost_anomaly())
