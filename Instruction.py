import streamlit as st
import pandas as pd
from io import StringIO
# st.snow()
import streamlit as st
import time

progress_text = "Loading Instruction. Please wait."
my_bar = st.progress(0, text=progress_text)

for percent_complete in range(100):
    time.sleep(0.01)
    my_bar.progress(percent_complete + 1, text=progress_text)
    

with st.sidebar:
    loaded = st.success("Loaded successfully")
    time.sleep(0.5)

if loaded:
    st.title("SpendSync")
    st.caption("Steps to follow , if you want this to work!")
    st.subheader("Prerequisite")
    st.write("1. Click on https://takeout.google.com/")
    st.caption(" - or for demo purpose you can use my data by clicking here.")
    st.write("2. Select only the 'GPAY' data.")
    st.write("3. After selection the data will be downloaded")

    st.subheader("File Conversion")
    st.write("4. Now extract the files and upload it in the Data_Showing section ")
    st.write("5. Prerequisite  - fetch the file 'My Acticity.html' through the path - downloads/takeout(filename)/Google Pay/My Activity/My Activity.html \n And upload it int the Data_Showing section")
    st.write("6. After uploading , download the renamed file.")
    st.write("7. Wait for the Analysis to finish")
    st.write("8. Horrayy!! CSV file is generated ")

    st.title("Features")
    st.subheader("Data Showing")
    st.write("9. Dataframes are displayed in the website")
    st.write("10. 2 types of dataframes are created ")
    st.write("-       Gendral Transcation History ")
    st.write("-       Category based transcation history")


    st.subheader("Retrieving data")
    st.write("11. Here you can basically download the csv files")
    st.write("12. Click the button to start the download")

    st.subheader("Screening")
    st.write("13. Two types of filtering is available")
    st.write("-      Single select ")
    st.write("-      Multi select")
    st.write("14. If Single select is selected then inside it there are two types:")
    st.write("-       📈Month wise ")
    st.write("-       📈Year wise")
    st.write("15. Charts are prepared accordingly")
    st.write("16. If Multi select is selected then, you can select both month and year")

    st.subheader("Comparing_Months")
    st.write("17. Here you have to select the Months in multiple-Select mode")
    st.write("18. After selecting you will get charts in 2 ways")
    st.write("-       📈Category wise ")
    st.write("-       📈Year wise")

    st.subheader("Expenditure Estimation")
    st.write("19. User's should give inputs")
    st.write("20. Expenditure will be estimated and displayed")

