# Post Here Application

## Overview

Post Me is an application that allows you to post your reddit post, which will then go through a machine learning algorithm that will return to you the best subreddit to post on based off subreddit comment data.
I chose this project because it was something I had created years back. Before my current work, I got into programming with python and data science. I was a big fan of creating models and deploying them for people to use. This application in particular was fun to build because I have many friends that use reddit. Reddit is really big, with about 2.8 million subreddits. If you are someone that is new to reddit, how would you decide where to post? Which subreddit would bring the most relevant attention to your post? Of course there are some obvious ones like food or gaming, if you wish to post about food or gaming. But there are so many other subreddits that you might not know is big and can be the most efficient to post on to grab the right audience for your post. 


## How it works

The web app is consisted of a Flask backend with basic CSS/HTML in the front end. In the Flask backend, there is  a machine learning model inside of a function def predict( ). When a user writes a body of text inside of the text box, the text will be transformed (using NLP) into numerical data that can be ran through the machine learning model. Another function called def subRLink( ), will redirect the user to the actual subreddit to post on.

### The Dataset
The dataset used is from a website called Kaggle. The dataset contains 1 million rows of reddit comments with that is categorized into 40 subreddits. 
Dataset Link: https://www.kaggle.com/smagnan/1-million-reddit-comments-from-40-subreddits
`  
| Subreddit | Body |  Controversiality | Score
| ----------- | ----------- | ----------- | ----------- |  
| RoastMe | ..... |   ..... | .... |
| WorldNews | ..... |   ..... | ..... |
| MortalKombat | ..... |   ..... | .... |


### Machine Learning Model (High Level Overview)

The model initially used was a k-Nearest Neighbor model.  However there was some issues. Using this kind of model to deploy on a cloud platform like Heroku was not possible. This is because you need to use the dataset and the model to be able to predict. This would make the entire application too big to even be hosted on Heroku. I believe the size of the application was about 800MB and Heroku caps you at 500MB. Another issue with that was that I only used 250,000 rows of data. This means that using this model was inefficient in terms of data utilization and not being deployable because of how big the application would be. This is also a slower model to use because it needs to reference the dataset to eventually provide you a prediction.

I decided to use a Naive Bayes classification model instead. There are many different models to use but I believed that the Naive Bayes was the best to use in terms of performance and memory. For starters, the k-Nearest Neighbor model is a lazy supervised classifier. Meaning it doesn't learn from the data but memorizes it (this is why you need the dataset to predict on). Naive Bayes is an eager learning algorithm that allows you to train the model and then predict on it independently. This model is capable of learning overtime and out performs k-NN in real time prediction. 

There is more that can be dived deep into this topic as well as introducing and testing with other machine learning algorithms and deep learning/neural network models. Though, my knowledge is not as strong as it was before as I mostly work with general C++ programming at Microsoft now a days.

## What I would do differently
There are many things I would love to do differently. Number one is investing more time into this project because it requires a lot of research and proper configuration to achieve the highest accuracy. When you talk about a classification model, you want to be able to achieve the best accuracy, else your model is pretty useless. The first thing you want to do to make your model more accurate is wrangling more data. If I created a model that only contains 2 classifications, then 1 millions rows of data might have be sufficient, however with a dataset that has 40 different classifications, 1 million rows of data is not enough. On top of that, maybe a different eager learning model that allows hyperparameter to optimize the model could have been a better route as well however you would need a substantial amount of research to find the best hyperparameters and model. You would also need more computing power. 

###  How can I improve the general application?
I would use the reddit API to constantly grab more data for the 40 different subreddits. I would make a data pipeline that allows the machine learning model to constantly train itself with the new data about ever week. The one weekly retraining the model can vary of course, based on accuracy output, cost of hosting the pipeline, cost of computing power and the requests received to serve the ML model. Overall, this would allow for the application to uses millions of rows of data to work with as well as access to more cloud computing power to train and run the model. This is more into the space of big data, however with research and time, it would be possible.
