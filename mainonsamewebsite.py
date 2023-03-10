import csv
from bs4 import BeautifulSoup
import string
import pandas as pd

with open('My Activity.html', 'r' , encoding='utf8') as html_file:
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
    tosend =[]
    # tosenss = []
    for tag in tags:
        sentence = tag.text
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
        txt = sentence.split("using")[0].replace("\n","").strip()
        # print(txt)
        # tosenss = sentence.split("using")[-1].replace("\n","").strip()
        # daa = tosenss.split()[2].split()

        if(conditions == 'Paid'):
            tosend.append(txt.split("to")[-1])
            paidlist.append(numm)
            print("Loading data...")
            # print(tosend)
        elif conditions == 'Sent':
            tosend.append("using "+sentence.split("using")[-1].replace("\n","").strip())
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
data = {"Money": money, "Category": paidSentrec , "Send To" : tosend}
data2 = {"Send" : sendlist , "Paid" : paidlist, "Recived" : reclist}
# print(len(money))
# print(len(paidSentrec))
# print(len(tosend))
df = pd.DataFrame(data)
dff = pd.DataFrame(data2)
# print(df)
df.to_csv("Data.csv" , index=False)
dff.to_csv("MoneyData.csv" , index=False)

print("Converted to csv")
