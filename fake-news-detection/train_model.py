from flask import Flask, render_template, request
import pickle
import re

app = Flask(__name__)

# Load model and vectorizer
model = pickle.load(open("model/model.pkl", "rb"))
vectorizer = pickle.load(open("model/vectorizer.pkl", "rb"))


# same preprocessing used in training
def clean_text(text):

    text = text.lower()

    text = re.sub('[^a-zA-Z]', ' ', text)

    return text


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def predict():

    news = request.form['news']

    # clean user input
    news = clean_text(news)

    data = vectorizer.transform([news])

    prediction = model.predict(data)

    result = prediction[0]

    if result == "FAKE":
        message = "⚠ Fake News Detected"
    else:
        message = "✔ This News is Real"

    return render_template("index.html", prediction_text=message)


if __name__ == "__main__":
    app.run(debug=True)