from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load trained model
model = pickle.load(open("model/model.pkl", "rb"))
vectorizer = pickle.load(open("model/vectorizer.pkl", "rb"))

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def predict():

    news = request.form['news']

    data = vectorizer.transform([news])

    prediction = model.predict(data)

    result = prediction[0]

    if result == "FAKE" or result == 1:
        message = "⚠ Fake News Detected"
    else:
        message = "✔ This News is Real"

    return render_template(
        "index.html",
        prediction_text=message
    )


if __name__ == "__main__":
    app.run(debug=True)