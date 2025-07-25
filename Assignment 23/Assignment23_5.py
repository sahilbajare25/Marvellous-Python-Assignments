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
    
    # replacing pooja with puja  
    #New = df.replace({'Name':'Pooja'},'puja')

    df['Name'] = df['Name'].replace('Pooja','Puja')

    print(df)

if __name__ == "__main__":
    main()