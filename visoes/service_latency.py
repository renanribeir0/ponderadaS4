from visoes.consultar_todos_logs import consultar_todos_logs
import pandas as pd

def obter_eventos_por_servico(all_data):

    df = pd.DataFrame(all_data)
    df_grouped = df.groupby("service").agg(
        total_eventos=("service", "count"),
        media_latency=("latency_ms", "mean")
    ).reset_index()

    df_grouped = df_grouped.sort_values(by="total_eventos", ascending=False)

    return df_grouped
