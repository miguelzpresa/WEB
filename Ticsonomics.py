import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

# icon = Image.open('https://avatars.githubusercontent.com/u/127362849?s=200&v=4')
st.set_page_config(page_title='Ticsonomics', page_icon='https://avatars.githubusercontent.com/u/127362849?s=200&v=4', layout="wide")
st.sidebar.header("Ticsonomics")

'''
# Hi, we're Ticsonomics 👋
---
🧙 Welcome to our GitHub

Final project for the Distributed Computing subject, at ENES' Morelia B. Sc. Program "Tecnologías para la Información en Ciencias" (https://www.enesmorelia.unam.mx/)

Welcome to our  crypto-trading AI Platform! In this project, we aim to process historical data of cryptocurrencies to identify patterns and trends within their behavior, to understand their behavior in the market, identify trends and make informed decisions in the field of investment. Through the analysis of prices and other relevant indicators, such as KDJK, MACD, PPSR, and MACD, offer useful insights for investors, and allow them to use this information to make informed trading decisions.

____
# Team_Members :family:

* José Ignacio Ireta. ([ignacio-ireta](https://github.com/ignacio-ireta))
* María Lucrecia Beltz González ([LucreciaBeltz](https://github.com/LucreciaBeltz))
* Miguel Ángel Zamorano Presa. ([miguelzpresa](https://github.com/miguelzpresa))

____
# License :space_invader:
Copyright © 2023 <mikezpresa@gmail.com,ignacio.ireta@outlook.com>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

____
# Introduction :microscope:



The world of cryptocurrency is highly volatile, with prices fluctuating wildly within a matter of hours. To be successful in this space, traders must have a deep understanding of the behavior of each cryptocurrency they are trading. This is where data analysis comes in - by analyzing large amounts of historical data, we can identify patterns and trends that may not be visible through simple observation.

We have chosen to focus on several key indices, including: RSI_14, MACD, Stochastic Oscillator & PPSR(ivot Points, Supports, and Resistances )as these indices have proven to be effective in predicting market trends and making informed trading decisions. By calculating these indices for our univariate cripto system, we can identify potential entry and exit points for trades, and make more profitable trading decisions.

The TICSonomics project will focus on the analysis of the XRP cryptocurrency  using the information provided by the Coingecko API. The main objective is to create an artificial intelligence model that processes and stores this data to make decisions based on machine learning techniques and, finally, deploy the model in a web app accessible to users. 
In this project, we created a system that processes historical data  of the behavior of the XRP cryptocurrency price and then sends it to our website. The project is divided into 5 phases, each with its own objectives and challenges.



# Justification :telescope:
---
The comparison between the TICSonomics project and existing alternatives such as TradingView, TrendSpider, Koyfin, among others, lies mainly in the focus and automation of technical analysis. These existing platforms offer a wide range of tools and charts to perform fundamental and technical analysis of different assets, including cryptocurrencies. However, these tools require users to perform the analysis manually, which can result in a slower and error-prone process due to human subjectivity.  
TICSonomics sets itself apart from current alternatives by offering an automated, AI-based solution for cryptocurrency technical analysis. This can result in faster and more accurate decision making, as well as a more personalized and adaptable approach for investors compared to the manual tools offered by platforms such as TradingView, TrendSpider, and Koyfin.

# "Cryptocurrency Analysis: Mini Historical Overview and Essential Concepts":chart_with_upwards_trend:
---
### what are cryptocurrencies?  

A crypto a digital currency that uses cryptography to secure and verify transactions and to control the creation of new units. Cryptocurrencies are based on a technology called blockchain, which is a distributed and decentralized database that securely records all transactions.
Cryptocurrencies  offer several advantages over traditional fiat currencies. Firstly, cryptocurrencies allow for secure and fast transactions with low transaction fees. Unlike traditional fiat currencies, cryptocurrencies are not controlled by any government or central authority, which means that transactions can be processed faster and more securely, and are not subject to inflation or manipulation by central banks.
Cryptocurrencies matter because they offer a secure, fast, and efficient way to transact and transfer value globally, as well as a potential investment opportunity.

### Who and how is determined the value of any crypto?  

Like any other financial asset, the price of a cryptocurrency fluctuates based on the supply and demand of investors who buy and sell the currency on exchange markets.  

One key factor that influences the value of a cryptocurrency is its market capitalization (market cap). The market cap of a cryptocurrency is calculated by multiplying the current price of the cryptocurrency by the total number of coins in circulation. This metric provides an estimate of the relative size of the cryptocurrency in the market. Generally, the higher the market capitalization of a cryptocurrency, the higher its price, although this is not always the case.  

In addition to market capitalization, other factors that can influence the value of a cryptocurrency include:  

- The adoption and actual use of the cryptocurrency by businesses and consumers.
- The strength of the technology and security of the network on which the cryptocurrency is based.
- News and events related to the cryptocurrency and its underlying technology, such as protocol updates, security breaches, and government regulations.
- The market's perception of the value and utility of the cryptocurrency relative to other cryptocurrencies and financial assets.  

It is important to note that the value of cryptocurrencies can be extremely volatile due to the speculative nature of the cryptocurrency market. Therefore, investors should conduct their own research and analysis before investing in any cryptocurrency.

## Transactional Cycle overview   :round_pushpin:  

Exchanges usually follow the price of the cryptocurrency on its respective blockchain, as this is the real price of the cryptocurrency.  

In the case of XRP, the price is established on its blockchain, and exchanges that offer XRP rely on that price to determine its value. That is, it is not the exchange that determines the price of the cryptocurrency, but rather follows it through its blockchain.
Exchanges can set their own fees, but they generally adhere to market standards to avoid losing competitiveness. Regulation regarding exchange fees varies by country, but maximum limits are typically established to protect users from abusive prices."


# Arquitecture 
---
'''
path_arqui_image = 'images/Ticsonomics.png'
st.image(path_arqui_image)

