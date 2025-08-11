############################################################################################
#Required libraries

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt

from sklearn.metrics import (accuracy_score,
                            classification_report,
                            confusion_matrix)
import joblib

##############################################################################################

INPUT_DATA = 'mall_customers_full.csv'
MODEL_PATH = 'mc_rf_pipeline.joblib'

HEADERS = ['CustomerID','Gender','Age','Annual Income (k$)','Spending Score (1-100)']

################################################################################################
#Function Name : get_data
#Input : Nothing
#Task : To Read the data from Input Data
#Output : return the store while reading from Input Data
################################################################################################

def get_data():

    data = pd.read_csv(INPUT_DATA)
    return data

################################################################################################
#Function Name : check_stat
#Input : dataset
#Task : To display Statistical Details from dataset
#Output : Nothing
################################################################################################

def check_stat(data):

    print(data.describe)
    print("\nStats Successfully Displayed")

################################################################################################
#Function Name : display
#Input : dataset
#Task : To display dataset after making some changes in dataset
#Output : Nothing
################################################################################################

def display(data):

    print(data.head())
    print("\nDataset successfully Displayed")

################################################################################################
#Function Name : Encode
#Input : dataset
#Task : To Encode the data so that dataset can be trained
#Output : Encoded dataset
################################################################################################

def Encode(data):

    data['Gender'] = data['Gender'].map({'Male' : 0, 'Female' : 1})
    return data
################################################################################################
#Function Name : split
#Input : dataset with required details to split the dataset
#Task : To split the dataset into trainig and testing sets
#Output : Training and Testing datasets
################################################################################################

def split(Data,splitting_parcentage,Data_headers,Data_targets,random_state = 42):

    x_train, x_test,y_train, y_test = train_test_split(Data[Data_headers],Data[Data_targets],test_size=splitting_parcentage,random_state=random_state, stratify=Data[Data_targets])
    return x_train, x_test,y_train, y_test

################################################################################################
#Function Name : build_pipeline
#Input : Nothing
#Task : To build pipeline to perform model building tasks
#Output : pipeline
################################################################################################

def build_pipeline():
    pipe = Pipeline([
        ("rf",RandomForestClassifier(n_estimators=150,random_state=42,n_jobs=-1,class_weight=None))
    ])
    return pipe

################################################################################################
#Function Name : traine_pipeline
#Input : pipeline and trainig datasets
#Task : To train the pipeline on training dataset
#Output : trained pipeline
################################################################################################

def train_pipeline(pipe,train_x,train_y):
    pipe.fit(train_x,train_y)
    return pipe

################################################################################################
#Function Name : feature_plot
#Input : dataset and datset features
#Task : To visualize the feattures of dataset and calculate their importance 
#Output : Nothing
################################################################################################

def feature_plot(model,feature_header, title = "Feature Importance"):
    if hasattr(model,'named_steps') and 'rf' in model.named_steps:
        rf = model.named_steps['rf']
        importances = rf.feature_importances_
    elif hasattr(model,'feature_importances_'):
        importances = model.feature_importances_
    else:
        print("Feature Impotances not available for this model")
        return
    
    id = np.argsort(importances)[::-1]
    plt.figure(figsize=(8,6))
    plt.bar(range(len(importances)),importances[id])
    plt.xticks(range(len(importances)), [feature_header[i] for i in id],rotation = 45,ha = 'right')
    plt.ylabel("Importance")
    plt.title(title)
    plt.tight_layout()
    plt.show()

################################################################################################
#Function Name : save_model
#Input : dataset, path to store the model
#Task : To store the trained model
#Output : Nothing
################################################################################################

def save_model(model,path):
    joblib.dump(model,path)
    print(f"\nModel succesfully saved on {path}")

################################################################################################
#Function Name : load_model
#Input : path
#Task : To laod the model from provided path
#Output : dataset
################################################################################################

def load_model(path):
    model = joblib.load(path)
    print(f"\nModel successfully loaded from {path}")
    return model

################################################################################################
#Function Name : MallCaseStudy
#Input : Nothing
#Task : Function from where execution start
#Output : Nothing
################################################################################################

def MallCaseStudy():

    #1. Get the data of dataset from csv file
    Dataset = get_data()

    #2. check the data basic stat
    check_stat(Dataset)

    ################################################################################
    # In Encoding we Encoded Male : 0 and Female : 1
    ################################################################################
    #3. Encode the data and check if encoded succesully in display method
    Dataset = Encode(Dataset)
    print("After Encoding dataset look like:")
    display(Dataset)

    #4 . prepare Features and Target
    Feature_Header = HEADERS[2:]        #['Age','Annual Income (k$)','Spending Score (1-100)]
    Feature_Target = HEADERS[1:-3]      #['Gender]
    
    #5 . Split the dataset into Training and Testing Dataset
    x_train, x_test,y_train, y_test = split(Dataset,0.2,Feature_Header, Feature_Target)

    print("\nx_train shape is :",x_train.shape)
    print("x_test shape is :",x_test.shape)
    print("y_train shape is :",y_train.shape)
    print("y_test shape is :",y_test.shape)

    print("/n Dataset Successfully split into Train and Test Dataset")

    #6. Build + Train pipeline
    Pipeline = build_pipeline()
    trained_model = train_pipeline(Pipeline,x_train,y_train)
    print('Trained Model : \n',trained_model)

    #7 Model predictions
    prediction  = trained_model.predict(x_test)

    #Metrics
    print("\nTraining accuracy : ",accuracy_score(y_train,trained_model.predict(x_train)))
    print("\nTest Accuracy :",accuracy_score(y_test,prediction))
    print("\nClassification report :\n",classification_report(y_test, prediction))
    print("Confusion Matrix : \n",confusion_matrix(y_test, prediction))

    feature_plot(trained_model, Feature_Header)

    #8 Save the model
    save_model(trained_model,MODEL_PATH)

    #9 Load the model
    Loaded = load_model(MODEL_PATH)
    sample = x_test.iloc[[0]]
    pred_loaded = Loaded.predict(sample)
    print(f"\nLoaded model prediction for first test sample : {pred_loaded[0]}")

################################################################################################
#Function Name : main
#Input : Nothing
#Task : Call the function to proceed with task
#Output : Nothing
################################################################################################

def main():

    MallCaseStudy()

################################################################################################
#Application starter
################################################################################################
if __name__ == "__main__":
    main()