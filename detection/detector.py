from collections import defaultdict

def analyze_logs(logs):
    stats = {
        "warning": 0,
        "critical": 0,
        "tcp": 0,
        "udp": 0,
        "icmp": 0
    }

    ip_count = defaultdict(int)
    processed_logs = []

    for log in logs:
        log = log.strip()

        # Count protocols
        if "TCP" in log:
            stats["tcp"] += 1
        elif "UDP" in log:
            stats["udp"] += 1
        elif "ICMP" in log:
            stats["icmp"] += 1

        # Extract IP
        try:
            parts = log.split()
            src_ip = parts[2].split(":")[0]
        except:
            src_ip = "unknown"

        ip_count[src_ip] += 1

        # Detection rules
        if ":22" in log or ":3389" in log:
            stats["warning"] += 1
            log = "WARNING: Suspicious port | " + log

        elif ip_count[src_ip] > 3:
            stats["critical"] += 1
            log = "CRITICAL: Possible attack | " + log

        processed_logs.append(log)

    # 🔥 Find top attacker
    top_ip = max(ip_count, key=ip_count.get)
    top_count = ip_count[top_ip]

    return processed_logs, stats, top_ip, top_count
