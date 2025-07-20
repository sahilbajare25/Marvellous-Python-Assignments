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

    value = df[['Math']]

    scaler = MinMaxScaler()

    scaler.fit(value)

    new_value = scaler.transform(value)
    
    print(new_value)

if __name__ == "__main__":
    main()