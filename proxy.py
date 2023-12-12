import streamlit as st
import pandas as pd

def main():
    st.title('PRIORITIZE')

    st.header('Orinigal Data')
    file_path1 = 'details.csv'
    data1 = pd.read_csv(file_path1)
    st.write(data1)

    st.header('Ordered Data')
    file_path2 = 'sorted_output.csv'
    data2 = pd.read_csv(file_path2)
    st.write(data2)

if __name__ == "__main__":
    main()
