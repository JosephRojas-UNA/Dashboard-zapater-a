import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# Datos
# -----------------------------
df_racks = pd.DataFrame({
    "País": ["Costa Rica", "Nicaragua", "Honduras", "El Salvador", "Guatemala", "Panamá"],
    "Regulaciones Aduaneras": [4,1,3,3,3,2],
    "Competencia Local": [2,2,4,3,2,3],
    "Costos de Transporte": [1,1,3,3,2,3],
    "Aranceles": [4,4,4,4,2,3]
})

df_demanda = pd.DataFrame({
    "País": ["Costa Rica", "Nicaragua", "Honduras", "El Salvador", "Guatemala", "Panamá"],
    "Demanda Hombre": [30312, 31631, 27591, 38837, 38655, 43771],
    "Demanda Mujer": [24002, 34877, 54269, 50484, 18998, 23428]
})

df_riesgo = pd.DataFrame({
    "País": ["Costa Rica", "Nicaragua", "Honduras", "El Salvador", "Guatemala", "Panamá"],
    "Riesgo Político": [8, 1, 2, 8, 8, 8],
    "Riesgo Económico": [6, 7, 3, 2, 6, 2],
    "Riesgo Social": [5, 5, 3, 3, 7, 9]
})

df_competencia = pd.DataFrame({
    "País": ["Costa Rica", "Nicaragua", "Honduras", "El Salvador", "Guatemala", "Panamá"],
    "Competidor A": [28835, 7002, 18228, 12837, 28364, 11578],
    "Competidor B": [13061, 6311, 24347, 23772, 23990, 24784],
    "Competidor C": [14843, 17046, 19676, 6860, 19433, 3413]
})

# -----------------------------
# Título y menú
# -----------------------------
st.set_page_config(page_title="Dashboard de Países", layout="wide")
st.title("🌎 Dashboard Interactivo de Evaluación de Países")

menu = st.sidebar.selectbox("Selecciona la sección:", ["Racks", "Demanda", "Riesgo", "Competencia"])

# -----------------------------
# Sección: Racks
# -----------------------------
if menu == "Racks":
    st.subheader("📦 Evaluación de Racks Logísticos")
    st.dataframe(df_racks.set_index("País"))

    st.markdown("### Comparación por categoría")
    categoria = st.selectbox("Selecciona una categoría", df_racks.columns[1:])
    fig = px.bar(df_racks, x="País", y=categoria, color="País", title=f"{categoria} por País")
    st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# Sección: Demanda
# -----------------------------
elif menu == "Demanda":
    st.subheader("📊 Análisis de la Demanda")
    st.dataframe(df_demanda.set_index("País"))

    fig = px.bar(df_demanda, x="País", y=["Demanda Hombre", "Demanda Mujer"],
                 barmode="group", title="Demanda por Género")
    st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# Sección: Riesgo
# -----------------------------
elif menu == "Riesgo":
    st.subheader("⚠️ Análisis de Riesgos por País")
    st.dataframe(df_riesgo.set_index("País"))

    fig = px.line(df_riesgo, x="País",
                  y=["Riesgo Político", "Riesgo Económico", "Riesgo Social"],
                  markers=True, title="Comparación de Riesgos")
    st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# Sección: Competencia
# -----------------------------
elif menu == "Competencia":
    st.subheader("🏁 Análisis de Competidores")
    st.dataframe(df_competencia.set_index("País"))

    pais = st.selectbox("Selecciona un país para analizar competencia:", df_competencia["País"])
    datos_pais = df_competencia[df_competencia["País"] == pais].set_index("País").T
    fig = px.bar(datos_pais, y=pais, orientation="v", title=f"Competencia en {pais}", labels={"index": "Competidor", pais: "Cantidad"})
    st.plotly_chart(fig, use_container_width=True)

