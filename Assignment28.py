import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns

def WinePredictor(Datapath):

    df = pd.read_csv(Datapath)

    print("The data set contains:")
    print(df.head())
    print(df.shape)

    x = df.drop(columns='Class')
    #x = df[['Alcalinity of ash','Malic acid','Color intensity']]
    #x = df.drop(columns=['Class','Proline'])
    y = df['Class']

    x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state= 42)

    model = LogisticRegression()

    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)

    Accuracy = accuracy_score(y_pred,y_test)

    print("Accuracy score is :",Accuracy*100)

    #Data Visualisation
    plt.figure(figsize=(10,8))
    sns.heatmap(df.corr(), annot=True, cmap= 'RdBu')
    plt.title("Heatmap of Wine Predictor")
    plt.show()

def main():

    WinePredictor('WinePredictor.csv')

if __name__ == "__main__":
    main()