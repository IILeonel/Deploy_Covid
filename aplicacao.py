import streamlit as st
import plotly.graph_objs as go
import pandas as pd

st.text('COVID MUNDIAL 2020')

data_url = ('https://raw.githubusercontent.com/nikkisharma536/streamlit_app/master/covid.csv')

data = pd.read_csv(data_url)
data = data.rename(columns={'Latitude': 'latitude', 'Longitude': 'longitude'})

df = data

st.map(df) 
