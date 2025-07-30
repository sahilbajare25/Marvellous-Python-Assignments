import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score

def Logisticmodel(x_train, x_test, y_train, y_test):

    line = "-"*50
    print(line)

    model = LogisticRegression()

    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)

    np.savetxt('Assignment29_output_logistic.csv', y_pred, delimiter=',')

    print("Predicted data for Logistic regression model is :",y_pred)

    Ans = accuracy_score(y_pred, y_test)

    conf_matrix = confusion_matrix(y_pred, y_test)
    print("\n Confusion matrix for Logistic Regression is : \n",conf_matrix)

    precision = precision_score(y_pred, y_test)
    print("\n Precision score for Logistic Regression is : ",precision)

    recall = recall_score(y_pred, y_test)
    print("\n Recall score for the Logistic Regression is : ",recall)

    f1 = f1_score(y_pred, y_test)
    print("\n F1 score for the Logistic Regression is : ",f1)

    print(line)

    #visualization
    plt.figure(figsize=(10,8))
    sns.heatmap(conf_matrix, annot=True, cmap='coolwarm')
    plt.xlabel("Predicted value")
    plt.ylabel("True Value")
    plt.title("Confusion Matrix for Logistic Regression")
    #plt.show()

    return Ans

def KNNModel(x_train, x_test, y_train, y_test):

    line = "-"*50
    print(line)

    model = KNeighborsClassifier()

    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)

    np.savetxt('Assignment29_output_KNN.csv', y_pred, delimiter=',')

    Ans = accuracy_score(y_pred, y_test)

    conf_matrix = confusion_matrix(y_pred, y_test)
    print("\n Confusion matrix for KNN Classifier is : \n",conf_matrix)

    precision = precision_score(y_pred, y_test)
    print("\n Precision score for KNN Classifier is : ",precision)

    recall = recall_score(y_pred, y_test)
    print("\n Recall score for the KNN Classifer is : ",recall)

    f1 = f1_score(y_pred, y_test)
    print("\n F1 score for the KNN Classifier is : ",f1)

    #visualization
    plt.figure(figsize=(10,8))
    sns.heatmap(conf_matrix, annot=True, cmap='inferno')
    plt.xlabel("Predicted value")
    plt.ylabel("True Value")
    plt.title("Confusion Matrix for KNN Classifier")
    #plt.show()

    print(line)
    return Ans

def DecisionTreemodel(x_train, x_test, y_train, y_test):

    line = "-"*50
    print(line)

    model = KNeighborsClassifier(n_neighbors=3)

    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)

    np.savetxt('Assignment29_output_Decision_tree.csv', y_pred, delimiter=',')

    print("Predicted data for Decision Tree Classifier model is :",y_pred)

    Ans = accuracy_score(y_pred, y_test)

    conf_matrix = confusion_matrix(y_pred, y_test)
    print("\n Confusion matrix for Decision Tree classifier is : \n",conf_matrix)

    precision = precision_score(y_pred, y_test)
    print("\n Precision score for Decision Tree Classifier is : ",precision)

    recall = recall_score(y_pred, y_test)
    print("\n Recall score for the Decision Tree Classifier is : ",recall)

    f1 = f1_score(y_pred, y_test)
    print("\n F1 score for the Decision Tree Classifer is : ",f1)

    #visualization
    plt.figure(figsize=(10,8))
    sns.heatmap(conf_matrix, annot=True, cmap='RdBu')
    plt.xlabel("Predicted value")
    plt.ylabel("True Value")
    plt.title("Confusion Matrix for Decision Tree Classifier")
    plt.show()

    print(line)
    return Ans

def DiabetesPredictor(Datapath):

    df = pd.read_csv(Datapath)

    print("The Dataset contains:")
    print(df.head())
    print(df.shape)

    df_null = df[df.isnull() == True]

    print("The stastistic data of the data set is :\n",df.describe())
    
    values = df.drop(columns='Outcome')


    #Histogram
    plt.figure()
    plt.hist(values,bins=8)
    plt.title("Histogram")
    plt.xlabel('Values')
    plt.ylabel('Frequency')
    #plt.show()

    #Boxplot
    plt.figure()
    sns.boxplot(values)

    #pairplot
    sns.pairplot(values)
    #plt.show()

    x = df.drop(columns='Outcome')
    y = df['Outcome']

    scaler = StandardScaler()
    x_scale = scaler.fit_transform(x)

    x_train, x_test, y_train, y_test = train_test_split(x_scale,y, test_size= 0.2, random_state= 42)

    Accuracy = Logisticmodel(x_train, x_test, y_train, y_test)

    print("Accuracy of the Logisitic regression model : ",Accuracy*100)

    Accuracy = KNNModel(x_train, x_test, y_train, y_test)

    print("Accuracy of the KNN model : ",Accuracy*100)

    Accuracy = DecisionTreemodel(x_train, x_test, y_train, y_test)

    print("Accuracy of the Decision tree model : ",Accuracy*100)

def main():

    DiabetesPredictor('diabetes.csv')

if __name__ == "__main__":
    main()