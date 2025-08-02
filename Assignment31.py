import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score ,confusion_matrix ,roc_auc_score

import matplotlib.pyplot as plt
import seaborn as sns

def Gradient(x_train ,x_test, y_train, y_test, x_set):

    line = "-"*70

    model = GradientBoostingClassifier(n_estimators=150, max_depth=10, learning_rate= 0.1)

    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)

    #Confusion Matrix
    conf_matrix = confusion_matrix(y_pred, y_test)

    print("Confusion matrix for the Gradient Bosting Classifier model is : \n", conf_matrix)
    print(line)

    #Data Visualization
    plt.figure(figsize=(8,6))
    sns.heatmap(conf_matrix, annot= True,fmt='d',linewidths=1 ,cmap='coolwarm')
    plt.xlabel("Predicted values")
    plt.ylabel("Actual Values")
    plt.title("Confusion Matrix of Gradient Bosting Classifier Model")
    plt.show()

    #ROC AUC Score
    y_prob = model.predict_proba(x_test)[:,1]

    roc = roc_auc_score(y_test, y_prob)

    print("ROC AUC Score for the Gradient Bosting Classifier model is :",roc*100)

    ans = accuracy_score(y_pred,y_test)

    importance = pd.Series(model.feature_importances_, index= x_set.columns)
    importance = importance.sort_values(ascending=False)

    importance.plot(kind="bar", figsize=(8,6), title="Feature Importance for Gradient Bosting Classifier Model")
    plt.show()

    return ans

def RandomForest(x_train ,x_test, y_train, y_test, x_set):
    
    line = "-"*70

    model = RandomForestClassifier(n_estimators=150, max_depth=10, random_state= 42)

    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)

    #Confusion Matrix
    conf_matrix = confusion_matrix(y_pred, y_test)

    print("Confusion matrix for the Random Forest model is : \n", conf_matrix)
    print(line)

    #Data Visualization
    plt.figure(figsize=(8,6))
    sns.heatmap(conf_matrix, annot= True,fmt='d',linewidths=1 ,cmap='coolwarm')
    plt.xlabel("Predicted values")
    plt.ylabel("Actual Values")
    plt.title("Confusion Matrix of Random Forest Model")
    plt.show()

    #ROC AUC Score
    y_prob = model.predict_proba(x_test)[:,1]

    roc = roc_auc_score(y_test, y_prob)

    print("ROC AUC Score for the Random Forest model is :",roc*100)

    ans = accuracy_score(y_pred,y_test)

    importance = pd.Series(model.feature_importances_, index= x_set.columns)
    importance = importance.sort_values(ascending=False)

    importance.plot(kind="bar", figsize=(8,6), title="Feature Importance for Random Forest Model")
    plt.show()

    return ans

def DecisionTree(x_train ,x_test, y_train, y_test, x_set):

    line = "-"*70

    model = DecisionTreeClassifier()

    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)

    #Confusion Matrix
    conf_matrix = confusion_matrix(y_pred, y_test)

    print("Confusion matrix for the Decision Tree model is : \n", conf_matrix)
    print(line)

    #Data Visualization
    plt.figure(figsize=(8,6))
    sns.heatmap(conf_matrix, annot= True,fmt='d',linecolor='black' ,cmap='RdBu')
    plt.xlabel("Predicted values")
    plt.ylabel("Actual Values")
    plt.title("Confusion Matrix for Descision Tree Model")
    plt.show()

    #ROC AUC Score
    y_prob = model.predict_proba(x_test)[:,1]

    roc = roc_auc_score(y_test, y_prob)

    print("ROC AUC Score for the Decision Tree model is :",roc*100)

    ans = accuracy_score(y_pred,y_test)

    importance = pd.Series(model.feature_importances_, index=x_set.columns)
    importance = importance.sort_values(ascending= False)

    importance.plot(kind="bar", figsize=(8,6), title="Feautre Importance for Decision Tree Model")
    plt.show()

    return ans

def breastCancer(Datapath):

    line = "-"*70

    df = pd.read_csv(Datapath)

    print("The Dataset contains:")
    print(df.head())
    print(df.shape)
    print(line)

    df.drop(df[df['BareNuclei'] == '?'].index, inplace= True)
    df.drop(columns='CodeNumber', inplace= True)

    print("After removing the unnecessary rows the dataset contains:")
    print(df.shape)
    print(line)

    x = df.drop(columns='CancerType')
    y = df['CancerType']

    x_train ,x_test, y_train, y_test = train_test_split(x,y,test_size=0.3, random_state= 42)

    Accuracy = DecisionTree(x_train ,x_test, y_train, y_test,x)

    print(line)
    print("Accuracy of Decision Tree Classifier model is :",Accuracy*100)
    print(line)
    print(line)

    Accuracy = RandomForest(x_train ,x_test, y_train, y_test, x)

    print(line)
    print("Accuracy of Random Forest Classifier model is :",Accuracy*100)
    print(line)

    Accuracy = Gradient(x_train ,x_test, y_train, y_test, x)

    print(line)
    print("Accuracy of Gradient Bossting Classifier model is :",Accuracy*100)
    print(line)

def main():

    breastCancer('breast-cancer-wisconsin.csv')

if __name__ == "__main__":
    main()