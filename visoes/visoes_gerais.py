from visoes.consultar_todos_logs import consultar_todos_logs

def consultar_logs_por_level(all_data):
    total_logs = len(all_data)
    total_success = sum(1 for log in all_data if log["level_type"] == "SUCCESS")
    total_errors = sum(1 for log in all_data if log["level_type"] == "ERROR")

    
    latencies = [log["latency_ms"] for log in all_data if log["latency_ms"] is not None]
    avg_latency = round(sum(latencies) / len(latencies), 2) if latencies else 0

    return {
        "total_logs": total_logs,
        "total_success": total_success,
        "total_errors": total_errors,
        "avg_latency": avg_latency
    }
