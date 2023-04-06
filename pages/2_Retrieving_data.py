import streamlit as st
import pandas as pd

@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

st.header("Money Send/paid and Received Data ")
st.checkbox("Show neatly", value=True, key="use_container_width")

df = pd.read_csv("Data.csv")
st.write()
hide_dataframe_row_index = """
            <style>
            .row_heading.level0 {display:none}
            .blank {display:none}
            </style>
            """

# Inject CSS with Markdown
st.markdown(hide_dataframe_row_index, unsafe_allow_html=True)

# Display the dataframe and allow the user to stretch the dataframe
# across the full width of the container, based on the checkbox value
st.dataframe(df, use_container_width=st.session_state.use_container_width)

csvdata = convert_df(df)
downloaded = st.download_button(
    label="Download data as CSV",
    data=csvdata,
    file_name='Data.csv.csv',
    mime='text/csv',
)
if downloaded:
    with st.sidebar:
        st.success("CSV file downloaded as 'Data.csv'")




st.header("Category Wise Distribution ")
# st.write(dff)


# Boolean to resize the dataframe, stored as a session state variable
st.checkbox("Show neatly", value=True, key="use_container_width_2nd")

dfd = pd.read_csv("MoneyData.csv")

# Display the dataframe and allow the user to stretch the dataframe
# across the full width of the container, based on the checkbox value
st.dataframe(dfd, use_container_width=st.session_state.use_container_width_2nd)
# st.bar_chart(dff)
csv = convert_df(dfd)
donwloaded_2 = st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='MoneyData.csv',
    mime='html/text',
)
if donwloaded_2:
    with st.sidebar:
        st.success("CSV file downloaded as 'MoneyData.csv'")
