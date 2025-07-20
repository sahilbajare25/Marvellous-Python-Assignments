import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

def main():

    data = {'marks':[45,67,88,32,76]}

    df = pd.DataFrame(data)

    print("Before")
    print(df)

    values = df['marks']

    for i in df['marks']:
        if i < 50:
            df['marks'].replace(i,'Fail',inplace= True)

    print('After')
    print(df)

if __name__ == "__main__":
    main()