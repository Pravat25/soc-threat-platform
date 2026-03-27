from collections import defaultdict

def analyze_logs(logs):
    stats = {
        "warning": 0,
        "critical": 0
    }

    ip_count = defaultdict(int)
    processed_logs = []

    for log in logs:
        log = log.strip()

        # Extract source IP (basic split)
        try:
            parts = log.split()
            src_ip = parts[2].split(":")[0]
        except:
            src_ip = "unknown"

        ip_count[src_ip] += 1

        # WARNING: suspicious ports
        if ":22" in log or ":3389" in log or ":23" in log:
            stats["warning"] += 1
            log = "WARNING: Suspicious port activity | " + log

        # CRITICAL: too many requests from same IP
        elif ip_count[src_ip] > 3:
            stats["critical"] += 1
            log = "CRITICAL: Possible brute-force or scan | " + log

        processed_logs.append(log)

    return processed_logs, stats
