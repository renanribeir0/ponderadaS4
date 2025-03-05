import streamlit as st
import pandas as pd
from visoes.erros_por_servico import obter_erros_por_servico

def exibir_erros_por_servico(all_data):
    """Exibe a contagem de erros por serviço e as tabelas detalhadas."""


    dados_erros = obter_erros_por_servico(all_data)

    df_contagem = dados_erros["contagem_por_servico"]
    df_agrupado = dados_erros["erros_agrupados"]
    df_detalhado = dados_erros["erros_detalhados"]

    if df_contagem.empty:
        st.warning("Nenhum erro registrado nos logs.")
        return


    st.markdown("### ❌ Visão Geral: Total de Erros por Serviço")
    st.dataframe(df_contagem, height=300, use_container_width=True)

    servico_selecionado = st.selectbox(
        "🔍 Selecione um serviço para visualizar os erros:",
        df_contagem["service"].unique()
    )

    df_agrupado_filtrado = df_agrupado[df_agrupado["service"] == servico_selecionado][["service", "context", "error_description", "quantidade"]]

    st.markdown(f"### 📊 Erros Agrupados no Serviço **{servico_selecionado}**")
    st.dataframe(df_agrupado_filtrado, height=300, use_container_width=True)

    df_detalhado_filtrado = df_detalhado[df_detalhado["service"] == servico_selecionado]

    st.markdown(f"### 📜 Lista Completa de Erros no Serviço **{servico_selecionado}**")
    st.dataframe(df_detalhado_filtrado, height=400, use_container_width=True)
