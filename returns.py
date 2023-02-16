# app.py, run with 'streamlit run app.py'
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import pymongo


# Initialize the MongoDb connection
# Use st.cache to cache the connection so it doesn't have to be reinitialized every time the app is run
@st.cache_resource
def init_connection():
    return pymongo.MongoClient("mongodb+srv://"+st.secrets['username']+":"+st.secrets['password']+"@"+st.secrets['cluster_id']+".xq4stxw.mongodb.net/?retryWrites=true&w=majority")

client = init_connection()

# Connect to the returnsdb database and returns_collection collection
db = client['returnsdb']
collection = db['returns_collection']

# Create a form to collect the user's input
st.title('TVSO Customer Service Form')
with st.form(key='returns_form', clear_on_submit=True):
    sku_input = st.text_input(label='SKU')

    # Create a number input to collect the quantity of the return
    quantity = st.number_input(label='Quantity', min_value=1, max_value=100)

    # Create a selectbox to collect the reason for the return
    reason_input = st.selectbox(label='Reason', options=[' ', 'Damaged', 'Defective', 'Wrong Item', 'Missing Parts', 'Too Large', 'Too Small', 'Never Received'])

    # Stop the user from submitting the form if the SKU or reason is blank
    if sku_input == '' or reason_input == ' ':
        st.form_submit_button('Submit', on_click=None, args=None, kwargs=None)
    else:
        # add a button to submit the form
        if st.form_submit_button('Submit'):
            # create a new document to save to MongoDB
            doc = {
                'SKU': sku_input,
                'Reason': reason_input,
                'Quantity': quantity
            }
            # insert the document into the MongoDB collection
            collection.insert_one(doc)

            # display a success message
            st.success('Successfully saved')

# Create a dataframe from the MongoDB returns_collection collection
df = pd.DataFrame(list(collection.find()))

# Display the data in a table sorted by quantity and combine the sku and reason columns
st.table(df.groupby(['SKU', 'Reason']).sum().reset_index().sort_values('Quantity', ascending=False).head(25))

# plot the data as a bar chart
st.bar_chart(df.groupby(['SKU', 'Reason'])['Quantity'].sum(numeric_only=True).unstack().head(25))


