import streamlit as st
import pandas as pd
import numpy as np


df = pd.read_csv("MoneyData.csv")
st.write(df)
chart_data = pd.DataFrame(df.head(28))
st.line_chart(chart_data)
st.bar_chart(chart_data)
st.area_chart(chart_data)
