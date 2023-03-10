# import libraries

import requests

from bs4 import BeautifulSoup
import csv

import pandas as pd

# base url which you want to scrap

base_url = 'https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India'

# Make a get request to server

r = requests.get(base_url)

# initialize the soup object

soup = BeautifulSoup(r.text, 'html.parser')

# define the HTML table and class

table = soup.find('table', class_='wikitable sortable')
# print(table)

# declare empty lists

list1 = []

list2 = []

list3 = []

# make a simple loop
q=table.find_all('tr')
#print(q)
w=len(q)
#print(len(q))
table_data = []
table_head = []
for i in range(1,w):
    #print(row)
    table_data.append(q[i].find_all('td'))

#print(table_data[27])
d = []
for i in range(w-1):
    z = len(table_data[i])
    if z == 6:
        for j in range(z):
            d.append(table_data[i][j].get_text())
print(d)
print(len(d))
d1=[]
x=0
for i in range(28):
    y= x+6
    d1.append(d[i:i+6])
    x=y

with open('jeva.csv', "w") as f:
    writer = csv.writer(f)
    #x = 0
    #for i in range(28):

        #y=x+6
    writer.writerows(d1)
        #x=y

# print(table_data[i][0].get_text())
#     # # to store second column data
# table_head.append(i.find_all('th'))
#     print(table_head[0][0].get_text())
# print(table_data[1])

    # only extract table body not heading

    # if len(table_data) == 6:
    #     list1.append(table_data[0].find(text=True))
    #     print("******************")
    #     print(table_data[0])
    #     print(table_head)
    #
    #     list2.append(table_head[0].find(text=True))
    #     print(table_head[0])
    #
    #     list3.append(table_data[1].find(text=True))
    #     print(table_data[1])
    #
    #     print("\n")
#print(table_data)
# df = pd.DataFrame(list1, columns=['Number'])
#
# df['States/UT'] = list2
#
# df['Capital'] = list3
#
# # copy data frame in to CSV file
#
# # csv file has been created in current working directory
#
# df.to_csv('India.csv')
#
# # read scraped data from CSV file
#
# read = pd.read_csv('/home/soft27/.config/spyder-py3/India.csv')
#
# print("Reading data from csv file")
#
# print(read)
