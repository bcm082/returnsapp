import streamlit as st
import pandas as pd


# Create a title for the page
st.title('Returns By Year and Month')

# Create a dropdown to select the year of the data to display
year = st.selectbox(label='Select Year', options=['2021', '2022', '2023'])

# Create a dropdown to select the month of the data to display
month = st.selectbox(label='Select Month', options=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])

# Select the data file to display based on the year and month selected
valid_years = ['2021', '2022', '2023']
valid_months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

if year in valid_years and month in valid_months:
    file_path = f'pages/data/{year}/{month}-{year}.csv'
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        st.header('No Data Available')
else:
    st.header('Invalid Year or Month')


# Display the data in a table
st.header('Data from ' + month + ' - ' + year)

# Display to total number of returns
st.subheader('Total Returns: ' + str(df['Quantity'].sum()))

st.markdown('---')

st.subheader('Top 25 Returns by SKU')
# Display the top 25 SKUs by quantity in a table
st.table(df.groupby('SKU').sum().reset_index().sort_values('Quantity', ascending=False).head(25))

st.markdown('---')

st.subheader('Top 25 Reason by SKU')
# Display the data in a table sorted by quantity and combine the sku and reason columns
st.table(df.groupby(['SKU', 'Reason']).sum().reset_index().sort_values('Quantity', ascending=False).head(25))

st.markdown('---')

st.subheader('Top 25 Reasons for Returns')
# Display the data in a table sort by reason and quantity
st.table(df.groupby('Reason').sum().reset_index().sort_values('Quantity', ascending=False))
