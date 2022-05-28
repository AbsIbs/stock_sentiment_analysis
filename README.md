# Stock Sentiment Analysis
![image](https://github.com/AbsIbs/stock_sentiment_analysis/raw/main/images/sa_business_statement.png)

## Table of Contents
- <a href="#business-case">Business Case</a>
- <a href="#requirements">Requirements</a>
- <a href="#installation">Installation</a>
- <a href="#demo-and-usage">Demo and Usage</a>
- <a href="#dataset">Dataset</a>
- <a href="#exploratory-data-analysis">Exploratory Data Analysis</a>
- <a href="#modelling">Modelling</a>
- <a href="#model-performance">Model Performance</a>
- <a href="#conclusion">Conclusion</a>

## Business Case
Sentiment analysis is a fundamental practice in trading. This is even more so in today’s world where social media is rife with opinions on trading.

The aim is to create an NLP classification model that classifies tweets regarding trading into positive or negative sentiments in order to aid investment decisions.

## Requirements
This project assumes you already have these system dependencies set up:
- **Python 3.8.5**
- **pip**
- **Conda environment set-up**

## Installation
As all the dependencies are stored in the **requirements.txt** file, running this command in your bash/terminal  <br>
```bash
pip: -r requirements.txt
```

## Demo and Usage
The classification model has been deployed onto a simple [webapp](https://absibs-sentiment-analysis.herokuapp.com/) where the user can type out the tweet and be advised on whether or not the tweet is a positve/negative sentiment.
<br><br>
![image](https://github.com/AbsIbs/stock_sentiment_analysis/raw/main/images/webapp.png)

## Dataset
- The dataset was retrieved from [Kaggle](https://www.kaggle.com/code/adeyoyintemidayo/stock-data-eda-and-prediction/data).
- The dataset is **unbalanced**
- The tweets are in **english**
- It contains near 6000 tweets with 63% classified as positive sentiments and 37% classified as negative
<br><br>
![image](https://github.com/AbsIbs/stock_sentiment_analysis/raw/main/images/dataset.png)

## Methodology
![image](https://github.com/AbsIbs/stock_sentiment_analysis/raw/main/images/sa_methodology.png)
<br><br>
The methodology follows the general steps of text preprocessing for NLP modelling.
- Lowercasing
- Stripping ponctuation
- Tokenization
- Removal of stopwords
- Lemmatization
- Vectorization

For this project, the vectorization technique used is a **simple count vectorizer**. Whilst I tracked each of the 4 metrics, the main metric of interest is accuracy.

## Exploratory Data Analysis
For the EDA, focus was given to constructing word clouds. This gives a visual representation of the distribution of words used for positive and negative sentiments.

![image](https://github.com/AbsIbs/stock_sentiment_analysis/raw/main/images/positive_word_cloud.png)
<br><br>
From the image, we see that words such as ‘buy, long and break’ were most common for positive sentiments. 

![image](https://github.com/AbsIbs/stock_sentiment_analysis/raw/main/images/negative_word_cloud.png)
<br><br>
In contrast, words such as ‘coronavirus, sell and stop’ were very common in negative sentiments.

## Modelling
The following models were used in the project;
> Logistic Regression<br>
> Random Forest<br>
> Gradient Boost<br>
> Naive Bayes<br>

The models were then tuned using **optuna**.

Whilst our project records the following 4 metrics:
> Accuracy<br>
> Recall<br>
> F1<br>
> Precision,<br>

the main focus is going to be on **Accuracy**.

## Model Performance
![image](https://github.com/AbsIbs/stock_sentiment_analysis/raw/main/images/results.png)
<br><br>
As we see, our best performing model was a tuned gradient boosting model with an accuracy score of **73%**.
<br><br>
|                classifiers 	| val_accuracy 	| val_recall 	| val_precision 	| val_f1 	|
|---------------------------:	|-------------:	|-----------:	|--------------:	|-------:	|
|       Tuned Gradient_boost 	|         0.73 	|       0.87 	|          0.75 	|   0.81 	|
|        Tuned Random_Forest 	|         0.72 	|       0.81 	|          0.77 	|   0.79 	|
| Tuned   Logistic_regresion 	|         0.72 	|       0.75 	|          0.80 	|   0.78 	|
|                Naive_Bayes 	|         0.72 	|       0.81 	|          0.76 	|   0.79 	|
|             Gradient_boost 	|         0.71 	|       0.95 	|          0.70 	|   0.81 	|
|              Random_Forest 	|         0.67 	|       0.70 	|          0.77 	|   0.72 	|
|         Logistic_regresion 	|         0.66 	|       0.68 	|          0.76 	|   0.72 	|

We can further examine our best model by plotting a **confusion matrix**.
<br><br>
![image](https://github.com/AbsIbs/stock_sentiment_analysis/raw/main/images/cm.png)
<br><br>
Overall, we wish to minimize both our false positives and false negatives. For our best model, we can see values of 16% and 9% respectively. It appears that the model is better at predicting negative tweets as opposed to positive ones.

## Conclusion
- As the model seems to be better at predicting negative tweets, it may be better suited for bears rather than bulls
- The accuracy of the model is not high enough for investors to solely rely on it. Investors should use this tool along side other factors and/or models before making an investment decision
 
 ## Future Work
 - Different vectorization techniques can be used e.g. **TF-IDF**
 - Neural Network architectures can be used aswell e.g. **LSTM** with **word embeddings**
