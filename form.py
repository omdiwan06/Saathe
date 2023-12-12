import streamlit as st
import pandas as pd
import json
import os
import pickle
import csv
count=0
# Load the pre-trained machine learning model
# ml = pickle.load(open('LinearRegressionModel.pkl','rb')) #LinearRegressionModel.pkl
# Function to save data to JSON file
def save_to_json(data):
    file_name = 'user_details.json'

    # If the file doesn't exist, create a new one
    if not os.path.exists(file_name):
        with open(file_name, 'w') as file:
            json.dump([], file)
        
    with open(file_name, 'r+') as file:
        # Load existing data
        details = json.load(file)
        
        # Append new data
        details.append(data)
    
        # Reset file pointer to the beginning and write the updated data
        file.seek(0)
        json.dump(details, file, indent=4)
# Define the app
def app():
    # Set the app title
    global count
    count = 1
    st.subheader(':blue[Welcome to,]',' qSaarth-E')
    st.title('Saarth-E')
    
    # Add some instructions
    
    # Add input fields for person details
    # make = st.text_input('Company of car')
    first_name = st.text_input("First Name:", "")
    last_name = st.text_input("Last Name:", "")
    st.write("You entered:", first_name,last_name)
    father_name = st.text_input("Father Name:", "")
    mobile = st.text_input('Mobile number')
    st.write("You entered:", mobile)
    avd_for = st.selectbox('application_for',('Individual','Group','Other'))
    type = st.selectbox('application_type',('Advice','Complaint','Request'))
    subject = st.text_input("Write your concern","")
    
    if st.button('Save'):
        # Create a dictionary with user inputs
        user_data = {
            "serial" : ret_serial_number()+1,
            "first_name" : first_name,
            "last_name" : last_name,
            "father_name" : father_name,
            "mobile" : mobile,
            "avd_for" : avd_for,
            "type" : type,
            "subject" : subject
        }
        # Save data to JSON file
        save_to_json(user_data)
        st.success('Details saved successfully!')
        count = count + 1

    csv_file_path = 'input.csv'  # Replace 'your_file.csv' with your CSV file path
    new_values = [first_name, last_name, father_name, mobile, avd_for, type, subject]  # Replace with the values you want to insert
    insert_values_into_csv(csv_file_path, new_values)

    
def ret_serial_number():
    file_name = 'user_details.json'
    with open (file_name, 'r') as file:
        details = json.load(file)
        

        if details != []:
            last_user = details[-1]
            last_serial_number = int(last_user.get("serial"))
            return last_serial_number
        else:
            return 0    


# Function to insert values into a CSV file
def insert_values_into_csv(csv_file, values):
    with open(csv_file, 'a', newline='') as file:
        csv_writer = csv.writer(file)
        
        # Write the values to the CSV file
        csv_writer.writerow(values)

# Example usage



# Run the app
# to run the app code: "streamlit run app.py" in terminal
if __name__ == '__main__':
    app()
