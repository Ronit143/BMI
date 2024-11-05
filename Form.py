import streamlit as st
import pandas as pd

# Initialize a session state to store the DataFrame if not already present
if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=['Name', 'Age', 'Email'])

# Function to handle form submission and save to CSV
def submit_form():
    name = st.session_state.name
    age = st.session_state.age
    email = st.session_state.email
    
    # Append the new submission to the DataFrame
    new_data = pd.DataFrame([[name, age, email]], columns=['Name', 'Age', 'Email'])
    st.session_state.data = pd.concat([st.session_state.data, new_data], ignore_index=True)
    
    # Save the updated DataFrame to a CSV file
    save_data_to_csv()

# Function to save data to CSV
def save_data_to_csv():
    # Save the DataFrame to a CSV file in the current directory
    st.session_state.data.to_csv('submitted_data.csv', index=False)

# Streamlit form for user input
with st.form(key='data_form'):
    st.text_input('Name', key='name')
    st.number_input('Age', key='age', min_value=0)
    st.text_input('Email', key='email')
    
    submit_button = st.form_submit_button('Submit')

    if submit_button:
        submit_form()
        st.success('Data submitted successfully!')

# Display the collected data in a table
st.write("Collected Data")
st.dataframe(st.session_state.data)

# Optionally, allow the user to download the data as a CSV file
st.download_button(
    label="Download data as CSV",
    data=st.session_state.data.to_csv(index=False),
    file_name="submitted_data.csv",
    mime="text/csv"
)
