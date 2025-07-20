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
    
    #displaying details of stidents who score more than 85 in Science
    values = df[df['Science'] > 85]

    print("Students who score more than 85 in science")
    print(values)
        

if __name__ == "__main__":
    main()