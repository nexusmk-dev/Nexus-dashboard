
import streamlit as st

st.set_page_config(
    page_title="Nexus Dashboard",
    page_icon="⚡",
    layout="wide"
)

st.title("⚡ NEXUS DASHBOARD")
st.caption("Central de controle do seu negócio")

st.subheader("Visão geral")

c1, c2, c3 = st.columns(3)

c1.metric("Vendas", "R$ 2.500", "+12%")
c2.metric("Clientes", "18", "+3")
c3.metric("Conversão", "12%", "+2%")

st.subheader("Desempenho de vendas")

st.bar_chart({
    "Vendas": [120, 180, 150, 260, 220, 320]
})

if st.button("Atualizar painel"):
    st.success("Painel atualizado!")
