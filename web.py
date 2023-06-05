import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

# icon = Image.open('https://avatars.githubusercontent.com/u/127362849?s=200&v=4')
st.set_page_config(page_title='Ticsonomics', page_icon='https://avatars.githubusercontent.com/u/127362849?s=200&v=4', layout="wide")
st.sidebar.header("Ticsonomics")

'''
# Hi,we´re Ticsonomics 👋
---
🧙 Welcome to our GitHub org

"Final Project",UNAM (https://www.unam.mx/) -TICs-Distributed Computing 2023-1 class  

Welcome to our  crypto-trading AI Platform! In this project, we aim to process historical data of cryptocurrencies to identify patterns and trends within their behavior, to understand their behavior in the market, identify trends and make informed decisions in the field of investment. Through the analysis of prices and other relevant indicators, such as RSI, MACD, volume, Parabolic Sar and Bollinger bands, machine learning models can be generated to predict the future behavior of cryptocurrencies and offer useful recommendations for investors.and use this information to make informed trading decisions.

____
# Team_Members :family:

* José Ignacio Ireta. ([}ignacio-ireta](https://github.com/ignacio-ireta))
* María Lucrecia Beltz González ([LucreciaBeltz](https://github.com/LucreciaBeltz))
* Gerardo Zabdiel Martinez Zavala ([ZabdielZ](https://github.com/ZabdielZ))
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

We have chosen to focus on several key indices, including: IRS,  Fibonacci retracement as these indices have proven to be effective in predicting market trends and making informed trading decisions. By calculating these indices for our univariate cripto system, we can identify potential entry and exit points for trades, and make more profitable trading decisions.

The TICSonomics project will focus on the analysis of the XRP cryptocurrency from August 2013 to date, using the information provided by the Coingecko API. The main objective is to create an artificial intelligence model that processes and stores this data to make decisions based on machine learning techniques and, finally, deploy the model in a web app accessible to users. 
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
![Ticsonomics4](https://github.com/TICsonomics/.github/blob/main/Ticsonomics(1).png)







---
![Arquitecture![Ticsonomics](https://user-images.githubusercontent.com/49998408/235947042-753ae6b7-6e1d-4283-86d0-2e6fe7e9cbe9.png)
 ](https://github.com/TICsonomics/.github/blob/main/arqui.png)



---
# Objectives_of_each_Phase :pushpin:
---
##### Phase 1: Data Acquisition
Obtain data on the XRP cryptocurrency from Coin Market Cap api.
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
During the first iterations of the project, free software tools for information acquisition and storage will be considered. Seeking to be able to count from the beginning with the minimum information essential for the project such as the opening price, maximum, minimum, closing and volume of the asset of interest. Currently, various sources of information have already been considered, with historical prices dating back to the inception of the first asset to be analyzed, the Ripple cryptocurrency with XRP ticker, which have public APIs, which, although free, do not seem to provide adequate access to the information. necessary information in its free versions, however our specialists ensure that it is possible to obtain them from various sources or derive them from those already mentioned.

# Data Storage :floppy_disk:
---
data lake
Data warehousing
Possible tools to use for data storage:
-Apache Hive
-Apache Spark
In this stage, a division will be made in the database to store all the types of data and the different phases in which they are found.
The first division of the database will be to store the data provided by the data acquisition system, these data will be the ones that are worked on during the processing stage and the results of this stage will be stored in the second division of the database. of data so that they can be used in the publication stage  
# Processing Data System :mailbox_with_mail:
---
In this project, we aim to process historical data of cryptocurrencies to identify patterns and trends within their behavior, and use this information to make informed trading decisions.

We have chosen to focus on several key indices, including: IRS, Pivot Point, Fibonacci retracement, EMA, and stochastic oscillator, as these indices have proven to be effective in predicting market trends and making informed trading decisions. By calculating these indices for various cryptocurrencies, we can identify potential entry and exit points for trades, and make more profitable trading decisions.  

##### Methodology:

Exploratory Data Analysis (EDA) : We will begin by performing exploratory data analysis of the provided historical data to identify any trends or patterns in the time series data. This will involve visualizing the data, analyzing the distribution of the data, and identifying any outliers or anomalies.

Statistical Techniques: We plan to use a variety of statistical techniques to analyze the time series data, including time series decomposition, autocorrelation analysis, and statistical modeling. These techniques will help us to identify any trends, seasonal patterns, or other time-dependent relationships within the data.

Applying Indices: We will apply various indices such as IRS, Fibonacci, EMA, and stochastic oscillator to the time series data at different time frames (e.g., daily, weekly, monthly, etc.). This will help us to identify potential entry and exit points for trades, as well as to identify patterns of trend, consolidation, resistance breakthroughs, and momentum.

Pattern Identification: Once we have applied the indices, we will use them to identify patterns of trend, consolidation, resistance breakthroughs, and momentum within the data. This will involve identifying support and resistance levels, analyzing trends and patterns over time, and identifying potential breakouts or breakdowns in the data.


# Web_Platform :european_castle:
---
The Web Platform for this phase is designed to provide users with an interactive platform for analyzing historical data on various cryptocurrencies. The web app provides a variety of visualizations and analytical tools that allow users to gain insights into the behavior of different cryptocurrencies over time.

The web app is built on the [Dash](https://dash.plotly.com/) framework, which is a Python low-code framework for building web applications. The web app uses a combination of Python, HTML, CSS, and JavaScript to provide users with an interactive and responsive experience.

These Website will include:

- Interactive price charts for various cryptocurrencies
- Customizable timeframes for analyzing data
- Price change percentage and volume data visualization
- Detailed price and volume data table
- User-friendly interface for easy navigation

# Deployment :calendar:
---
Creation of container images  
We start creating  container images for each of the subsystems. It must be ensured that the images are compatible with the deployment environment and meet the system requirements. A version control system like Git can be used to manage code and configurations.

Deployment of containers  
Once container images have been created, they must be deployed. We will use  Docker Compose for  deployment. It must be ensured that the containers are deployed correctly and running optimally.

System configuration and testing  
After the containers have been deployed correctly, the system must be configured. This may include configuring databases, web pages, and connections between subsystems. Tests must be performed to ensure that everything is working correctly, and the system is ready to use.

Monitoring and maintenance of the system  
Once the system is in production, it must be ensured that it remains up-to-date and running optimally. This may include software updates, security patches, and troubleshooting errors. A monitoring system must also be implemented to keep track of any issues that may arise.
#L
---

# Libraries :pencil2:
---
* [Python 3](https://www.python.org/)
* Linux Ubuntu    64-bit
* [Github](https://www.github.com)
* Windows 10      64-bit
* Jupyter lab     3.2.9

# Packages :triangular_flag_on_post:  
---
* [Pandas    version 1.4.1](https://pandas.pydata.org/)
* [Matplotlib version 3.2.2](https://matplotlib.org/)
* [Numpy      version 1.21.5](https://numpy.org/) 
* [poetry     version](https://python-poetry.org)
* [Docker     version](https://www.docker.com)



# Executing_Software_Intructions :surfer:
---

# References :peach:
---

'''