import streamlit as st
import time


def exibir_botao_refresh():
    

    if st.button("🔄 Atualizar Dados"):
        with st.spinner("Atualizando os dados..."):
            time.sleep(1)
            st.rerun()