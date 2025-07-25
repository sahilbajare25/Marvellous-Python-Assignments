import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns

def checkAccuracy(trainingData, testingData, trainingTarget, testingTarget):

    model = KNeighborsClassifier(n_neighbors=5)

    model.fit(trainingData,trainingTarget)

    y_pred = model.predict(testingData)

    Accuracy = accuracy_score(y_pred,testingTarget)

    return Accuracy

def PlayPredictor(Datapath):

    df = pd.read_csv(Datapath)

    print("Dataset contains:")
    print(df.head())
    print(df.shape)

    df.drop(columns=['Unnamed: 0'],axis=1,inplace= True)

    #Independent Dataset encoding
    df['Whether'] = df['Whether'].map({'Sunny': 0,'Overcast': 1,'Rainy': 2})
    df['Temperature'] = df['Temperature'].map({'Hot':3,'Mild': 4, 'Cool': 5})

    #Dependent Dataset encoding
    df['Play'] = df['Play'].map({'Yes': 8, 'No': 9 })

    print("After Encdoing the dataset contains ")
    print(df.head())

    x = df.drop(columns='Play')
    y = df['Play']

    x_train, x_test, y_train, y_test = train_test_split(x,y,test_size= 0.5, random_state= 42)

    Result = checkAccuracy(x_train, x_test, y_train, y_test)

    print("Accuracy of model is :",Result)

    '''plt.figure()
    target = 'Whether'
    sns.countplot(data=df,x=target, hue= 'Whether').set_title("wheaher details")
    plt.show()'''
    
def main():

    PlayPredictor("PlayPredictor.csv")

if __name__ == "__main__":
    main()