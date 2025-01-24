# Web app
# Windows HP templates route: C:\Users\HP\PycharmProjects\polytopia_python\app\templates
# Windows truncated templates route: C:\PycharmProjects\polytopia_python\app\templates
# relative templates route: polytopia_python\app\templates
from flask import Flask, request, jsonify, render_template
from transformers import pipeline
from transformers.agents.evaluate_agent import classifier

# Create a Flask app
app = Flask(__name__)

# add Index page, Privacy, ChatsList, About, Settings routes

# Route for the homepage
@app.route("/")
def home():
    return render_template("home.html", title="Home Page")

@app.route("/chat")
def chat():
    return ""

# Route for the Privacy page
@app.route("/privacy")
def privacy():
    return
'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
{% extends "base.html" %}

{% block content %}
<h1>Privacy Policy</h1>
<p>This is the Privacy page content.</p>
{% endblock %}

</body>
</html>
'''


# Route for the Chats List page
@app.route("/chats-list")
def chats_list():
    return render_template("chats-list.html")

# Route for the About page
@app.route("/about")
def about():
    return render_template("about.html")

# Route for the Settings page
@app.route("/settings")
def settings():
    return render_template("settings.html")


@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        sentence_a = data.get("sentence_a", "")
        sentence_b = data.get("sentence_b", "")
        target_word = data.get("target_word", "")

        if not sentence_a or not sentence_b or not target_word:
            return jsonify({"error": "Hiányzó bemenet"}), 400

        # Formázzuk a bemenetet
        input_text = f"A: {sentence_a} B: {sentence_b} X: {target_word}"
        result = classifier(input_text)

        # Egyszerűsített válasz
        prediction = "YES" if result[0]['label'] == 'LABEL_1' else "NO"

        return jsonify({"prediction": prediction})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
