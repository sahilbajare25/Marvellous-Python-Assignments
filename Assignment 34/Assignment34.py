import pandas as pd
from sklearn.datasets import load_breast_cancer 
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

import matplotlib.pyplot as plt
import seaborn as sns

def KNNModel(x_train, x_test, y_train, y_test):

    line = "-"*70

    model = KNeighborsClassifier(n_neighbors= 9)

    model.fit(x_train,y_train)

    y_pred = model.predict(x_test)

    Ans = accuracy_score(y_pred, y_test)

    conf_matrix = confusion_matrix(y_pred, y_test)

    print("Confusion matrix for the KNN Classifier model is :\n",conf_matrix)
    print(line)

    plt.figure(figsize=(8,6))
    sns.heatmap(conf_matrix, annot= True,fmt='d', linewidths= 1 ,cmap='coolwarm')
    plt.xlabel("Actual value")
    plt.ylabel("Predicted value")
    plt.title("Confusion Matrix of Descision Tree Classifier Model")
    plt.show()

    report = classification_report(y_pred, y_test)

    print("Classification report for the KNN Classifier model is :\n",report)

    return Ans 


def DecisionTree(x_train, x_test, y_train, y_test):

    line = "-"*70

    model = DecisionTreeClassifier()

    model.fit(x_train,y_train)

    y_pred = model.predict(x_test)

    Ans = accuracy_score(y_pred, y_test)

    conf_matrix = confusion_matrix(y_pred, y_test)

    print("Confusion matrix for the Decision Tree Classifier model is :\n",conf_matrix)
    print(line)

    plt.figure(figsize=(8,6))
    sns.heatmap(conf_matrix, annot= True,fmt='d', linecolor= 'black',cmap='RdBu')
    plt.xlabel("Actual value")
    plt.ylabel("Predicted value")
    plt.title("Confusion Matrix of KNN Classifier Model")
    plt.show()

    report = classification_report(y_pred, y_test)

    print("Classification report for the Decision Tree Classifier model is :\n",report)

    return Ans 

def main():

    line = "-"*70

    df = load_breast_cancer()

    x = df.data
    y = df.target

    df = pd.DataFrame(x,columns=df.feature_names)
    df['Target'] = y

    df.to_csv('load_breast_cancer.csv',index=False)

    print("The Stastitical data of the dataset is :")
    print(df.describe())
    print(line)

    print("Correlation of the feature are :")
    correlation = df.corr()

    #print(correlation)

    plt.figure(figsize=(6,4))
    sns.heatmap(correlation, annot= True, linecolor= 'black',cmap='coolwarm')
    plt.show()
    print(line)

    X = df.drop(columns='Target')
    Y = df['Target']

    scale = StandardScaler()

    x_scale = scale.fit_transform(X)

    x_train, x_test, y_train, y_test = train_test_split(x_scale, Y, test_size= 0.2, random_state= 42)

    Accuracy = DecisionTree(x_train, x_test, y_train, y_test)

    print(line)
    print(f"Accuracy of the Decision Tree Classifier model is : {Accuracy*100}")
    print(line)

    Accuracy = KNNModel(x_train, x_test, y_train, y_test)

    print(line)
    print(f"Accuracy of the KNN Classifier model is : {Accuracy*100}")
    print(line)

if __name__ == "__main__":
    main()