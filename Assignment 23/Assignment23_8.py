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

    marks = df[df['Name'] == 'Amit'][['Math','Science','English']].values.flatten()

    subjects = ['Math','Science','English']

    plt.plot(subjects,marks, marker = 'o')
    plt.xlabel('Subjects')
    plt.ylabel('Marks')
    plt.title('Amit report')
    plt.grid(True)

    plt.show()

    '''df['marks'] = df[['Math','Science','English']].values.tolist()

    value = df[df['Name'] == 'Amit']

    Name = value['Name']
    marks = value['marks']

    #print(Name,"\n",marks)

    plt.plot(marks)

    plt.show()'''

if __name__ == "__main__":
    main()