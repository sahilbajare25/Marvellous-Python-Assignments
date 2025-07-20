import pandas as pd

def main():

    data = {'Name':['A','B','C'], 'Age':[21.0,22.0,23.0]}

    df = pd.DataFrame(data)

    Value = df['Age']

    new_df = df.astype({'Age': 'int32'}).dtypes

    print(new_df)

if __name__ == "__main__":
    main()