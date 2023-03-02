# app.py, run with 'streamlit run app.py'
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import pymongo
from streamlit_autorefresh import st_autorefresh



# Initialize the MongoDb connection
# Use st.cache to cache the connection so it doesn't have to be reinitialized every time the app is run
@st.experimental_singleton
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

    sku_input.strip()

    # Create a number input to collect the quantity of the return
    quantity = st.number_input(label='Quantity', min_value=1, max_value=100)

    # Create a selectbox to collect the reason for the return
    reason_input = st.selectbox(label='Reason', options=[' ', 'Defective', 'Unwanted', 'Wrong Item', 'Missing Parts', 'Too Large', 'Too Small', 'Never Received', 'Missed Delivery Date', 'Bad Description'])

    # Create a text area to collect any notes from the user
    note_input = st.text_area(label='Notes')

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
                'Quantity': quantity,
                'Notes': note_input
            }
            # insert the document into the MongoDB collection
            collection.insert_one(doc)

            # display a success message
            st.success('Successfully saved')

            # Auto refresh when the form is submitted
            st_autorefresh()

# Create a dataframe from the MongoDB returns_collection collection
df = pd.DataFrame(list(collection.find()))

@st.experimental_singleton
def convert_df(df):
    return df.to_csv().encode('utf-8')

csv = convert_df(df)
st.download_button(
"Export to CSV",
csv,
"issue_tracker.csv",
"text/csv",
key='issue_tracker'
)

# Display the data in a table sorted by quantity and combine the sku and reason columns, ignoring the notes column
st.table(df.groupby(['SKU', 'Reason', 'Notes']).sum().reset_index().sort_values('Quantity', ascending=False).head(25))

# plot the data as a bar chart
st.bar_chart(df.groupby(['SKU', 'Reason'])['Quantity'].sum(numeric_only=True).unstack().head(25))

with st.sidebar:
        st.write("")



