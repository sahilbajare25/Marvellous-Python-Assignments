import pandas as pd
from sklearn.preprocessing import LabelEncoder 
from sklearn.model_selection import train_test_split

def main():

    data = {'Grade' : ['A+','B','A','C','B+']}

    df = pd.DataFrame(data)

    print("Before replacing")
    print(df)
    print()

    df['Grade'].replace('A+','Excellent',inplace= True)
    df['Grade'].replace('A','Very Good',inplace= True)
    df['Grade'].replace('B+','Good',inplace= True)
    df['Grade'].replace('B','Average',inplace= True)
    df['Grade'].replace('C','Poor',inplace= True)

    print("After replacing")
    print(df)
    
if __name__ == "__main__":
    main()