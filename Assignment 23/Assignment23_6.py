import pandas as pd

def main():

    line = "-"*50

    data = {
       'Name' : ['Amit','Sagar','Pooja'],
       'Math' : [85,90,78],
       'Science': [92,88,80],
       'English' : [75,85,82]     
    }

    df = pd.DataFrame(data)

    df['Total'] = df[['Math','Science','English']].sum(axis=1)

    #we can save the chnages in original dataframe by usng inplace = True
    '''df.sort_values(by=['Total'], inplace= True)

    print(df)'''

    print("Data before soritng :")
    print(df)
    
    # Sorting dataframe on the base of Total marks
    New_df = df.sort_values(by=['Total'],ascending= False)

    print("Data after sorting")
    print(New_df)

if __name__ == "__main__":
    main()