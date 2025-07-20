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
    
    #Sum of marks (axis = 1 : vartical sum, axis = 0 : Horizontal sum)
    #df['Total'] = df[['Math','Science','English']].sum(axis = 1)

    df['Total'] = df['Math'] + df['Science'] + df['English']

    print(df)
        

if __name__ == "__main__":
    main()