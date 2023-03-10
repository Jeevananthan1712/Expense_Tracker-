import streamlit as st
import pandas as pd
from io import StringIO
import csv
from bs4 import BeautifulSoup
import string
import glob
import os.path
import time
import streamlit as st


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df



st.title('Upload File here')
st.caption('Make sure it' + "'" + 's a HTML-file.')
uploaded_file = st.file_uploader("Choose a file", type='html')
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    # st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    # st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    # st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    # dataframe = pd.read_html(uploaded_file)
    # st.write(dataframe)
    html = convert_df(string_data)
    downloaded = st.download_button(
        label="Download file",
        data=html,
        file_name='MyDataHTMLFile.html',
        mime='html/text',
    )

    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

    if downloaded:
        path = r'C:\Users\JEEVA\Downloads\MyDataHTMLFile.html'
        # st.write(path)
        with st.spinner('Analysing your html file...'):
            time.sleep(5)
        with st.spinner('Correcting things...'):
            time.sleep(5)
        with st.spinner('Almost completed..'):
            time.sleep(5)
        with st.spinner('Hoorayy!!'):
            time.sleep(5)
            st.balloons()
        st.success('Converted to CSV file!')
        # folder_path = r'C:\"Users\JEEVA\Downloads'
        # file_type = r''
        # files = glob.glob(folder_path + file_type)
        # st.write(files)
        # max_file = max(files, key=os.path.getctime)

        # print(max_file)
        with open(r'C:\Users\JEEVA\Downloads\MyDataHTMLFile.html', 'r', encoding='Utf8') as html_file:
            print("Asccessing HTML file")
            content = html_file.read()
            soup = BeautifulSoup(content, 'lxml')
            tags = soup.find_all('div', class_='content-cell mdl-cell mdl-cell--6-col mdl-typography--body-1')
            # print(tags)

            # ***************************************************************************************************************
            paidlist = []
            reclist = []
            sendlist = []
            mainpartpaidlist = []
            mainpartsendlist = []
            mainpartreclist = []
            money = []
            paidSentrec = []
            tosend = []
            print("Lists created")

            # tosenss = []
            for tag in tags:
                sentence = tag.text
                print("Sentence accessed")
                # date = tag
                # print(date)
                # print(sentence)
                # if(sentence.startswith('U')):
                # sentence = sentence.replace(sentence ," ")
                # print(sentence)
                # print(sentence)
                mainpart = sentence.split("using")[0]
                # print(mainpart)
                num = tag.text.split(" ")[1].replace('â‚¹', ' ')
                numm = num.split(".")[0]
                conditions = tag.text.split()[0]
                money.append(numm)
                paidSentrec.append(conditions)
                txt = sentence.split("using")[0].replace("\n", "").strip()
                # print(txt)
                # tosenss = sentence.split("using")[-1].replace("\n","").strip()
                # daa = tosenss.split()[2].split()

                if (conditions == 'Paid'):
                    tosend.append(txt.split("to")[-1])
                    paidlist.append(numm)
                    print("Loading data...")
                    # print(tosend)
                elif conditions == 'Sent':
                    tosend.append("using " + sentence.split("using")[-1].replace("\n", "").strip())
                    sendlist.append(numm)

                    # print(sentence.split("using")[-1].replace("\n",""))
                else:
                    tosend.append("Received to this Account")
                    reclist.append(numm)

            # if conditions == 'Paid':
            #     mainpartpaidlist.append(mainpart)
            # elif conditions == 'Sent':
            #     mainpartsendlist.append(mainpart)
            # else:
        # print(tosenss)
        # print(daa)
        # print(tosend)
        # print(mainpartreclist)
        # print(pd.Series(tosend))
        # print(pd.Series(money))
        # print(pd.Series(paidSentrec))
        # ********************************************************************************************************************
        paidlistlen = len(paidlist)
        reclistlen = len(reclist)
        sendlistlen = len(sendlist)

        if reclistlen < paidlistlen and paidlistlen > sendlistlen:
            print("Adjusting Data")
            for i in range(reclistlen, paidlistlen):
                reclist.append(0)
                mainpartreclist.append(0)
            for i in range(sendlistlen, paidlistlen):
                sendlist.append(0)
                mainpartsendlist.append(0)

        if reclistlen > paidlistlen and reclistlen > sendlistlen:
            for i in range(paidlistlen, reclistlen):
                paidlist.append(0)
                mainpartpaidlist.append(0)
            for i in range(sendlistlen, reclistlen):
                sendlist.append(0)
                mainpartsendlist.append(0)

        if sendlistlen > paidlistlen and sendlistlen > reclistlen:
            for i in range(paidlistlen, sendlistlen):
                paidlist.append(0)
                mainpartpaidlist.append(0)
            for i in range(reclistlen, sendlistlen):
                reclist.append(0)
                mainpartreclist.append(0)
        # *********************************************************************************************************
        # print(pd.Series(paidlist))
        # print("*************************************")
        # print(pd.Series(sendlist))
        # print("*************************************")
        # print(pd.Series(reclist))
        # print("*************************************")
        # ***********************************************************************************************************
        data = {"Money": money, "Category": paidSentrec, "Send To": tosend}
        data2 = {"Send": sendlist, "Paid": paidlist, "Recived": reclist}
        # print(len(money))
        # print(len(paidSentrec))
        # print(len(tosend))
        df = pd.DataFrame(data)
        dff = pd.DataFrame(data2)
        # print(df)
        df.to_csv("Data.csv", index=False)
        print(df.style.highlight_max())
        dff.to_csv("MoneyData.csv", index=False)

        print("Converted to csv")

        # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        st.header("Money Send/paid and Received Data ")
        df = pd.read_csv("Data.csv")
        dff = pd.read_csv("MoneyData.csv")
        # st.line_chart(df)
        st.write(df)

        st.header("Category Wise Distribution ")
        st.write(dff)

        import pandas as pd
        import streamlit as st


        # Cache the dataframe so it's only loaded once




# st.bar_chart(dff)
