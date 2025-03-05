import pandas as pd

def obter_erros_por_servico(all_data):


    df = pd.DataFrame(all_data)


    df_erros = df[df["level_type"] == "ERROR"].copy()

    if df_erros.empty:
        return {
            "contagem_por_servico": pd.DataFrame(),
            "erros_agrupados": pd.DataFrame(),
            "erros_detalhados": pd.DataFrame()
        }

    df_contagem = df_erros.groupby("service").size().reset_index(name="total_erros")

    df_agrupado = df_erros.groupby(["service", "context", "error_description"]).size().reset_index(name="quantidade")


    df_detalhado = df_erros[["created_at", "service", "context", "error_description"]]
    df_detalhado = df_detalhado.sort_values(by="created_at", ascending=False)

    return {
        "contagem_por_servico": df_contagem,
        "erros_agrupados": df_agrupado,
        "erros_detalhados": df_detalhado
    }
