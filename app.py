import streamlit as st
import pandas as pd
import plotly.express as px

st.title("COVID-19 Unemployment Tracker - India")

# Load our data
df = pd.read_csv('data/Unemployment_Rate_upto_11_2020.csv')
df.columns = ['State', 'Date', 'Frequency', 'Unemployment_Rate', 'Employed', 'Labour_Participation_Rate', 'Region', 'Longitude', 'Latitude']
df['Date'] = pd.to_datetime(df['Date'].str.strip(), format='%d-%m-%Y')

# Interactive Graph
st.subheader("Unemployment Trends Over Time")
timeline = df.groupby('Date')['Unemployment_Rate'].mean().reset_index()
fig = px.line(timeline, x='Date', y='Unemployment_Rate', markers=True)
st.plotly_chart(fig)

# Show Data Option
if st.checkbox("Show Raw Data"):
    st.write(df)