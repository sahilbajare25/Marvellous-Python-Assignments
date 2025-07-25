import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error

def AdvertisementAgency(Datapath):

    line = "-"*50
    df = pd.read_csv(Datapath)

    print(line)
    print("The data set contains:\n")
    print(df.head())
    print(df.shape)

    df.drop(columns=['Unnamed: 0'], axis= 1,inplace= True)

    print(line)
    print("After removing the unamed column the dataset contains\n")
    print(df.head())
    print(line)

    x = df.drop(columns='sales')
    y = df['sales']

    x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.5, random_state= 42)

    model = LinearRegression()

    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)

    r2 = r2_score(y_pred,y_test)

    print("Predicted values of algorithm are:\n")
    print(y_pred)
    print(line)

    print("Expected vales of the data set are :\n")
    print(y_test)
    print(line)

    print("R2 score is :",r2)
    print(line)

    mse = mean_squared_error(y_pred,y_test)

    print("MSE values is :",mse)
    print(line)

    rmse = np.sqrt(mse)

    print("RMSE value is :",rmse)
    print(line)

def main():

    AdvertisementAgency('Advertising.csv')

if __name__ == "__main__":
    main()