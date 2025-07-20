import pandas as pd
import matplotlib.pyplot as plt

def main():

    line = "-"*50

    data = {
       'Name' : ['Amit','Sagar','Pooja'],
       'Math' : [85,90,78],
       'Science': [92,88,80],
       'English' : [75,85,82]     
    }

    df = pd.DataFrame(data)

    Value = df[df['Name'] == 'Sagar'][['Math','Science','English']].values.flatten()
    subjects = ['Math','Science','English']

    plt.pie(Value,labels=subjects)
    plt.title('Sagars marks')

    plt.show()
    

if __name__ == "__main__":
    main()