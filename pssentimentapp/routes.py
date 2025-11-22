from flask import render_template, request
from . import app, client


@app.route("/", methods=["GET", "POST"])
def index():
    sentiment = None
    if request.method == "POST":
        user_text = request.form.get("user_text", "")
        if user_text.strip():
            response = client.analyze_sentiment([user_text])[0]
            sentiment = response.sentiment
    return render_template("index.html", sentiment=sentiment)
