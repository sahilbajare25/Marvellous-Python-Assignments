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

    print("Actual Dataset is ")
    print(line)
    print(df)
    print(line)

    #shape
    print("Dataset contains:")
    print(df.shape)
    print(line)

    #columes
    print("Columns of Dataset is :")
    print(df.columns)
    print(line)

    #data types
    print("Data Types in Datasets are :")
    print(df.dtypes)
    print(line)

if __name__ == "__main__":
    main()