from flask import Flask, render_template, jsonify, request
import joblib
from sklearn.metrics.pairwise import cosine_similarity
# import pandas as pd
import json

app = Flask(__name__)


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

# @app.route('/results', methods=['GET','POST'])
# def results():
    # if request.method == 'POST':
    #     inputtitle = request.form['MTV']
    #     data = inputtitle.lower()
    #     cosScore = cosine_similarity(countmatrix.toarray())
    #     indices = pd.Series(dfNFRec['title'].str.lower())
    #     if data in indices.tolist():
    #         def recommend(title, cosScore=cosScore):
    #             idx = indices[indices == title].index[0]
    #             simscores = list(enumerate(cosScore[idx]))
    #             simscores = sorted(simscores, key=lambda x: x[1], reverse=True)
    #             simscores = simscores[1:11]
    #             movieshowindices = [i[0] for i in simscores]
    #             return df.iloc[movieshowindices]
        
    #         rec = recommend(data)

    #         return render_template('NFR_results.html', inputtitle=inputtitle, rec=rec)

    #     else:
    #         return render_template('NFR_error.html')


if __name__ == '__main__':
    # countmatrix = joblib.load('CVJoblib') 
    # df = pd.read_csv('dfcleaned.csv')
    # dfNFRec = pd.read_csv('dfNFRec.csv')
    app.run(debug=True)