'''
---
# Objectives_of_each_Phase :pushpin:
---
##### Phase 1: Data Acquisition
Obtain data on the XRP cryptocurrency from CoinGecko api.
Standardize the obtained data for use in the system.
##### Phase 2: Database System
Design and configure a suitable database for storing the obtained data.
Implement the necessary mechanisms to maintain data integrity.
##### Phase 3: Processor
Design and implement a data processing system to analyze the data obtained from the XRP cryptocurrency.
Develop algorithms and analysis techniques to extract relevant information from the data.
##### Phase 4: Website
Design and implement a website to display the information obtained and analyzed in the previous phases.
Develop a clear and intuitive data visualization system for users.
##### Phase 5: Integration and Testing
Integrate all the previous phases into a functional and efficient system.
Conduct exhaustive testing to ensure that the system works correctly in all situations.

# Data_Acquisition_System :satellite:
---
The provided Python script retrieves market data for a specific cryptocurrency from the CoinGecko API and stores it in a PostgreSQL database. It utilizes the pandas library for data manipulation and storage.  

The script consists of the following steps:  

    functions:  
        fetch_data_from_api(url): Sends a GET request to the API and returns the response as a JSON object.  
        get_ohcl(coin_id, vs_currency, days): Retrieves OHLC prices for a cryptocurrency within a timeframe and returns them as a pandas DataFrame.  
        get_volume(coin_id, vs_currency, days): Retrieves trading volume data for a cryptocurrency within a timeframe and returns it as a pandas DataFrame.  
        convert_timestamp(df): Converts the Unix timestamp in a DataFrame to a readable format.  
        pull_coin_data(coin_id, vs_currency, days): Retrieves OHLC prices and volume data, merges them, and returns a DataFrame.  
        get_latest_timestamp(db, table_name): Retrieves the latest timestamp stored in a specified table in the database.  
        store_data_to_db(df, db, table_name): Stores a DataFrame in the database, appending new data if available.  

    Connecting to the PostgreSQL database.  

    Retrieving data for different timeframes using the pull_coin_data() function.  
  
    Storing the data in the database using the store_data_to_db() function.  

The script allows for easy retrieval and storage of cryptocurrency market data from the CoinGecko API into a PostgreSQL database.
---
# Data Storage :floppy_disk:
---
### Dockerized PostgreSQL Database

This database system utilizes Docker and PostgreSQL to create a containerized environment for storing and managing data. The purpose of this system is to facilitate the management of cryptocurrency price data.  

The system includes three tables: assets, half_hours, and four_hours, each serving a specific purpose.  

The assets table stores information about different cryptocurrencies, including their unique identifier (coin_id) and symbol (symbol).  

The half_hours table records price data for cryptocurrencies at half-hour intervals, including the opening, high, low, closing prices (open, high, low, close) and trading volume (volume).  

Similarly, the four_hours table captures price data at four-hour intervals, with the same column structure as the half_hours table.  

All tables are created using the CREATE TABLE IF NOT EXISTS statement, ensuring they are only created if they do not already exist in the PostgreSQL database.    

The system leverages Docker to provide a containerized environment, which enhances portability, scalability, and ease of deployment. Docker enables isolation and simplifies the process of setting up the database system, making it more efficient and convenient to manage the PostgreSQL database for storing cryptocurrency price data.



---  
# Processing Data System :mailbox_with_mail:
---
Our Processing System code represents generates and processes data related to cryptocurrency price indicators.  

Functionalities  :
 The system consists of various functions:     
-RSI14(df, n): Calculates the RSI14 of a given DataFrame df using a specified window size n. The function adds the RSI_14 column to the DataFrame.  
-MACD(df): This function calculates the Moving Average Convergence Divergence (MACD) indicator for a given DataFrame df. Currently, it is commented out and not used in the code.    
-MOM(df, n): Computes the Momentum indicator for a given DataFrame df using a specified period n. The function adds the Momentum column to the DataFrame.    
-PPSR(df): Calculates Pivot Points, Supports, and Resistances (PPSR) for a given DataFrame df containing high, low, and close price values. The function adds columns for PP, R1, S1, R2, S2, R3, and S3 to the DataFrame.    
-graficador2(indi, temporalidad, cols=None): This function generates candlestick charts using the mplfinance library. It takes an indicator name (indi) and a time frame (temporalidad) as inputs. If the indicator is "ppsr," it plots the PPSR values from the DataFrame using the specified color (b). Otherwise, it plots the indicator values from the DataFrame using the corresponding color (b, g, or r). The function returns the generated chart and the modified DataFrame.

main():  
The main function serves as the entry point for the program. It prompts the user to select a cryptocurrency asset (bitcoin, ethereum, ripple, matic_network, or polkadot) and connects to the PostgreSQL database. It then retrieves price data for different indicators and time frames, such as RSI_14, MACD, Stochastic Indicator (Indi_Stocástico), and PPSR. The function calls graficador2 to generate charts and saves them as PNG images. It also saves the processed DataFrame as a CSV file.  The system provides flexibility for selecting different indicators and time frames for visualization and analysis. It utilizes PostgreSQL as the underlying database for data storage and retrieval.   

Output:  
The generated charts and processed data files are saved in the images_output and pdfs_output directories, respectively, within the same directory as the script.  Overall, this processor system offers a way to retrieve, process, and visualize cryptocurrency price data using various indicators, facilitating technical analysis and research.



Applying Indices: We will apply various indices such as IRS_14,MACD ,ppsr, and stochastic oscillator to the time series data at different time frames (e.g., daily, weekly, monthly, etc.). This will help us to identify potential entry and exit points for trades, as well as to identify patterns of trend, consolidation, resistance breakthroughs, and momentum.

Pattern Identification: Once we have applied the indices, we will use them to identify patterns of trend, consolidation, resistance breakthroughs, and momentum within the data. This will involve identifying support and resistance levels, analyzing trends and patterns over time, and identifying potential breakouts or breakdowns in the data.


# Web_Platform :european_castle:
---
The Web Platform  is designed to provide users with an interactive platform for analyzing historical data on various cryptocurrencies. The web app provides a variety of visualizations and analytical tools that allow users to gain insights into the behavior of different cryptocurrencies over time.

The web app is built on the * [streamlit](https://www.streamlit.io/) framework, which is a Python low-code framework for building web applications. The web app uses a combination of Python, HTML, CSS, and JavaScript to provide users with an interactive and responsive experience.

Features:

- Interactive price charts for various cryptocurrencies
- Customizable timeframes for analyzing data
- Price change percentage and volume data visualization
- Detailed price and volume data table
- User-friendly interface for easy navigation

# Deployment :calendar:
---
The deployment process for the "ticsonomics" project involves the following steps:  

    Change directory to the project's deployment folder.  
    Execute the Docker Compose file to set up the project's services and containers.  
    Wait for 60 seconds to ensure proper initialization.  
    Run a Python script related to the deployment process.  
    Stage and commit PDF files in the designated output directory using Git.  
    Push the committed changes to the remote Git repository.  
    Shut down and remove the services and containers created by Docker Compose.  

This deployment process enables easy access to image and CSV URLs associated with the web application, allowing users to request these resources at any time.
---

# Libraries :pencil2:
---
* [Python 3](https://www.python.org/)
* Linux Ubuntu    64-bit
* [Github](https://www.github.com)
* Windows 10      64-bit
* Jupyter lab     3.2.9
* git
* cron

# Packages :triangular_flag_on_post:  
---
* [Pandas version 1.4.1](https://pandas.pydata.org/)
* [Matplotlib version 3.2.2](https://matplotlib.org/)
* [Numpy version 1.21.5](https://numpy.org/) 
* [Docker Compose version v2.18.1](https://www.docker.com)
* [requests](https://docs.python-requests.org/)
* [mplfinance==0.12.9b7](https://pypi.org/project/mplfinance/)
* [psycopg2_binary==2.9.6](https://pypi.org/project/psycopg2-binary/)
* [SQLAlchemy==1.4.39](https://www.sqlalchemy.org/)
* [stockstats==0.5.2](https://pypi.org/project/stockstats/)
* [requests==2.31.0](https://pypi.org/project/requests/)
* 



---
# Executing_Software_Intructions :surfer:
---
1. clone the deployment repo
2. open the cron-instructions.txt file and follow its instructions
3. execute deployer.sh

---
# Conclusions: :pencil2:
The project aimed to develop a data acquisition system for cryptocurrency market data. The main objectives were to fetch data from an CoinGecko API, process it, store it in a database, and provide the ability to request image and CSV URLs associated with the data.  

Throughout the project, several key components and technologies were utilized. These included the API client, database management, deployment scripts, Docker, Python, Pandas, Matplotlib, Numpy, Git, and Cron.  

The data acquisition process involved making API requests to fetch OHLC prices and volume data for cryptocurrencies. Python and Pandas were used to process the data, converting timestamps, removing duplicates, and storing it in a PostgreSQL database.  

The processing  syste fetches cryptocurrency market data, performs data processing and analysis, and generates visualizations in the form of candlestick charts with technical indicators. The generated images and CSV files can be used for further analysis or reporting purposes. 

Deployment was facilitated through Docker and Docker Compose, ensuring easy setup and execution of the system. A deployment script managed container configuration, executed Python scripts, performed Git operations, and ensured the system was up and running.  

The project successfully accomplished its objectives, providing a functional data acquisition system. It effectively fetched, processed, and stored cryptocurrency market data, enabling users to access image and CSV URLs associated with the data. The automated deployment streamlined the setup process and ensured smooth execution.



---
# References :peach:
---
https://docs.streamlit.io/  
https://github.com/matplotlib/mplfinance/tree/master/examples  
https://github.com/jealous/stockstats  
https://docs.sqlalchemy.org/en/20/
https://www.coingecko.com/en/api/documentation  
https://docs.docker.com/desktop/
'''