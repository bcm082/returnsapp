# app.py, run with 'streamlit run app.py'
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt


# Create a sidebar with a dropdown menu
st.sidebar.title("Select a file")
file = st.sidebar.selectbox("Select a file", ("December_2022.csv", "Jan_2023.csv", "Feb_2023.csv"))


df = pd.read_csv("December_2022.csv")  # read a CSV file inside the 'data" folder next to 'app.py'
# df = pd.read_excel(...)  # will work for Excel files

df.dropna(how="all", inplace=True)  # drop empty rows

st.title('December 2022 Returns')  # print a text


# Compare 'Merchant SKU' and 'Return quantity' vs 'SKU Shipped' and 'Total Shipped' for the top 10 'Merchant SKU'. Format the numbers to be in thousands.
st.title("Comparison of Returns vs Shipped")
st.write(df.groupby('Merchant SKU')['Return quantity', 'SKU Shipped', 'Total Shipped'].sum().sort_values(by='Return quantity', ascending=False).head(10).style.format("{:,.0f}"))

# Plot a bar chart of 'Merchant SKU' and 'Return quantity' vs 'SKU Shipped' and 'Total Shipped' for the top 10 'Merchant SKU'. Format the numbers to be in thousands.
st.title("Bar Chart of Returns vs Shipped")
st.bar_chart(df.groupby('Merchant SKU')['Return quantity', 'SKU Shipped', 'Total Shipped'].sum().sort_values(by='Return quantity', ascending=False).head(10).style.format("{:,.0f}"))

# Count how many total 'Return Reason' there are by 'Merchant SKU' and sort them
st.title("Total Returns by Reason")
st.write(df.groupby('Return Reason')['Return quantity'].sum().sort_values(ascending=False))

# Plot a bar chart of 'Return Reason' and 'Return quantity'
st.title("Bar Chart of Returns by Reason")
st.bar_chart(df.groupby('Return Reason')['Return quantity'].sum().sort_values(ascending=False))


# Count how many total 'Return Reason' there are by 'Merchant SKU' and 'Return quantity' sort them
st.title("Total Returns by SKU and Reason")
st.write(df.groupby(['Merchant SKU', 'Return Reason'])['Return quantity'].sum().sort_values(ascending=False))



