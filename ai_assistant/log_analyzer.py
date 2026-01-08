import re

LOG_FILE = "logs/app.log"

ERROR_PATTERNS = {
    "crash": "Application crash detected",
    "timeout": "Request timeout issue",
    "exception": "Unhandled exception occurred"
}

def analyze_logs():
    findings = []

    try:
        with open(LOG_FILE, "r") as f:
            lines = f.readlines()

        for line in lines[-50:]:
            for key, message in ERROR_PATTERNS.items():
                if re.search(key, line.lower()):
                    findings.append({
                        "issue": key,
                        "explanation": message,
                        "log": line.strip()
                    })

    except FileNotFoundError:
        return {"status": "no logs found"}

    if not findings:
        return {"status": "healthy", "message": "No critical issues detected"}

    return {
        "status": "issues_detected",
        "summary": f"{len(findings)} issue(s) found",
        "details": findings
    }

if __name__ == "__main__":
    print(analyze_logs())
