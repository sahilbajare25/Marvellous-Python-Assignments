import pandas as pd
from sklearn.preprocessing import LabelEncoder 

def main():

    data = {'Department':['HR','IT','Finance','HR','IT']}

    df = pd.DataFrame(data)
    
    #one-hot encoding
    df['encoding'] = df['Department'].map({'HR' : 0, 'IT': 1, 'Finance' : 2})

    print(df)

if __name__ == "__main__":
    main()