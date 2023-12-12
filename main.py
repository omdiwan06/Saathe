import streamlit as st

# HTML template for opening new tabs
html_template = """
<form action="{url}" target="_blank" method="get">
    <button type="submit" style="display: block; margin-bottom: 10px; padding: 8px 16px; background-color: #00000; color: white; border: none; border-radius: 4px; cursor: pointer;">{label}</button>
</form>
"""

# Streamlit app
st.subheader(':blue[Welcome to,]',' qSaarth-E')
st.title('Saarth-E Application Portal')
st.image('https://eservices.durg.gov.in/saarth-e/assests/assets/img/logo2.png', caption='Saarth-E', use_column_width=True)

# Open "Assign Department" in a new tab
if st.button('Grievance Form'):
    new_tab_assign_department = html_template.format(url="http://localhost:8502", label="Form")
    st.components.v1.html(new_tab_assign_department, height=50)

# Open "Prioritize" in a new tab
if st.button('Prioritize'):
    new_tab_prioritize = html_template.format(url="http://localhost:8503", label="Prioritize")
    st.components.v1.html(new_tab_prioritize, height=50)
