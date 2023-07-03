# Start streamlit app :: " streamlit run front.py "

import streamlit as st
import requests

# Function to send the request to the API
def send_request():
    # Define the API endpoint
    url = 'http://localhost:5000/predict'
    
    # Get the input text from the input field
    input_text = input_field
    
    # Define the feature data
    data = {'data': input_text}
    
    try:
        # Send the POST request
        response = requests.post(url, json=data)
        
        # Get the predictions from the response
        predictions = response.json()['note']
        
        # Display the predictions
        st.write('Note:', predictions)
        
    except requests.exceptions.RequestException as e:
        # Display an error message if the request fails
        st.write('Error:', e)

# Create the Streamlit interface
st.title('API Interface')

# Create an input field for entering the string
input_field = st.text_area('Enter your string')

# Create a button to send the request
send_button = st.button('Send', on_click=send_request)

# Create a button to erase the prediction note
erase_button = st.button('Erase Prediction')

# Handle erase button click event
if erase_button:
    if 'predictions' in st.session_state:
        del st.session_state.predictions

# Start the Streamlit app
# st.set_page_config(layout='wide')
st.write('Please enter a string and click "Send" to get the predictions.')
