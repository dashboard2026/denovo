
import streamlit as st
import pandas as pd

st.title("Tabela Excel carregada direto do disco")

# Caminho do seu arquivo Excel
caminho_arquivo = 'CARTEIRA_DI_GASPI_24.04.xlsx'

try:
    # Carregar a planilha
    df = pd.read_excel(caminho_arquivo)
    st.success("Arquivo carregado com sucesso!")
    st.dataframe(df)

except FileNotFoundError:
    st.error(f"Arquivo não encontrado no caminho: {caminho_arquivo}")

except Exception as e:
    st.error(f"Ocorreu um erro ao ler o arquivo: {e}")
