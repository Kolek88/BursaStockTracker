#  Bursa Malaysia Portfolio Tracker

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)]([https://bursastocktracker-klhqfrbndhfvcvckxnc3f3.streamlit.app/])

##  Overview
The Bursa Malaysia Portfolio Tracker is a full-stack, interactive web application designed to help investors monitor their Malaysian stock market holdings in real-time. Built specifically for Data Analysis and Financial Tracking, this dashboard replaces manual spreadsheet tracking with automated live data extraction.

## Live Demo
Check out the live web application here: **[[https://bursastocktracker-klhqfrbndhfvcvckxnc3f3.streamlit.app/](https://bursastocktracker-klhqfrbndhfvcvckxnc3f3.streamlit.app/)]]**

## Key Features
* **Live Market Data:** Integrates with the `yfinance` API to fetch real-time stock prices for Bursa Malaysia tickers.
* **Automated Financial Metrics:** Instantly calculates Current Portfolio Value, Total Profit/Loss, and individual asset performance.
* **Interactive Data Visualization:** Generates dynamic, 6-month historical performance line charts for deeper trend analysis.
* **Portfolio Management:** Allows users to input and save new stock purchases (Ticker, Company Name, Shares, Buy Price) directly through a user-friendly sidebar interface.
* **Persistent Storage:** Utilizes a localized CSV database structure (`portfolio.csv`) using Pandas to ensure data is saved and retrieved efficiently.

## Technologies Used
* **Python:** Core programming language.
* **Streamlit:** Front-end framework for building the interactive web application.
* **Pandas:** Data manipulation, cleaning, and CSV file management.
* **yfinance:** API library used to scrape live market data from Yahoo Finance.

## How to Run Locally

If you would like to run this project on your own machine, follow these steps:

1. **Clone the repository:**
git clone [https://github.com/Kolek88/bursa-stock-tracker.git](https://github.com/Kolek88/bursa-stock-tracker.git)
   
2. **Navigate into the project directory:**
   cd bursa-stock-tracker

3. **Install the required dependencies:**
   pip install -r requirements.txt

4.**Run the Streamlit application:**
   streamlit run bursa_app.py / py -m streamlit run bursa_app.py

Initial versions of this application utilized a local PostgreSQL database (psycopg2) for backend storage. It was adapted to utilize Pandas and CSV for seamless cloud deployment on Streamlit Community Cloud.

