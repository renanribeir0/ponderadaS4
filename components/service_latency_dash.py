import streamlit as st
import matplotlib.pyplot as plt
from visoes.service_latency import obter_eventos_por_servico

def exibir_servico_latency(all_data):



    df_grouped = obter_eventos_por_servico(all_data)


    st.subheader("Eventos por Serviço & Latência Média")

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.barh(df_grouped["service"], df_grouped["total_eventos"], color="#4CAF50", alpha=0.7)
    ax.set_xlabel("Total de Eventos")
    ax.set_ylabel("Serviço")
    ax.set_title("Quantidade de Eventos por Serviço")

    st.pyplot(fig)


    st.subheader("Tabela de Serviços")
    st.dataframe(df_grouped, height=400, use_container_width=True)
