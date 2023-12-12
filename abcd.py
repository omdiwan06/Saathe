import streamlit as st
import pandas as pd
import csv

# Define the app
def app():
    
    # st.subheader(':blue[Welcome to,]',' qSaarth-E')
    # st.title('Saarth-E Application Portal')
    # st.image('https://eservices.durg.gov.in/saarth-e/assests/assets/img/logo2.png', caption='Saarth-E', use_column_width=True)
    st.header('Grievance Registration Form')
    # Add input fields for person details
    first_name = st.text_input("First Name:", "")
    last_name = st.text_input("Last Name:", "")
    st.write("You entered:", first_name,last_name)
    father_name = st.text_input("Father Name:", "")
    mobile = st.text_input('Mobile number:')
    st.write("You entered:", mobile)
    avd_for = st.selectbox('Application for:',('Individual','Group','Other'))
    type = st.selectbox('Application type:',('Complaint','Request','Suggestion'))
    subject = st.text_input("Write your concern:","")
    
    if st.button('Save'):
        if first_name and last_name and mobile:
            # Assuming serial number starts from 1 and increments by 1 for each entry
            serial_number = sum(1 for line in open('details.csv')) + 1
            save_to_csv([serial_number, first_name, last_name, father_name, mobile, avd_for, type, subject])
            st.success('Details saved successfully!')
        else:
            st.warning('Please fill in all the details.')


def save_to_csv(data):
    with open('details.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)


def prioritize(file_name):
    with open(file_name, newline='') as csvfile:
    # Create a CSV reader object
        csv_reader = csv.reader(csvfile)
    
    # Read each row in the CSV file
    for row in csv_reader:
        # Process each row as needed
        print(row)
# Run the app
# to run the app code: "streamlit run app.py" in terminal
if __name__ == '__main__':
    app()
