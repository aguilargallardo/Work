from flask import Flask, request, jsonify, render_template, redirect, url_for
import pickle
import pandas as pd

def create_app():
    app = Flask(__name__)
    naive_bayes = pickle.load(open('naive_bayes.pkl', 'rb'))
    tfidf = pickle.load(open('tfidf.pkl', 'rb'))


    @app.route('/')
    def home():
        return render_template('home.html')
        
    @app.route('/predict', methods=['POST'])
    @app.route('/predict', methods=['GET'])
    def predict():
            """
            This function will be able to take in a string of text that will then be transformed
            with countvectorizer so that it can be ran through nearest neighbors to query the 
            nearest subreddit to post it on by relevance.
            """
            if request.method == 'GET':
                 return render_template('index.html')

            elif request.method == 'POST':
                #Transform raw text
                new = tfidf.transform(request.form.values())
                
                #Creates new dense matrix with nearest neighbor values
                pred = naive_bayes.predict(new)
                global output 
                output = pred[0]

                #return subreddit from nearest neighbor
                return render_template('index.html', prediction_text=output)
   
    @app.route('/subReddit', methods=['GET'])
    def subRLink():
        redditLink = "https://www.reddit.com/r/{}".format(output)
        return redirect(redditLink)


    return app

APP = create_app()