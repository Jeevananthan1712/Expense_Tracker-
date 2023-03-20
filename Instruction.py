import streamlit as st
import pandas as pd
from io import StringIO
# st.snow()
import streamlit as st
import time

progress_text = "Loading Instruction. Please wait."
my_bar = st.progress(0, text=progress_text)

for percent_complete in range(100):
    time.sleep(0.1)
    my_bar.progress(percent_complete + 1, text=progress_text)
    

with st.sidebar:
    loaded = st.success("Loaded successfully")
    time.sleep(0.5)

if loaded:
    st.title("Experense Tarcko")
    st.caption("Steps to follow , if you want this to work!")
    st.subheader("Prerequisite")
    st.write("1. Click on https://takeout.google.com/")
    st.write("2. Select only the 'GPAY' data.")
    st.write("3. After selection the data will be downloaded")

    st.subheader("File Conversion")
    st.write("4. Now extract the files and upload it in the Data_Showing section ")
    st.write("5. Prerequisite  - fetch the file 'My Acticity.html' through the path - downloads/takeout(filename)/Google Pay/My Activity/My Activity.html \n And upload it int the Data_Showing section")
    st.write("6. After uploading , download the renamed file.")
    st.write("7. Wait for the Analysis to finish")
    st.write("8. Horrayy!! CSV file is generated ")

    st.title("Features")
    st.subheader("Data_Showing")
    st.write("9. Dataframes are displayed in the website")
    st.write("10. 2 types of dataframes are created ")
    st.write("-      1. Gendral Transcation History ")
    st.write("-      2. Category based transcation history")


    st.subheader("Downloading_data")
    st.write("11. Here you can basically download the csv files")
    st.write("12. Click the button to start the download")

    st.subheader("Filteration")
    st.write("13. Two types of filtering is available")
    st.write("-      1. Single select ")
    st.write("-      2. Multi select")
    st.write("14. If Single select is selected then inside it there are two types:")
    st.write("-      1. Month wise ")
    st.write("-      2. Year wise")
    st.write("15. Charts are prepared accordingly")
    st.write("16. If Multi select is selected then, you can select both month and year")




