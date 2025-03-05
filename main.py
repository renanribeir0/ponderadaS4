import streamlit as st
import components.big_numbers
import components.botao_refresh_dash
import components.eventos_por_tempo
import components.service_latency_dash
import components.erros_por_servico
import config.dash_style
import visoes.consultar_todos_logs

def main():
    
    st.set_page_config(page_title="Dashboard de Telemetria", layout="wide")

    
    config.dash_style.aplicar_estilos()

    
    st.markdown("## 📊 Dashboard de Telemetria")
    st.markdown("---")

    
    components.botao_refresh_dash.exibir_botao_refresh()

    
    all_data = visoes.consultar_todos_logs.consultar_todos_logs()

    
    tab1, tab2, tab3, tab4 = st.tabs([
        "📌 Resumo", "📈 Eventos no Tempo", "🔍 Análise por Serviço", "❌ Erros por Serviço"
    ])

    with tab1:
        st.markdown("### 🔹 Resumo Geral")
        components.big_numbers.exibir_big_numbers(all_data)

    with tab2:
        st.markdown("### 🔹 Eventos ao Longo do Tempo")
        components.eventos_por_tempo.exibir_eventos_por_tempo(all_data)

    with tab3:
        st.markdown("### 🔹 Análise por Serviço")
        components.service_latency_dash.exibir_servico_latency(all_data)

    with tab4:
        st.markdown("### ❌ Análise de Erros por Serviço")
        components.erros_por_servico.exibir_erros_por_servico(all_data)

if __name__ == "__main__":
    main()
