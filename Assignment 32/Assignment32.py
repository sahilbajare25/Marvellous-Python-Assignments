import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

import matplotlib.pyplot as plt
import seaborn as sns

def VotingClass(x_train, x_test, y_train, y_test):

    line = "-"*70

    log_clf = LogisticRegression()
    dt_clf = DecisionTreeClassifier(max_depth=8)
    knn_clf = KNeighborsClassifier(n_neighbors=5)

    '''vot_clf = VotingClassifier(
        estimators=[('lr',log_clf),('dt', dt_clf),('knn',knn_clf)], 
        voting = 'hard')'''
    
    vot_clf = VotingClassifier(
        estimators=[
            ('lr', log_clf),
            ('dt',dt_clf),
            ('knn',knn_clf)
        ],
        voting='hard'
    )

    vot_clf.fit(x_train, y_train)
    y_pred = vot_clf.predict(x_test)

    Ans_Hard = accuracy_score(y_pred, y_test)

    vot_clf = VotingClassifier(
        estimators=[
            ('lr', log_clf),
            ('dt',dt_clf),
            ('knn',knn_clf)
        ],
        voting='hard'
    )

    vot_clf.fit(x_train, y_train)
    y_pred = vot_clf.predict(x_test)

    Ans_Soft = accuracy_score(y_pred, y_test)

    return Ans_Hard, Ans_Soft

def LogisitcModel(x_train, x_test, y_train, y_test):

    line = "-"*70

    model = LogisticRegression()

    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)

    Ans = accuracy_score(y_pred, y_test)

    #confusion Matrix
    conf_matrix = confusion_matrix(y_pred, y_test)

    print("Confusion matrix of Logistic Regression model is :\n",conf_matrix)
    print(line)

    #Visualization
    plt.figure(figsize=(8,6))
    sns.heatmap(conf_matrix, annot= True,fmt='d',cmap='RdBu')
    plt.xlabel("predicted Values")
    plt.ylabel("Actual Values")
    plt.title("Hearmap of confusion matrix of logistic regression model")
    plt.show()

    return Ans

def DecisionTreeModel(x_train, x_test, y_train, y_test):

    line = "-"*70

    model = DecisionTreeClassifier()

    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)

    Ans = accuracy_score(y_pred, y_test)

    #confusion Matrix
    conf_matrix = confusion_matrix(y_pred, y_test)

    print("Confusion matrix of Descision Tree Classifier model is :\n",conf_matrix)
    print(line)

    #Visualization
    plt.figure(figsize=(8,6))
    sns.heatmap(conf_matrix, annot= True,fmt='d',linewidths=1,cmap='coolwarm')
    plt.xlabel("predicted Values")
    plt.ylabel("Actual Values")
    plt.title("Hearmap of confusion matrix of Decision Tree Classifier model")
    plt.show()

    return Ans

def News(Datapath1, Datapath2):

    line = "-"*70

    df_true = pd.read_csv(Datapath1)
    df_false = pd.read_csv(Datapath2)

    df_true['Label'] = 1
    df_false['Label'] = 0

    print("After adding label dataset contains :")
    print(df_true.shape)
    print(df_false.shape)

    print(line)

    data = pd.concat([df_false, df_true]).reset_index(drop=True)

    data.to_csv('News.csv',sep=';',index=False)

    print("The dataset in the concatenated file is :")
    print(data.shape)
    print(line)

    ''''
    data['date'] = pd.to_datetime(data['date'], errors='coerce')

    count = (data['date'] == 'NaT').sum()
    print(count)

    data.dropna(subset=['date'], inplace= True)

    #data.drop((data['date'] == 'NaT').index, inplace= True)

    print(data.shape)'''

    #x = data.drop(columns=['Label'])
    x = data['text']
    y = data['Label']

    #TF IDF Vectorization
    vector = TfidfVectorizer()
    x_trans = vector.fit_transform(x)
    
    #x_array = x_trans.toarray()
    #print("X_trans contains:\n",x_trans.shape)
    #features = vector.get_feature_names_out()
    #df = pd.DataFrame(x_array, columns=features)

    x_train, x_test, y_train, y_test = train_test_split(x_trans, y, test_size= 0.2, random_state= 42)

    Accuracy = LogisitcModel(x_train, x_test, y_train, y_test)

    print("Accuracy of Logistic Regression model is :", Accuracy*100)
    print(line)
    print(line)

    Accuracy = DecisionTreeModel(x_train, x_test, y_train, y_test)

    print("Accuracy of Decision Tree Classifier model is :", Accuracy*100)
    print(line)
    print(line)

    Accuracy_hard, Accuracy_soft = VotingClass(x_train, x_test, y_train, y_test)
    
    print("Accuracy of Voting Classifer model hard is :", Accuracy_hard*100)
    print("Accuracy of Voting Classifer model soft is :", Accuracy_soft*100)
    print(line)
    print(line)

def main():

    News("Fake.csv","True.csv")

if __name__ == "__main__":
    main()