import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_auc_score

import matplotlib.pyplot as plt
import seaborn as sns

def Logisticmodel(x_train, x_test, y_train, y_test):

    print("\n--------------------------Logistic Regression Model-----------------------------\n")

    line = "-"*80

    model = LogisticRegression()

    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)

    #Confusion matrix
    config_matrix = confusion_matrix(y_pred, y_test)
    #np.set_printoptions(suppress=True)

    print("Confusion Matrix for Logistic Model is : \n",config_matrix,"\n")

    #Data Visualisation
    plt.figure(figsize=(10,6))
    sns.heatmap(config_matrix,fmt='d',annot= True, cmap='coolwarm', linewidths=1)
    plt.xlabel("Predicted value")
    plt.ylabel("True Value")
    plt.title("Confusion Matrix for Logistic Regression")
    plt.show()

    #Classification Report
    report = classification_report(y_pred, y_test)

    print("Classification report for Logisitc regression model is :\n",report)

    #ROC-AUC Score
    y_prob = model.predict_proba(x_test)[:,1]

    roc = roc_auc_score(y_test, y_prob)

    print(line)
    print("The ROC AUC Score for the Logistic regression model is :",roc*100)

    res = accuracy_score(y_pred, y_test)

    print(line)

    return res

def KNNModel(x_train, x_test, y_train, y_test):
    
    print("\n--------------------------KNN classifier model----------------------------------\n")

    line = "-"*80

    model = KNeighborsClassifier()

    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)

    #Confusion matrix
    config_matrix = confusion_matrix(y_pred, y_test)

    print("Confusion Matrix for KNN classifier model is : \n",config_matrix,"\n")

    #Data Visualisation
    plt.figure(figsize=(10,6))
    sns.heatmap(config_matrix,fmt='d',annot= True, cmap='BrBG',linewidths=1,linecolor='black')
    plt.xlabel("Predicted value")
    plt.ylabel("True Value")
    plt.title("Confusion Matrix for Logistic Regression")
    plt.show()

    #Classification Report
    report = classification_report(y_pred, y_test)

    print("Classification report for KNN Classifier model is :\n",report)

    #ROC-AUC Score
    y_prob = model.predict_proba(x_test)[:,1]

    roc = roc_auc_score(y_test, y_prob)

    print(line)
    print("The ROC AUC Score for the KNN Classifier model is :",roc*100)

    res = accuracy_score(y_pred, y_test)

    print(line)

    return res

def RandomForest(x_train, x_test, y_train, y_test):

    print("\n--------------------------Random Forest Classifier model------------------------\n")

    line = "-"*80

    model = RandomForestClassifier(n_estimators=150, max_depth= 10, random_state= 42)

    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)

    #Confusion matrix
    config_matrix = confusion_matrix(y_pred, y_test)

    print("Confusion Matrix for Random Forest Classifier model is : \n",config_matrix,"\n")

    #Data Visualisation
    plt.figure(figsize=(10,6))
    sns.heatmap(config_matrix,fmt='d',annot= True, cmap='RdBu',linewidths=1,linecolor='black')
    plt.xlabel("Predicted value")
    plt.ylabel("True Value")
    plt.title("Confusion Matrix for Logistic Regression")
    plt.show()

    #Classification Report
    report = classification_report(y_pred, y_test)

    print("Classification report for Random forest classifier model is :\n",report)

    #ROC-AUC Score
    y_prob = model.predict_proba(x_test)[:,1]

    roc = roc_auc_score(y_test, y_prob)

    print(line)
    print("The ROC AUC Score for the Random Forest Classifier model is :",roc*100)

    res = accuracy_score(y_pred, y_test)

    print(line)

    return res

def BankingData(Datapath):

    line = "-"*80

    df = pd.read_csv(Datapath, delimiter=';')

    df.to_csv("Newfile.csv", index=False)

    df = pd.read_csv("Newfile.csv")

    print("The dataset contains :")
    print(df.shape)
    print(line)

    df.drop(columns=['contact','poutcome'],inplace=True)

    df.drop(df[df['job'] == 'unknown'].index, inplace= True)
    df.drop(df[df['education'] == 'unknown'].index, inplace= True)

    print("After removal of unnecessary columns statistics of the dataset is :")
    print(df.describe())
    print(line)
    
    for col in df.select_dtypes(include='object'):
        df[col] = LabelEncoder().fit_transform(df[col])

    x = df.drop(columns='y')
    y = df['y']

    scaler = StandardScaler()

    x_scale = scaler.fit_transform(x)

    x_train, x_test, y_train, y_test = train_test_split(x_scale,y, test_size=0.2 , random_state= 42)

    Accuracy = Logisticmodel(x_train, x_test, y_train, y_test)    

    print("Accuracy of Logistic Regression model is : ",Accuracy*100)
    print(line)
    print(line)

    Accuracy = KNNModel(x_train, x_test, y_train, y_test)

    print("Accuracy of KNN Classifier model is : ",Accuracy*100)
    print(line)
    print(line)

    Accuracy = RandomForest(x_train, x_test, y_train, y_test)

    print("Accuracy of Random Forest Classifier model is : ",Accuracy*100)    
    print(line)
    print(line)

def main():

    BankingData("bank-full.csv")

if __name__ == "__main__":
    main()