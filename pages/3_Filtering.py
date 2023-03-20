import streamlit as st
import seaborn as sbn
import matplotlib.pyplot as plt
import pandas as pd
# loading the dataset using the seaborn library
# import streamlit as st
import altair as alt
import time

st.title("Select your preference.")
multi =  st.checkbox('Multi-Select')
single =  st.checkbox('Single-Select')





# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# Single/Month-Wise
if single:
    with st.sidebar:
        st.success("You have selected Single wise datas")
    dataset = pd.read_csv('Data.csv')
    data = dataset.copy()
    # d = data.head()
    chart_data = pd.DataFrame(data)
    month_option  = ['Jan' , 'Feb', 'Mar','Apr','May','Jun','Jul','Aug','Sept','Oct','Nov','Dec']
    month = st.selectbox("Month", month_option, 0)
    df = chart_data[chart_data['Month'] == month]
    st.dataframe(df, use_container_width=1)
    print(data)

    # energy_source = pd.DataFrame({
    #     "EnergyType": ["Electricity", "Gasoline", "Natural Gas", "Electricity", "Gasoline", "Natural Gas",
    #                    "Electricity", "Gasoline", "Natural Gas"],
    #     "Price ($)": [150, 73, 15, 130, 80, 20, 170, 83, 20],
    #     "Date": ["2022-1-23", "2022-1-30", "2022-1-5", "2022-2-21", "2022-2-1", "2022-2-1", "2022-3-1", "2022-3-1",
    #              "2022-3-1"]
    # })
    if st.button("Create charts"):
        with st.spinner('Creating charts'):
            time.sleep(3)
        st.success('Created!')

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

    # st.write(count)
    # st.bar_chart(data=df['Category'])
    # sbn.displot(data['Month'])
    # plt.show()
    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    # Single/Year-wise

    # d = data.head()
    chart_data_for_year = pd.DataFrame(data)

    year_option  = ['2020,','2021,','2022,','2023,']
    year = st.selectbox("Year", year_option)
    df= chart_data[chart_data_for_year['Year'] == year]
    st.dataframe(df, use_container_width=1)
    cat = df['Category']

    # print(data)
    if st.button("Create charts",key="a"):
        with st.spinner('Creating charts'):
            time.sleep(5)
        st.success('Created!')

        tab1, tab2 = st.tabs(["📈 Category-Wise Chart", "📈 Month-Wise Chart"])
        with tab1:
            bar_chart = alt.Chart(df).mark_bar().encode(
                x='Year:O',
                y="sum(Money):Q",
                color="Category",
            )
            st.altair_chart(bar_chart, use_container_width=True)
        with tab2:
            bar_chart = alt.Chart(df).mark_bar().encode(
                x='Year:O',
                y="sum(Money):Q",
                color="Month"
            )
            st.altair_chart(bar_chart, use_container_width=True)
    # sbn.displot(data['Year'])
    # plt.show()

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
if multi:
    with st.sidebar:
        st.success("You have selected Multiple wise datas")
    dataset = pd.read_csv('Data.csv')
    data = dataset.copy()
    # d = data.head()
    chart_data_for_multi = pd.DataFrame(data)

    month_option_formulti  = ['Jan' , 'Feb', 'Mar','Apr','May','Jun','Jul','Aug','Sept','Oct','Nov','Dec']
    year_option_formulti  = ['2020,','2021,','2022,','2023,']
    year_formulti = st.selectbox("Year", year_option_formulti, 0)
    month_formulti = st.selectbox("Month", month_option_formulti, 0)
    df = chart_data_for_multi[chart_data_for_multi['Month'] == month_formulti]
    df = df[df['Year'] == year_formulti]
    st.dataframe(df, use_container_width=1)
    print(data)
    with st.spinner('Creating charts...'):
        time.sleep(5)
    st.success('Created!')

    # chart_data_for_year = pd.DataFrame(data)
    bar_chart = alt.Chart(df).mark_bar().encode(
        x='Year:O' and 'Month:O',
        y="sum(Money):Q",
        color="Category"
    )
    st.altair_chart(bar_chart, use_container_width=True)

    # df = chart_data[chart_data_for_year['Year'] == year]
    # st.write(df)

