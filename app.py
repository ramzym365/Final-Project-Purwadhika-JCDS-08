from flask import Flask, render_template, jsonify, request
import joblib
import pandas as pd
import json
import pickle
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

app = Flask(__name__)

df = pd.read_csv(r'E:\Job Connector Data Science Purwadhika\Module-03-Machine Learning\ulikan\Untitled Folder\Adult_Clean.csv')
df.drop('Unnamed: 0', axis = 1, inplace = True)

x = df.drop(['Income', 'Capital Gain', 'Capital Loss', 'Final Weight'], axis = 1)
y = df['Income'].map({'>50K' : 1, '<=50K' : 0})

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.20, random_state = 0)

# home route
@app.route('/')
def home():
    return render_template('home.html')

#introduction route
@app.route('/introduction')
def introduction():
    return render_template('introduction.html')

#dataset route
@app.route('/dataset')
def dataset():
    return render_template('dataset.html')

#visualization route
@app.route('/visualization')
def visualization():
    return render_template('visualization.html')

#conclusion route
@app.route('/conclusion')
def conclusion():
    return render_template('conclusion.html')

@app.route('/prediction')
def prediction():
    return render_template('prediction.html')

@app.route('/result', methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        input = request.form

        Age = int(input['Age'])

        Workclass = input['Workclass']
        if Workclass == 'Private':
            dataWC = 'Private'
            strWC = 'Private'
        elif Workclass == 'Government':
            dataWC = 'Government'
            strWC = 'Government'
        elif Workclass == 'Self-employed':
            dataWC = 'Self-employed'
            strWC = 'Self Employed'
        elif Workclass == 'Other':
            dataWC = 'Other'
            strWC = 'Other'
        
        Education = input['Education']
        if Education == 'Preschool':
            dataEdu = 'Preschool'
            strEdu = 'Preschool'
        elif Education == 'Elementary-School':
            dataEdu = 'Elementary-School'
            strEdu = 'Elementary School'
        elif Education == 'Middle-School':
            dataEdu = 'Middle-School'
            strEdu = 'Middle School'
        elif Education == 'High-School':
            dataEdu = 'High-School'
            strEdu = 'Some Years in High School'
        elif Education == 'HS-grad':
            dataEdu = 'HS-grad'
            strEdu = 'High School Graduate'
        elif Education == 'Prof-school':
            dataEdu = 'Prof-school'
            strEdu = 'Professional School'
        elif Education == 'Assoc-acdm':
            dataEdu = 'Assoc-acdm'
            strEdu = 'Vocational Education'
        elif Education == 'Assoc-voc':
            dataEdu = 'Assoc-voc'
            strEdu = 'Technical Vocational Education'
        elif Education == 'Some-college':
            dataEdu = 'Some-college'
            strEdu = 'Some Years in College'
        elif Education == 'Bachelors':
            dataEdu = 'Bachelors'
            strEdu = 'Bachelor / College Graduate'
        elif Education == 'Masters':
            dataEdu = 'Masters'
            strEdu = 'Master Graduate'
        elif Education == 'Doctorate':
            dataEdu = 'Doctorate'
            strEdu = 'Doctorate Graduate'

        Years_Of_Education = int(input['Years of Education'])
        
        Marital_Status = input['Marital Status']
        if Marital_Status == 'Single':
            dataMarital = 'Single'
            strMarital = 'Single'
        elif Marital_Status == 'Married':
            dataMarital = 'Married'
            strMarital = 'Married'
        elif Marital_Status == 'Separated':
            dataMarital = 'Separated'
            strMarital = 'Separated'
        elif Marital_Status == 'Divorced':
            dataMarital = 'Divorced'
            strMarital = 'Divorced'
        elif Marital_Status == 'Widowed':
            dataMarital = 'Widowed'
            strMarital = 'Widowed'

        Occupation = input['Occupation']
        if Occupation == 'Craft-repair':
            dataOccu = 'Craft-repair'
            strOccu = 'Handyman / Craft Repairman'
        elif Occupation == 'Prof-specialty':
            dataOccu = 'Prof-specialty'
            strOccu = 'Professional Specialty (Engineer, Teacher, etc.)'
        elif Occupation == 'Adm-clerical':
            dataOccu = 'Adm-clerical'
            strOccu = 'Administrative Cleric'
        elif Occupation == 'Exec-managerial':
            dataOccu = 'Exec-managerial'
            strOccu = 'Executive Managerial'
        elif Occupation == 'Sales':
            dataOccu = 'Sales'
            strOccu = 'Sales'
        elif Occupation == 'Machine-op-inspct':
            dataOccu = 'Machine-op-inspct'
            strOccu = 'Machine Operational Inspector'
        elif Occupation == 'Transport-moving':
            dataOccu = 'Transport-moving'
            strOccu = 'Transport Moving'
        elif Occupation == 'Handlers-cleaners':
            dataOccu = 'Handlers-cleaners'
            strOccu = 'Handler / Cleaner'
        elif Occupation == 'Farming-fishing':
            dataOccu = 'Farming-fishing'
            strOccu = 'Farmer / Fisher'
        elif Occupation == 'Tech-support':
            dataOccu = 'Tech-support'
            strOccu = 'Tech Support'
        elif Occupation == 'Protective-serv':
            dataOccu = 'Protective-serv'
            strOccu = 'Protective Service'
        elif Occupation == 'Priv-house-serv':
            dataOccu = 'Priv-house-serv'
            strOccu = 'Private House Service'
        elif Occupation == 'Armed-Forces':
            dataOccu = 'Armed-Forces'
            strOccu = 'Armed Forces'
        elif Occupation == 'Other-service':
            dataOccu = 'Other-service'
            strOccu = 'Other Service'

        Role_in_Family = input['Role in Family']
        if Role_in_Family == 'Husband':
            dataRole = 'Husband'
            strRole = 'Husband'
        elif Role_in_Family == 'Wife':
            dataRole = 'Wife'
            strRole = 'Wife'
        elif Role_in_Family == 'Own-child':
            dataRole = 'Own-child'
            strRole = 'Child'
        elif Role_in_Family == 'Unmarried':
            dataRole = 'Unmarried'
            strRole = 'Unmarried'
        elif Role_in_Family == 'Other-relative':
            dataRole = 'Other-relative'
            strRole = 'Other Relative'
        elif Role_in_Family == 'Not-in-family':
            dataRole = 'Not-in-family'
            strRole = 'Not in Family / Support ownself'

        Race = input['Race']
        if Race == 'White':
            dataRace = 'White'
            strRace = 'White'
        elif Race == 'Black':
            dataRace = 'Black'
            strRace = 'Black'
        elif Race == 'Asian-Pac-Islander':
            dataRace = 'Asian-Pac-Islander'
            strRace = 'Asian Pacific Islander'
        elif Race == 'Amer-Indian-Eskimo':
            dataRace = 'Amer-Indian-Eskimo'
            strRace = 'American Native'
        elif Race == 'Other':
            dataRace = 'Other'
            strRace = 'Other'
        
        Gender = input['Gender']
        if Gender == 'Male':
            dataGender = 'Male'
            strGender = 'Male'
        elif Gender == 'Female':
            dataGender = 'Female'
            strGender = 'Female'
        
        Workhours_pw = int(input['Workhours per Week'])

        Native_Country = input['Native Country']
        if Native_Country == 'United-States':
            dataCountry = 'United-States'
            strCountry = 'United States'
        elif Native_Country == 'Outside-US':
            dataCountry = 'Outside-US'
            strCountry = 'Outside United States'

        input_predict = pd.DataFrame({
            'Age' : [Age],
            'Workclass' : [dataWC],
            'Education' : [dataEdu],
            'Years of Education' : [Years_Of_Education],
            'Marital Status' : [dataMarital],
            'Occupation' : [dataOccu],
            'Role in Family' : [dataRole],
            'Race' : [dataRace],
            'Gender' : [dataGender],
            'Workhours per Week' : [Workhours_pw],
            'Native Country' : [dataCountry]
        })

        predict = model.predict(input_predict)[0]

        if predict == 0:
            result = 'Income <= 50K'
        elif predict == 1:
            result = 'Income >50K'

        y_pred = model.predict(x_test)
        accu_score = round(accuracy_score(y_test, y_pred), 4)*100

        return render_template('result.html', Age = Age, Workclass = strWC, Education = strEdu, YearsEdu = Years_Of_Education,
                Marital_Status = strMarital, Occupation = strOccu, RoleinFamily = strRole, Race = strRace, 
                Gender = strGender, Workhours_PW = Workhours_pw, Native_Country = strCountry, accu_score = accu_score, result = result)

if __name__ == '__main__':
    model = pickle.load(open(r'E:\Job Connector Data Science Purwadhika\Module-03-Machine Learning\ulikan\Untitled Folder\model_fix.sav', 'rb'))
    app.run(debug=True)
