import streamlit as st
import plotly.express as px
from visoes.eventos_por_tempo import obter_eventos_por_tempo

def exibir_eventos_por_tempo(all_data):


    granularidade = st.selectbox(
        "Selecione a granularidade do tempo:",
        ["ano", "mês", "dia", "hora", "minuto"],
        index=3  
    )


    df_grouped = obter_eventos_por_tempo(all_data, granularidade)

    df_grouped = df_grouped[df_grouped["total_eventos"] > 0]

    df_grouped["tempo"] = df_grouped["tempo"].astype(str)

    fig = px.line(
        df_grouped,
        x="tempo",
        y="total_eventos",
        markers=True,
        title=f"Evolução dos Eventos por {granularidade.capitalize()}",
    )

    fig.update_layout(xaxis_type="category")


    fig.update_xaxes(title_text="Tempo", tickangle=-45, showgrid=True)

    st.plotly_chart(fig, use_container_width=True)


