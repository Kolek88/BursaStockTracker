import streamlit as st
import yfinance as yf
import pandas as pd
import time
import os

# Use a CSV file  for easy web hosting
CSV_FILE = 'portfolio.csv'

# Ensure the CSV exists. If not, create it with headers.
if not os.path.exists(CSV_FILE):
    df = pd.DataFrame(columns=['ticker', 'company_name', 'shares_owned', 'avg_buy_price'])
    df.to_csv(CSV_FILE, index=False)

def load_data():
    """Reads the portfolio from the CSV file."""
    return pd.read_csv(CSV_FILE)

def save_data(df):
    """Saves the portfolio to the CSV file."""
    df.to_csv(CSV_FILE, index=False)


st.title("Bursa Malaysia Portfolio Tracker")

# SIDEBAR: ADD NEW STOCK 
with st.sidebar:
    st.header("Add New Investment")
    
    new_ticker = st.text_input("Ticker Symbol (e.g., 1295.KL)")
    new_name = st.text_input("Company Name (e.g., Public Bank)")
    new_shares = st.number_input("Shares Bought", min_value=1, step=100)
    new_price = st.number_input("Buy Price (RM)", min_value=0.01, format="%.2f")

    if st.button("Add to Portfolio"):
        if new_ticker and new_name:
            try:
                # Load current data
                df = load_data()
                
                # Create a new row of data
                new_row = pd.DataFrame({
                    'ticker': [new_ticker],
                    'company_name': [new_name],
                    'shares_owned': [int(new_shares)],
                    'avg_buy_price': [float(new_price)]
                })
                
                # Add the new row to the existing data and save it
                df = pd.concat([df, new_row], ignore_index=True)
                save_data(df)
                
                st.success(f"Successfully added {new_name}!")
                time.sleep(1)
                st.rerun()
                
            except Exception as e:
                st.error(f"Error adding stock: {e}")
        else:
            st.warning("Please fill in both Ticker and Name.")

# MAIN DASHBOARD 
try:
    df = load_data()
    
    if df.empty:
        st.info("Your portfolio is empty! Add a stock using the sidebar.")
    else:
        st.subheader("1. My Holdings (Raw Data)")
        st.dataframe(df)

        st.subheader("2. Live Market Analysis")
        
        tickers = df['ticker'].tolist()
        ticker_string = " ".join(tickers) 
        
        # Suppress yfinance warnings and fetch data
        data = yf.download(ticker_string, period="1d", progress=False)['Close']
        
        # If there's only one stock, yf returns a Series, not a DataFrame
        if len(tickers) == 1:
            current_prices = {tickers[0]: data.iloc[-1]}
        else:
            current_prices = data.iloc[-1] 

        # Calculate live metrics
        df['Current Price'] = df['ticker'].apply(lambda x: float(current_prices[x]))
        df['Total Value'] = df['shares_owned'] * df['Current Price']
        df['Profit/Loss'] = df['Total Value'] - (df['shares_owned'] * df['avg_buy_price'])

        st.dataframe(df.style.format({
            "avg_buy_price": "RM {:.2f}",
            "Current Price": "RM {:.2f}",
            "Total Value": "RM {:.2f}",
            "Profit/Loss": "RM {:.2f}"
        }))

        total_value = df['Total Value'].sum()
        total_profit = df['Profit/Loss'].sum()
        
        st.metric(label="Total Portfolio Value", value=f"RM {total_value:,.2f}", delta=f"RM {total_profit:,.2f}")
            
        st.markdown("---")
        st.header("3. Stock Performance Explorer")

        stock_map = dict(zip(df['company_name'], df['ticker']))
        selected_name = st.selectbox("Select a company to analyze:", stock_map.keys())
        selected_ticker = stock_map[selected_name]

        if selected_ticker:
            st.write(f"Showing 6-month history for: **{selected_ticker}**")
            stock = yf.Ticker(selected_ticker)
            history_data = stock.history(period="6mo")
            
            if history_data.empty:
                st.error(f"Could not fetch history for {selected_ticker}. Try another stock.")
            else:
                history_data = history_data.reset_index()
                st.line_chart(history_data, x="Date", y="Close")

except Exception as e:
    st.error(f"An error occurred loading the dashboard: {e}")
