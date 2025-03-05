import pandas as pd

def obter_eventos_por_tempo(all_data, granularidade="hora"):
    df = pd.DataFrame(all_data)
    df["created_at"] = pd.to_datetime(df["created_at"]) 

    granularidade_map = {
        "ano": df["created_at"].dt.year,
        "mês": df["created_at"].dt.to_period("M").astype(str),
        "dia": df["created_at"].dt.to_period("D").astype(str),
        "hora": df["created_at"].dt.to_period("h").astype(str),
        "minuto": df["created_at"].dt.to_period("min").astype(str), 
    }


    df["tempo"] = granularidade_map.get(granularidade, df["created_at"].dt.to_period("h").astype(str))


    df_grouped = df.groupby("tempo").size().reset_index(name="total_eventos")

    return df_grouped
