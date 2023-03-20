import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import streamlit as st
from csv import writer
import time

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

st.header("Inputs")
userIncome= st.number_input("Enter Income",False)
fam_size = st.slider("Family Size",0,20)
area = st.selectbox('Select a Area', ('Rural', 'Urban'), False)
expenses = st.slider('Enpenditure',100, 50000)
st.write('Your Income is:',userIncome)
st.write('Your family size is:',fam_size)
st.write('You selected:', area)
st.write('Expenditure:', expenses)


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
if userIncome and fam_size and area and expenses:
    if st.button('Submit'):
        progress_text = "Adding your data to csv.."
        my_bar = st.progress(0, text=progress_text)
        
        for percent_complete in range(100):
            time.sleep(0.1)
            my_bar.progress(percent_complete + 1, text=progress_text)
        # Import writer class from csv module

        # List that we want to add as a new row
        List = [userIncome, fam_size, area,expenses]

        # Open our existing CSV file in append mode
        # Create a file object for this file
        with open('expenditure_data.csv', 'a') as f_object:
            # Pass this file object to csv.writer()
            # and get a writer object
            writer_object = writer(f_object)

            # Pass the list as an argument into
            # the writerow()
            writer_object.writerow(List)

            # Close the file object
            f_object.close()

        dataset = pd.read_csv("expenditure_data.csv")
        data = dataset.copy()
        st.dataframe(data)
        labelencoder = LabelEncoder()
        dataset['Location'] = labelencoder.fit_transform(dataset['Location'])

        X = dataset[['Income', 'Family Size', 'Location']]
        y = dataset[['Expenditure']]

        X_transformer = MinMaxScaler((-1, 1))
        X_transformer = X_transformer.fit(X)

        y_transformer = MinMaxScaler((-1, 1))
        y_transformer = y_transformer.fit(y)

        X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.2, random_state=1)

        X_train_transform = X_transformer.transform(X_train)
        X_test_transform = X_transformer.transform(X_test)
        Y_train_transform = y_transformer.transform(Y_train)
        Y_test_transform = y_transformer.transform(Y_test)

        model = LinearRegression()

        model.fit(X_train_transform, Y_train_transform)

        predictions = model.predict(X_train_transform)

        actual_data = y_transformer.inverse_transform(Y_train_transform)
        predicted_data = y_transformer.inverse_transform(predictions)
        # st.write(predicted_data)
        fig = plt.figure()
        plt.plot(actual_data, label="Actual Price", color='green')
        plt.plot(predicted_data, label="Predicted Price", color='red')
        plt.title('Expense Tracker')
        plt.xlabel('Months')
        plt.ylabel('Price')
        st.pyplot(fig)


        pred = model.predict(X_test_transform)

        actual_data = y_transformer.inverse_transform(Y_test_transform)
        predicted_data = y_transformer.inverse_transform(pred)

        figg = plt.figure()
        plt.plot(actual_data, label="Actual Price", color='green')
        plt.plot(predicted_data, label="Predicted Price", color='red')
        plt.title('Expense Tracker')
        plt.xlabel('Months')
        plt.ylabel('Price')
        st.pyplot(figg)


        # y_pred = [500, 3, 1]
        li = [[userIncome , fam_size]]
        if List[2] == 'Rural':
            li[0].append(0)
        else:
            li[0].append(1)

        # st.write(li)
        y_trans = X_transformer.transform(li)

        y = model.predict(y_trans)

        y_new = y_transformer.inverse_transform(y)

        st.subheader("Expected expenditure for the given income: ")
        st.caption(y_new[0][0])

        # fig = plt.figure()
        # plt.plot(Y_train_transform, label="Actual Price", color='green')
        # plt.plot(predictions, label="Predicted Price", color='red')
        # plt.title('Expense Tracker')
        # plt.xlabel('days')
        # plt.ylabel('Price')
        # st.pyplot(fig)
        #
        # pred = model.predict(X_test_transform)
        #
        # print(pred)
        # figg = plt.figure()
        # plt.plot(Y_test_transform, label="Actual Price", color='green')
        # plt.plot(pred, label="Predicted Price", color='red')
        # plt.title('Expense Tracker')
        # plt.xlabel('days')
        # plt.ylabel('Price')
        # # plt.show()
        # st.pyplot(figg)

        # New Section