import streamlit, pandas, numpy, datetime, json, requests, pyodbc
from keras.api.models import Sequential
from keras.api.layers import Input, Dense, Dropout
from keras.api.callbacks import TensorBoard
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from matplotlib import pyplot

getdatachoices = [
        "select your option", "Upload CSV", "Upload Excel", "Add API", "Connect to SQL"
    ]
Options = streamlit.selectbox("Upload file options: ", getdatachoices)
# CSV

if Options == "select your option":
    streamlit.session_state["disable"] = True
    streamlit.warning("Select options above if your data is ready and if not visit preprocessing")
if Options == "Upload CSV":
    uploaded_file = streamlit.file_uploader("Upload a CSV file", type=["csv"])
    if "show_data" not in streamlit.session_state:
        streamlit.session_state.show_data = False
    if uploaded_file is not None:
        file_has_been_uploaded = pandas.read_csv(uploaded_file)
        streamlit.write("File uploaded successfully!")
    col1, col2 = streamlit.columns(2)
    with col1:
        if streamlit.button("View data"):
            streamlit.session_state.show_data = True
    with col2:
        if streamlit.button("Hide data"):
            streamlit.session_state.show_data = False
    if streamlit.session_state.show_data:        
        streamlit.write(file_has_been_uploaded.head())
# Excel

if Options == "Upload Excel":
    uploaded_file = streamlit.file_uploader("Upload an Excel file", type=["xlsx", "xls"])
    if "show_data" not in streamlit.session_state:
        streamlit.session_state.show_data = False
    if uploaded_file is not None:
        file_has_been_uploaded = pandas.read_excel(uploaded_file)
        streamlit.write("File uploaded successfully!")
    col1, col2 = streamlit.columns(2)
    with col1:
        if streamlit.button("View data"):
            streamlit.session_state.show_data = True
    with col2:
        if streamlit.button("Hide data"):
            streamlit.session_state.show_data = False
    if streamlit.session_state.show_data:        
        streamlit.write(file_has_been_uploaded.head())
# API
        
if Options == "Add API":
    url = streamlit.text_input("Enter your API URL:", "")
    if url == "":
        streamlit.write("")
    else:
        try:
            uploaded_file = pandas.DataFrame(requests.get(url).json())
            if "show_data" not in streamlit.session_state:
                streamlit.session_state.show_data = False
            elif uploaded_file is not None:
                file_has_been_uploaded = uploaded_file
                streamlit.write("Server response was successful!")
            col1, col2 = streamlit.columns(2)
            with col1:
                if streamlit.button("View data"):
                    streamlit.session_state.show_data = True
            with col2:
                if streamlit.button("Hide data"):
                    streamlit.session_state.show_data = False
            if streamlit.session_state.show_data:
                streamlit.write(file_has_been_uploaded.head())
        except requests.exceptions.RequestException as e:
            streamlit.write("Server response failed!")
            if "show_error" not in streamlit.session_state:
                streamlit.session_state.show_error = False
            col_left, col_right = streamlit.columns(2)
            with col_left:
                if streamlit.button("See what was the error"):
                    streamlit.session_state.show_error = True
            with col_right:
                if streamlit.button("You can hide the error"):
                    streamlit.session_state.show_error = False
            if streamlit.session_state.show_error:
                streamlit.write(f"Error fetching data: {e}")
# SQL

if Options == "Connect to SQL":
    Driver_Options = ["", "", "Other"]
    Driver = streamlit.text_input("Enter your Driver:", "")
    Server = streamlit.text_input("Enter your Server:", "")
    Database = streamlit.text_input("Enter your Database:", "")
    UserID = streamlit.text_input("Enter your UserID:", "")
    Password = streamlit.text_input("Enter your Password:", type="password")
    
    if not all ([Driver, Server, Database, UserID, Password]):
        streamlit.warning("Please fill in all fields")
    else:
        try:
            conn = pyodbc.connect(f"Driver={Driver};Server={Server};Database={Database};UID={UserID};PWD={Password};TrustServerCertificate=yes")
            streamlit.success("Server response was successful!")
            if "show_data" not in streamlit.session_state:
                streamlit.session_state.show_data = False
            elif uploaded_file is not None:
                file_has_been_uploaded = uploaded_file
                streamlit.write("Server response was successful!")
            col1, col2 = streamlit.columns(2)
            with col1:
                if streamlit.button("View data"):
                    streamlit.session_state.show_data = True
            with col2:
                if streamlit.button("Hide data"):
                    streamlit.session_state.show_data = False
            if streamlit.session_state.show_data:
                streamlit.write(file_has_been_uploaded.head())
        except requests.exceptions.RequestException as e:
            streamlit.write("Server response failed!")
            if "show_error" not in streamlit.session_state:
                streamlit.session_state.show_error = False
            col_left, col_right = streamlit.columns(2)
            with col_left:
                if streamlit.button("See what was the error"):
                    streamlit.session_state.show_error = True
            with col_right:
                if streamlit.button("You can hide the error"):
                    streamlit.session_state.show_error = False
            if streamlit.session_state.show_error:
                streamlit.write(f"Error fetching data: {e}")
                

# http://127.0.0.1:8000/items_processed