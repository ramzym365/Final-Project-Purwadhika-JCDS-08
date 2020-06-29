## Final-Project-Purwadhika-JCDS-08 - Income Prediction

About
-------
Final Project for Job Connector Data Science Program at Purwadhika Digital School.

This data was extracted from the 1994 Census United States bureau database by Ronny Kohavi and Barry Becker (Data Mining and Visualization, Silicon Graphics). This dataset task is to determine accurately whether a person makes over $50K a year or not.
You can access the dataset from this <a href="https://www.kaggle.com/uciml/adult-census-income">link.</a>


This is Classification task. In this project, I will use 4 models(Logistic Regression, Support Vector Classification, Random Forest Classifier, and XGBoost Classifier). With each model, I will be performing Hyperparameter Tuning.

Knowledege & Usability
-------
1. Providing accurate and up-to-date data that can be accounted for
2. Designing an appropriate policy package (Workclass sector, race-biased program, etc.)
3. Planning an efficient infrastructure to provide and improve economy


Model Building & Evaluation
-------
Before building model, I've done some cleaning including Renaming Columns, Dropping Duplicate Data, Categorizing Feature, and Cleaning Null Values ('?'). 
Furthermore in this process, you can see '1 Data Cleaning' notebook.<br>
Also I've done some Exploratory Data Analysis (EDA) that can be seen on the '2 EDA' notebook.

For building this model, I've done some Feature Selection, Outliers Handling with Scaling, and Handling Imbalanced Data with SMOTE that can be seen in '3 Building Model' notebook.
In addition, for this project, I use 4 different kind models with each model I apply a randomized search Hyperparameter Tuning.
Here are the evaluation metrics for those 8 different models :

  <center>
  
| Models                                                     |  Accuracy Score | F1-Score    |
|------------------------------------------------------------| :--------------:|:-----------:|
| Logistic Regression                                        |         0.805317|    0.879253 |
| Logistic Regression with Hyperparameter Tuning             |         0.800860|    0.876712 |
| Support Vector Classifier (SVC)                            |         0.820990|    0.889332 |
| Support Vector Classifier (SVC) with Hyperparameter Tuning |         0.822526|    0.890718 |
| Random Forest Classifier                                   |         0.820529|    0.884767 |
| Random Forest Classifier with Hyperparameter Tuning        |         0.838967|    0.897516 |
| XGBoost Classifier                                         |         0.842502|    0.899124 |
| XGBoost Classifier with Hyperparameter Tuning              |         0.842655|    0.899371 |

  </center>

Also, I am showing ROC curve for each models. Hereby is the ROC curve :

<p align="center">
  <img src="https://github.com/farizdar/Final-Project-Purwadhika-JCDS-08/blob/master/static/roc.png" width="600" height="400" >
</p>

For each model, the AUC-ROC score is :
| Models                                                     |  AUC-ROC Score  | 
|------------------------------------------------------------| :----:|
| Logistic Regression                                        |         0.82439 |  
| Logistic Regression with Hyperparameter Tuning             |         0.81496 |   
| Support Vector Classifier (SVC)                            |         0.86774 |  
| Support Vector Classifier (SVC) with Hyperparameter Tuning |         0.85892 |  
| Random Forest Classifier                                   |         0.86121 |  
| Random Forest Classifier with Hyperparameter Tuning        |         0.88688 |   
| XGBoost Classifier                                         |         0.88830 |   
| XGBoost Classifier with Hyperparameter Tuning              |         0.88830 |   

From the AUC and AUC-ROC score, XGBoost model has the biggest score.
So from our evaluation metrices (F1-Score, Accuracy Score, and AUC-ROC), I can draw a conclusion that XGBoost Classifier with Hyperparameter Tuning model is the best model for this project.

### Thank you for reading until the end!

#### Fariz Darmawan 
#### [Email](darmawanfariz@gmail.com) | [LinkedIn](https://www.linkedin.com/in/fariz-darmawan-a28600b3//) | [GitHub](https://github.com/farizdar/) 
