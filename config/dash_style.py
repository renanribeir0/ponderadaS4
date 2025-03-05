import streamlit as st

def aplicar_estilos():
    """Aplica o CSS global para o dashboard."""
    st.markdown("""
        <style>
            /* Centralizar o título */
            .title {
                text-align: center;
                font-size: 26px;
                font-weight: 600;
                color: #444;
                margin-bottom: 20px;
            }

            /* Estilo para os big numbers */
            .metric-box {
                background-color: #F8F9FA;
                padding: 18px;
                border-radius: 10px;
                text-align: center;
                color: #333;
                font-size: 20px;
                font-weight: 600;
                border: 1px solid #ddd;
                box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.08);
                transition: all 0.3s ease-in-out;
            }

            .metric-box:hover {
                box-shadow: 4px 4px 12px rgba(0, 0, 0, 0.15);
                transform: translateY(-2px);
            }

            .refresh-button {
                text-align: center;
                margin-bottom: 15px;
            }
        </style>
    """, unsafe_allow_html=True)



    st.markdown('<h class="title">Dashboard de Telemetria</h>', unsafe_allow_html=True)