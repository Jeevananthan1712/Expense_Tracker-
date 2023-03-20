import streamlit as st
import pandas as pd
import altair as alt

options = st.multiselect(
    'Select Months',
    ['Jan' , 'Feb', 'Mar','Apr','May','Jun','Jul','Aug','Sept','Oct','Nov','Dec'])

if options:
    with st.sidebar:
        st.write("You have selected : " ,len(options) , " months")
    dataset = pd.read_csv('Data.csv')
    data = dataset.copy()
    # d = data.head()
    chart_data = pd.DataFrame(data)
    df = chart_data[chart_data['Month'].isin(options)]
    st.dataframe(df, use_container_width=1)
    tab1, tab2 = st.tabs(["📈 Category-Wise Chart", "📈 Year-Wise Chart"])
    with tab1:
        bar_chart = alt.Chart(df).mark_bar().encode(
            x='Month:O',
            y="sum(Money):Q",
            color="Category"
        )
        st.altair_chart(bar_chart, use_container_width=True)
    with tab2:
        bar_chart = alt.Chart(df).mark_bar().encode(
            x='Month:O',
            y="sum(Money):Q",
            color="Year"
        )
        st.altair_chart(bar_chart, use_container_width=True)
