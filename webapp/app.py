from flask import Flask, render_template, request
import json
import pickle
from nltk.tokenize import RegexpTokenizer
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
import re
from sklearn.ensemble import GradientBoostingClassifier

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/callback/<endpoint>')
def cb(endpoint):   
    if endpoint == "predict":
        return model(request.args.get('data'))
    else:
        return "Bad endpoint", 400

def text_preprocessing(text):
    with open('static/models/complete_stopwords_list.pickle', 'rb') as handle:
            complete_stopwords_list = pickle.load(handle)
    # lowercase
    text = text.lower()
    #remove ponctuation
    cleaned_text = re.sub("([^A-Za-z0-9|\s|[:punct:]]*)", '', text)
    # tokenize
    text_list = cleaned_text.split()
    # remove stopwords
    tokens = [word for word in text_list if word not in complete_stopwords_list]
    # lemmatize
    lemmatize = WordNetLemmatizer()
    lemmatized_list = [lemmatize.lemmatize(word) for word in tokens if len(lemmatize.lemmatize(word)) > 2]
    # rejoin our tokens into sentences
    words = ' '.join([word for word in lemmatized_list])
    return words

def model(corpus):
    text_preprocessed = text_preprocessing(corpus)

    with open('static/models/count_vectorizer.pickle', 'rb') as handle:
        cv = pickle.load(handle)

    vectorized_text = cv.transform([text_preprocessed])

    with open('static/models/best_model.pickle', 'rb') as handle:
        model = pickle.load(handle)

    prediction = model.predict(vectorized_text)

    prediction_dict =  {
        'prediction': int(prediction)
    }

    return json.dumps(prediction_dict)