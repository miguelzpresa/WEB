import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import plotly.express as px
import requests


st.set_page_config(page_title='Indicador PPSR', page_icon='https://avatars.githubusercontent.com/u/127362849?s=200&v=4', layout="wide")
st.sidebar.header("Indicador PPSR")

coin_gecko_response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=ripple&vs_currencies=usd&include_24hr_change=true').json()
xrp_val = coin_gecko_response['ripple']['usd']
xrp_delta = coin_gecko_response['ripple']['usd_24h_change']

cripto_col1, cripto_col2, cripto_col3, cripto_col4 = st.columns(4)

# Add an icon to the first metric
with cripto_col1:
    # Set the columns to have no space between them
    col1, col2 = st.columns([1, 2])
    col1.image('assets/xrp-logo.png', use_column_width=True)
    # Grab only 2 characters from the string (0.00%)
    col2.metric(label="XRP", value="$"+str(xrp_val), delta=str(xrp_delta)[:4]+"%")

st.write('---')

'''
# Indicador PPSR
'''

########### PPSR 30 minutos ###########
ppsr_30_min = pd.read_csv('https://raw.githubusercontent.com/TICsonomics/Deployment/main/pdfs_output/ripple-ppsr-30%20minutos.csv')
with st.container():
    fig = go.Figure(data=go.Ohlc(x=ppsr_30_min.index,
                                 open=ppsr_30_min['open'],
                                 high=ppsr_30_min['high'],
                                 low=ppsr_30_min['low'],
                                 close=ppsr_30_min['close']))
    # Set a title for the chart
    fig.update_layout(
        title_text='PPSR 30 minutos',
        xaxis_title="Index",
        yaxis_title="Price",
    )
    st.plotly_chart(fig, use_container_width=True)

with st.container():
    #Y= ['PP','R1','S1','R2','S2','R3','S3'] 
    fig = px.line(ppsr_30_min, x=ppsr_30_min.index, y=['PP','R1','S1','R2','S2','R3','S3'] ,title ="30 mins")
    fig.update_layout(
        xaxis_title="Index",
        yaxis_title="PPSR",
    )
    st.plotly_chart(fig, use_container_width=True)

st.dataframe(ppsr_30_min, use_container_width=True)

st.write('---')

########### PPSR 4 horas ###########
ppsr_4_horas = pd.read_csv('https://raw.githubusercontent.com/TICsonomics/Deployment/main/pdfs_output/ripple-ppsr-4%20horas.csv')
with st.container():
    fig = go.Figure(data=go.Ohlc(x=ppsr_4_horas['date_price'],
                                     open=ppsr_4_horas['open'],
                                     high=ppsr_4_horas['high'],
                                     low=ppsr_4_horas['low'],
                                     close=ppsr_4_horas['close']))
    fig.update_layout(
        title_text='PPSR 4 horas',
        xaxis_title="Date",
        yaxis_title="Price",
    )

    st.plotly_chart(fig, use_container_width=True)

with st.container():
    fig = px.line(ppsr_4_horas, x=ppsr_4_horas['date_price'], y=['PP','R1','S1','R2','S2','R3','S3'] ,title =" 4hrs")
    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="PPSR",
    )
    st.plotly_chart(fig, use_container_width=True)

st.dataframe(ppsr_4_horas, use_container_width=True)

st.write('---')

########### PPSR 4 días ###########
ppsr_4_dias = pd.read_csv('https://raw.githubusercontent.com/TICsonomics/Deployment/main/pdfs_output/ripple-ppsr-4%20d%C3%ADas.csv')
with st.container():
    fig = go.Figure(data=go.Ohlc(x=ppsr_4_dias['date_price'],
                                     open=ppsr_4_dias['open'],
                                     high=ppsr_4_dias['high'],
                                     low=ppsr_4_dias['low'],
                                     close=ppsr_4_dias['close']))
    fig.update_layout(
        title_text='PPSR 1 día',
        xaxis_title="Date",
        yaxis_title="Price",
    )

    st.plotly_chart(fig, use_container_width=True)

with st.container():
    fig = px.line(ppsr_4_dias, x=ppsr_4_dias['date_price'], y=['PP','R1','S1','R2','S2','R3','S3'] ,title =" 4days")
    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="PPSR",
    )
    st.plotly_chart(fig, use_container_width=True)

st.dataframe(ppsr_4_dias, use_container_width=True)