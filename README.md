Fake News Detection System

A Machine Learning based Fake News Detection Web Application that classifies news articles as Real or Fake using Natural Language Processing (NLP) and supervised machine learning techniques.

This project helps detect misinformation by analyzing the text of news articles.

Project Overview

Fake news spreads quickly through social media and online platforms. This project builds a machine learning model capable of identifying fake news by learning patterns from labeled datasets.

The system allows users to input news text through a web interface, and the trained model predicts whether the news is real or fake.

Features

Machine Learning based fake news classification

NLP text preprocessing

Web interface for user input

Real-time prediction

High accuracy model (~99%)

Clean and simple UI

Technologies Used

Python

Machine Learning

Natural Language Processing (NLP)

Scikit-learn

Pandas

NLTK

Flask (Web framework)

HTML / CSS


Dataset

The project uses the Fake and Real News Dataset containing news articles labeled as fake or real.

Dataset includes:

Title

Text

Subject

Date

Label

Total samples used: 44,000+ news articles

Machine Learning Model

The model uses:

TF-IDF Vectorization

Passive Aggressive Classifier

Training accuracy achieved:

Accuracy: ~99%
Installation

Clone the repository:

git clone https://github.com/yourusername/fake-news-detection.git

Move into the project directory:

cd fake-news-detection

Install required packages:

pip install -r requirements.txt
Train the Model

Run the training script:

python train_model.py

This will generate:

model.pkl
vectorizer.pkl
Run the Web Application

Start the Flask server:

python app.py

Open the browser and visit:

http://127.0.0.1:5000
Example

Input:

The World Health Organization announced new global health guidelines aimed at improving vaccination coverage.

Output:

Real News
Future Improvements

Deep Learning models (LSTM / BERT)

News URL detection

Social media fake news detection

Confidence score for predictions

Live news verification API

Author

Surendra Korigam
Computer Science Engineering Student

License

This project is open source and available under the MIT License.
