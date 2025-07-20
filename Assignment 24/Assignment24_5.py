import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def main():

    line = "-"*50

    data = {
       'Name' : ['Amit','Sagar','Pooja'],
       'Math' : [85,90,78],
       'Science': [92,88,80],
       'English' : [75,85,82]     
    }

    df = pd.DataFrame(data)

    # it create encoding in the name column of dataframe
    #df['Name'] = df['Name'].map({'Amit': 'Male', 'Sagar' : 'Male','Pooja' : 'Female'})

    #It create new column with gender and encode name accordingly
    df['Gender'] = df['Name'].map({'Amit': 'Male', 'Sagar' : 'Male','Pooja' : 'Female'})

    df['Marks'] = df[['Math','Science','English']].sum(axis=1)

    df['Status'] = df['Marks'].apply(lambda x : 'Pass' if x >=250 else 'Fail')

    print(df)
    

if __name__ == "__main__":
    main()