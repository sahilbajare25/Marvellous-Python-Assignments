import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

def main():

    data = {'Age':[18,22,25,30,35]}

    df = pd.DataFrame(data)

    scaler = MinMaxScaler()

    new_df = scaler.fit_transform(df)

    print(new_df)
    
if __name__ == "__main__":
    main()