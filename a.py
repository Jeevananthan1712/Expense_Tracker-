import seaborn as sbn
import matplotlib.pyplot as plt
import pandas as pd
# loading the dataset using the seaborn library
dataset = pd.read_csv('Data.csv')
data = dataset.copy()
# d = data.head()
d = data[data['Month']=='Mar']
print(d)
sbn.displot(d['Money'],kde=True,color='purple')
plt.show()
#
# import streamlit as st
# import seaborn as sbn
# import matplotlib.pyplot as plt
# import pandas as pd
# # loading the dataset using the seaborn library
# dataset = pd.read_csv('Data.csv')
# data = dataset.copy()
# # d = data.head()
# # chart_data = pd.DataFrame(data)
#
# month_option  = ['Jan' , 'Feb', 'Mar']
# # month = st.selectbox("Month", month_option, 2)
# df = data[data['Month'] == 'Mar']
# # st.write(df)
# print(df['Money'])
# sbn.barplot(x=df["Money"])
# plt.show()
