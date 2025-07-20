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

    df['Total'] = df[['Math','Science','English']].sum(axis=1)

    plt.bar(df['Name'],df['Total'])
    plt.xlabel("Student name")
    plt.ylabel("Student Marks")
    plt.title("Barplot")

    plt.show()

    '''Name = df['Name']
    Total = df["Total"]

    #print(Name," ",Total)
    fig, ax = plt.subplots()

    bar_colors = ['red','blue','orange']
    bar_labels = ['red','blue','orange']

    ax.bar(Name, Total, color = bar_colors, label = bar_labels)

    ax.set_title('Bar plot for Total Marks')
    ax.set_ylabel('Total marks')
    ax.legend(title = 'Students')

    plt.show()'''

if __name__ == "__main__":
    main()