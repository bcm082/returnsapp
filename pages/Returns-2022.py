import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Create a title for the page
st.title('Returns Reason Dashboard - 2022')
st.write('Amazon Data from January 2022 to December 2022.')


# Create a dropdown to select the month of the data to display
month = st.selectbox(label='Select Month', options=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])

# If January is selected, display the data for January
if month == 'January':
    df = pd.read_csv('pages/data/January-2022.csv')
# If February is selected, display the data for February
elif month == 'February':
    df = pd.read_csv('pages/data/February-2022.csv')
# If March is selected, display the data for March
elif month == 'March':
    df = pd.read_csv('pages/data/March-2022.csv')
# If April is selected, display the data for April
elif month == 'April':
    df = pd.read_csv('pages/data/April-2022.csv')
# If May is selected, display the data for May
elif month == 'May':
    df = pd.read_csv('pages/data/May-2022.csv')
# If June is selected, display the data for June
elif month == 'June':
    df = pd.read_csv('pages/data/June-2022.csv')
# If July is selected, display the data for July
elif month == 'July':
    df = pd.read_csv('pages/data/July-2022.csv')
# If August is selected, display the data for August
elif month == 'August':
    df = pd.read_csv('pages/data/August-2022.csv')
# If September is selected, display the data for September
elif month == 'September':
    df = pd.read_csv('pages/data/September-2022.csv')
# If October is selected, display the data for October
elif month == 'October':
    df = pd.read_csv('pages/data/October-2022.csv')
# If November is selected, display the data for November
elif month == 'November':
    df = pd.read_csv('pages/data/November-2022.csv')
# If December is selected, display the data for December
elif month == 'December':
    df = pd.read_csv('pages/data/December-2022.csv')

st.subheader('Data from ' + month + ' 2022')

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


