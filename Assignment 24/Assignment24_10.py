import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import seaborn as sns

def main():

    line = "-"*50

    data = {
       'Name' : ['Amit','Sagar','Pooja'],
       'Math' : [85,90,78],
       'Science': [92,88,80],
       'English' : [75,85,82]     
    }

    df = pd.DataFrame(data)

    sns.boxplot(x='Name', y='English', data = df)

    plt.title("Boxplot for English marks")
    plt.show()

if __name__ == "__main__":
    main()