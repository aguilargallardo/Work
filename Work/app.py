from flask import Flask, request, jsonify, render_template, redirect, url_for
import pickle
import pandas as pd

output = ""
def create_app():
    app = Flask(__name__)
    naive_bayes = pickle.load(open('naive_bayes.pkl', 'rb'))
    tfidf = pickle.load(open('tfidf.pkl', 'rb'))


    @app.route('/')
    def home():
        return render_template('index.html')
        
    @app.route('/predict', methods=['POST'])
    @app.route('/predict', methods=['GET'])
    # def prediction():
    #     try:
    #         if request.method == 'POST':
    #             text = request.values['text']
    #     except KeyError:
    #         return ('''Bad request: one of the required values 
    #         was missing in the request.''')
    #     else:
    #         def prediction(text):
    #             """
    #             This function will be able to take in a string of text that will then be transformed
    #             with countvectorizer so that it can be ran through nearest neighbors to query the 
    #             nearest subreddit to post it on by relevance.
    #             """
    #             #Query subreddit
                
    #             #Transform raw text
    #             new = tfidf.transform([text])
                
    #             #Creates new dense matrix with nearest neighbor values
    #             pred = naive_bayes.predict(new)
                
    #             #return subreddit from nearest neighbor
                
    #             return pred[0]

    #         prediction = prediction(text)
    #         return str(prediction)

        #WITH A FORM 
    def predict():
            """
            This function will be able to take in a string of text that will then be transformed
            with countvectorizer so that it can be ran through nearest neighbors to query the 
            nearest subreddit to post it on by relevance.
            """
            #Query subreddit
            
            #Transform raw text
            new = tfidf.transform(request.form.values())
            
            #Creates new dense matrix with nearest neighbor values
            pred = naive_bayes.predict(new)
            output = pred[0]
            #return subreddit from nearest neighbor
            
            return render_template('index.html', prediction_text='{}'.format(output))

    @app.route('/subReddit', methods=['GET'])
    def subRLink():
        redditLink = "https://www.reddit.com/r/{}".format(output)

        return redirect(redditLink)


    return app