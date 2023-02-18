import streamlit as st
import pandas as pd


# Create a title for the page
st.title('Returns Dashboard')

# Create a dropdown to select the year of the data to display
year = st.selectbox(label='Select Year', options=['2021', '2022', '2023'])

# Create a dropdown to select the month of the data to display
month = st.selectbox(label='Select Month', options=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])

# Select the data file to display based on the year and month selected
if year == '2021':
    if month == 'January':
        df = pd.read_csv('pages/data/2021/January-2021.csv')
    elif month == 'February':
        df = pd.read_csv('pages/data/2021/February-2021.csv')
    elif month == 'March':
        df = pd.read_csv('pages/data/2021/March-2021.csv')
    elif month == 'April':
        df = pd.read_csv('pages/data/2021/April-2021.csv')
    elif month == 'May':
        df = pd.read_csv('pages/data/2021/May-2021.csv')
    elif month == 'June':
        df = pd.read_csv('pages/data/2021/June-2021.csv')
    elif month == 'July':
        df = pd.read_csv('pages/data/2021/July-2021.csv')
    elif month == 'August':
        df = pd.read_csv('pages/data/2021/August-2021.csv')
    elif month == 'September':
        df = pd.read_csv('pages/data/2021/September-2021.csv')
    elif month == 'October':
        df = pd.read_csv('pages/data/2021/October-2021.csv')
    elif month == 'November':
        df = pd.read_csv('pages/data/2021/November-2021.csv')
    elif month == 'December':
        df = pd.read_csv('pages/data/2021/December-2021.csv')
elif year == '2022':
    if month == 'January':
        df = pd.read_csv('pages/data/2022/January-2022.csv')
    elif month == 'February':
        df = pd.read_csv('pages/data/2022/February-2022.csv')
    elif month == 'March':
        df = pd.read_csv('pages/data/2022/March-2022.csv')
    elif month == 'April':
        df = pd.read_csv('pages/data/2022/April-2022.csv')
    elif month == 'May':
        df = pd.read_csv('pages/data/2022/May-2022.csv')
    elif month == 'June':
        df = pd.read_csv('pages/data/2022/June-2022.csv')
    elif month == 'July':
        df = pd.read_csv('pages/data/2022/July-2022.csv')
    elif month == 'August':
        df = pd.read_csv('pages/data/2022/August-2022.csv')
    elif month == 'September':
        df = pd.read_csv('pages/data/2022/September-2022.csv')
    elif month == 'October':
        df = pd.read_csv('pages/data/2022/October-2022.csv')
    elif month == 'November':
        df = pd.read_csv('pages/data/2022/November-2022.csv')
    elif month == 'December':
        df = pd.read_csv('pages/data/2022/December-2022.csv')
elif year == '2023':
    if month == 'January':
        df = pd.read_csv('pages/data/2023/January-2023.csv')
    else:
        st.header('No Data Available')

# Display the data in a table
st.header('Data from ' + month + ' - ' + year)

# Display to total number of returns
st.subheader('Total Returns: ' + str(df['Quantity'].sum()))

st.subheader('Top 25 Returns by SKU')
# Display the top 25 SKUs by quantity in a table
st.table(df.groupby('SKU').sum().reset_index().sort_values('Quantity', ascending=False).head(25))

st.write('Top 25 Reason by SKU')
# Display the data in a table sorted by quantity and combine the sku and reason columns
st.table(df.groupby(['SKU', 'Reason']).sum().reset_index().sort_values('Quantity', ascending=False).head(25))

st.write('Top 25 Reasons for Returns')
# Display the data in a table sort by reason and quantity
st.table(df.groupby('Reason').sum().reset_index().sort_values('Quantity', ascending=False))
