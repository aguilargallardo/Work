from flask import Flask, request
import pickle
import pandas as pd



def create_app():
    app = Flask(__name__)
    naive_bayes = pickle.load(open('naive_bayes.pkl', 'rb'))
    tfidf = pickle.load(open('tfidf.pkl', 'rb'))
   

    @app.route('/')
    def hello():
        return "Welcome to Post Here!"

    @app.route('/model', methods=['POST'])
    @app.route('/model/<text>', methods=['GET'])
    def prediction(text=None):
        try:
            if request.method == 'POST':
                text = request.values['text']
        except KeyError:
            return ('''Bad request: one of the required values 
            was missing in the request.''')
        else:
            def prediction(text):
                """
                This function will be able to take in a string of text that will then be transformed
                with countvectorizer so that it can be ran through nearest neighbors to query the 
                nearest subreddit to post it on by relevance.
                """
                #Query subreddit
                
                #Transform raw text
                new = tfidf.transform([text])
                
                #Creates new dense matrix with nearest neighbor values
                pred = naive_bayes.predict(new)
                
                #return subreddit from nearest neighbor
                
                return pred[0]

            prediction = prediction(text)
            return str(prediction)

    
    return app