import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import requests


st.set_page_config(page_title='Indicador RSI', page_icon='https://avatars.githubusercontent.com/u/127362849?s=200&v=4', layout="wide")
st.sidebar.header("Indicador RSI")

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
# Indicador RSI
'''

########### RSI 30 minutos ###########
rsi_30_min = pd.read_csv('https://raw.githubusercontent.com/TICsonomics/Deployment/main/pdfs_output/ripple-rsi_14-30%20minutos.csv')
with st.container():
    fig = go.Figure(data=go.Ohlc(x=rsi_30_min.index,
                                 open=rsi_30_min['open'],
                                 high=rsi_30_min['high'],
                                 low=rsi_30_min['low'],
                                 close=rsi_30_min['close']))
    
    fig.update_layout(
        title_text='RSI 30 minutos',
        xaxis_title="Index",
        yaxis_title="Price",
    )
    st.plotly_chart(fig, use_container_width=True)

with st.container():
    fig = go.Figure(data=[go.Bar(x=rsi_30_min.index, y=rsi_30_min['volume'], marker_color='purple')])
    fig.update_layout(
        xaxis_title="Index",
        yaxis_title="Volumen",
    )
    st.plotly_chart(fig, use_container_width=True)

st.dataframe(rsi_30_min, use_container_width=True)

st.write('---')

########### RSI 4 horas ###########
rsi_4_horas = pd.read_csv('https://raw.githubusercontent.com/TICsonomics/Deployment/main/pdfs_output/ripple-rsi_14-4%20horas.csv')
with st.container():
    fig = go.Figure(data=go.Ohlc(x=rsi_4_horas['date_price'],
                                      open=rsi_4_horas['open'],
                                      high=rsi_4_horas['high'],
                                      low=rsi_4_horas['low'],
                                      close=rsi_4_horas['close']))
    fig.update_layout(
        title_text='RSI 4 horas',
        xaxis_title="Date",
        yaxis_title="Price",
    )

    st.plotly_chart(fig, use_container_width=True)

with st.container():
    fig = go.Figure(data=[go.Bar(x=rsi_4_horas['date_price'], y=rsi_4_horas['volume'], marker_color='purple')])
    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Volumen",
    )
    st.plotly_chart(fig, use_container_width=True)

st.dataframe(rsi_4_horas, use_container_width=True)

st.write('---')

########### RSI 4 días ###########
rsi_4_dias = pd.read_csv('https://raw.githubusercontent.com/TICsonomics/Deployment/main/pdfs_output/ripple-rsi_14-4%20d%C3%ADas.csv')
with st.container():
    fig = go.Figure(data=go.Ohlc(x=rsi_4_dias['date_price'],
                                      open=rsi_4_dias['open'],
                                      high=rsi_4_dias['high'],
                                      low=rsi_4_dias['low'],
                                      close=rsi_4_dias['close']))
    fig.update_layout(
        title_text='RSI 4 días',
        xaxis_title="Date",
        yaxis_title="Price",
    )

    st.plotly_chart(fig, use_container_width=True)

with st.container():
    fig = go.Figure(data=[go.Bar(x=rsi_4_dias['date_price'], y=rsi_4_dias['volume'], marker_color='purple')])
    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Volumen",
    )
    st.plotly_chart(fig, use_container_width=True)

st.dataframe(rsi_4_dias, use_container_width=True)