import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import requests


st.set_page_config(page_title='Dashboard', page_icon='https://avatars.githubusercontent.com/u/127362849?s=200&v=4', layout="wide")
st.sidebar.header("Dashboard")

'''
# Dashboard
'''
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

general_col1, general_col2 = st.columns(2)

with general_col1:

    # Create a container to display a image using the full column width.
    timeseries_container = st.container()

    # Create a container for the timeseries plot
    with timeseries_container:
        timeseries_df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

        fig = px.line(timeseries_df, x='Date', y='AAPL.High', title='Time Series with Range Slider and Selectors')

        fig.update_xaxes(
            rangeslider_visible=True,
            rangeselector=dict(
                buttons=list([
                    dict(count=1, label="1m", step="month", stepmode="backward"),
                    dict(count=6, label="6m", step="month", stepmode="backward"),
                    dict(count=1, label="YTD", step="year", stepmode="todate"),
                    dict(count=1, label="1y", step="year", stepmode="backward"),
                    dict(step="all")
                ])
            )
        )
        st.plotly_chart(fig, use_container_width=True)

with general_col2:
    ohlc_df = pd.read_csv('https://raw.githubusercontent.com/TICsonomics/Deployment/main/pdfs_output/ripple-kdjk-30%20minutos.csv')#https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')
    fig = go.Figure(data=go.Ohlc(x=ohlc_df['Date'],
                    open=ohlc_df['AAPL.Open'],
                    high=ohlc_df['AAPL.High'],
                    low=ohlc_df['AAPL.Low'],
                    close=ohlc_df['AAPL.Close']))
    # Set a title for the chart
    fig.update_layout(title_text='Apple Stock')
    st.plotly_chart(fig, use_container_width=True)

# Create a container for a timeseries prediction
with st.container():
    stocks_df = px.data.stocks()
    fig = px.line(stocks_df, x='date', y="GOOG")
    # Set a title for the chart
    fig.update_layout(title_text='Google Stock')
    st.plotly_chart(fig, use_container_width=True)

# Create a data frame of 8 columns and 4 rows.
# The first column is the date.
# The other 7 columns are some metrics for each cryptocurrency.
df = pd.DataFrame(
    np.random.randn(4, 6),
    columns=['Timestamp',  'Open', 'Close', 'High', 'Low', 'Volume']
)

st.dataframe(df, use_container_width=True)