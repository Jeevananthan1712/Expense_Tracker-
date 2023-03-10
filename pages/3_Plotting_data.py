# # import streamlit as st
# # import pandas as pd
# # import numpy as np
# #
# # chart_data = pd.DataFrame(
# #     np.random.randn(20, 3),
# #     columns=['a', 'b', 'c'])
# #
# # st.line_chart(chart_data)
#
#
# # import streamlit as st
# # import pandas as pd
# # import numpy as np
# # data = pd.read_csv("MoneyData.csv")
# # df = pd.DataFrame(data)
# #
# # # st.write(df.style.highlight_max(axis=0))
# # st.dataframe(df.style.background_gradient())
#
# import streamlit as st
# import pandas as pd
# import numpy as np
# df = pd.read_csv("MoneyData.csv")
# # x=[data.Send]
# # y=[data.Paid]
# # z=[data.Recived]
# dff = pd.DataFrame(df)
# d = dff.style.highlight_max()
# st.write(dff.style.highlight_max())
#
# # print(dff)
import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv("MoneyData.csv")
st.write(df.head(28))
chart_data = pd.DataFrame(df.head(28))
# import numpy
# print(numpy.__version__)
st.line_chart(chart_data)
st.bar_chart(chart_data)
st.area_chart(chart_data)
import streamlit as st
from bokeh.plotting import figure
df = pd.read_csv("Data.csv")
x = []
y = []
dff = pd.DataFrame(df)
x.append(dff.Money)
y.append(dff.Category)
st.write(x)

p = figure(
    title='simple line example',
    x_axis_label='x',
    y_axis_label='y')

p.line(x, y, legend_label='Trend', line_width=2)

st.bokeh_chart(p, use_container_width=True)