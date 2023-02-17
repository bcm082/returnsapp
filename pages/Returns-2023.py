import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Create a title for the page
st.title('Returns Reason Dashboard - 2023')
st.write('Amazon Data from January 2023 to December 2023.')


# Create a dropdown to select the month of the data to display
month = st.selectbox(label='Select Month', options=['January'])

# If January is selected, display the data for January
if month == 'January':
    df = pd.read_csv('pages/data/January-2023.csv')

st.subheader('Data from ' + month + ' 2023')

# Display to total number of returns
st.write('Total Returns: ' + str(df['Quantity'].sum()))

st.write('Top 25 Returns by SKU')
# Display the top 25 SKUs by quantity in a table
st.table(df.groupby('SKU').sum().reset_index().sort_values('Quantity', ascending=False).head(25))

st.write('Top 25 Reason by SKU')
# Display the data in a table sorted by quantity and combine the sku and reason columns
st.table(df.groupby(['SKU', 'Reason']).sum().reset_index().sort_values('Quantity', ascending=False).head(25))

st.write('Top 25 Reasons for Returns')
# Display the data in a table sort by reason and quantity
st.table(df.groupby('Reason').sum().reset_index().sort_values('Quantity', ascending=False))


