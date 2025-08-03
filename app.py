import streamlit as st
import plotly.express as px
import pandas as pd
import altair as alt



st.title("Analýza kosatců")
st.write("Aplikace, která zvládne vypsat a zanalyzovat typy kosatců")

df_iris = px.data.iris()
# st.table(df_iris)
# st.dataframe(df_iris, hide_index=True)

st.scatter_chart(df_iris, x="sepal_width", y="sepal_length", color="species")

df_administrativa = pd.read_csv("https://www.datakhk.cz/api/download/v1/items/17ef6289f56048d3adeac5425f7e9c41/csv?layers=0")
df_obce = df_administrativa['Název správního obvodu obce s rozšířenou působností'].value_counts().reset_index()
df_obce.columns = ['Obec', 'Počet']

chart = alt.Chart(df_obce).mark_bar().encode(
    x=alt.X('Obec', sort='-y'),
    y='Počet'
).properties(
    title='Počet obcí podle správních obvodů'
)


st.markdown('## Graf')
st.altair_chart(chart)
