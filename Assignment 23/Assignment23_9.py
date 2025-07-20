import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def main():

    line = "-"*50

    data2 = {
       'Name' : ['Amit','Sagar','Pooja'],
       'Math' : [85,np.nan,78],
       'Science': [92,88,80],
       'English' : [75,np.nan,82]     
    }

    df = pd.DataFrame(data2)

    print(df)

    '''df['Math'].fillna(df['Math'].mean(), inplace= True)
    df['English'].fillna(df['English'].mean(), inplace= True)'''

    df.fillna(df.mean(numeric_only=True), inplace=True)

    print(df)
    

if __name__ == "__main__":
    main()