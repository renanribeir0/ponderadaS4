import streamlit as st
from visoes.visoes_gerais import consultar_logs_por_level

def exibir_big_numbers(all_data):

    totals = consultar_logs_por_level(all_data)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown('<div class="metric-box">📜<br><span style="font-size: 18px; color:#555;">Total de Logs</span><br><b style="color:#222;">{}</b></div>'.format(totals['total_logs']), unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="metric-box">✅<br><span style="font-size: 18px; color:#555;">Sucesso (SUCCESS)</span><br><b style="color:#228B22;">{}</b></div>'.format(totals['total_success']), unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="metric-box">❌<br><span style="font-size: 18px; color:#555;">Erros (ERROR)</span><br><b style="color:#D9534F;">{}</b></div>'.format(totals['total_errors']), unsafe_allow_html=True)

    with col4:
        st.markdown('<div class="metric-box">⏳<br><span style="font-size: 18px; color:#555;">Latência Média</span><br><b style="color:#007BFF;">{:.2f} ms</b></div>'.format(totals['avg_latency']), unsafe_allow_html=True)
