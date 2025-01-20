# Web app
# Windows HP templates route: C:\Users\HP\PycharmProjects\polytopia_python\app\templates
# Windows truncated templates route: C:\PycharmProjects\polytopia_python\app\templates
# relative templates route: polytopia_python\app\templates
from flask import Flask, request, jsonify, render_template
from transformers import pipeline

# Create a Flask app
app = Flask(__name__)

# add Index page, Privacy, Dashboard, About, Settings, HallOfFame and ThroneRoom routes! I have the content for them, you just make the routes and the navigation!

# Route for the homepage
@app.route("/")
def home():
    return (
        '''
            <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chat Dashboard</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f9;
        }

        .header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            background-color: #6200ea;
            color: white;
            padding: 10px 20px;
        }

        .header .icons {
            display: flex;
            gap: 15px;
        }

        .header .icons img {
            width: 24px;
            height: 24px;
            cursor: pointer;
        }

        .chat-container {
            display: flex;
            flex-direction: column;
            height: calc(100vh - 50px);
            padding: 20px;
            box-sizing: border-box;
        }

        .chats-dashboard {
            flex: 1;
            overflow-y: auto;
            background-color: white;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            padding: 15px;
            margin-bottom: 20px;
        }

        .chat-message {
            display: flex;
            align-items: center;
            margin-bottom: 15px;
        }

        .chat-message img {
            width: 40px;
            height: 40px;
            border-radius: 50%;
            margin-right: 10px;
        }

        .chat-message .message-text {
            background-color: #e0e0e0;
            padding: 10px 15px;
            border-radius: 10px;
            max-width: 70%;
        }

        .input-section {
            display: flex;
            gap: 10px;
        }

        .input-section input {
            flex: 1;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
            font-size: 16px;
        }

        .input-section button {
            background-color: #6200ea;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
        }

        .input-section button:hover {
            background-color: #4500b5;
        }
    </style>
</head>
<body>
    <div class="header">
        <div class="title">Chats</div>
        <div class="icons">
            <img src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png" alt="User Icon" title="User">
            <img src="https://cdn-icons-png.flaticon.com/512/929/929610.png" alt="Share Icon" title="Share">
        </div>
    </div>

    <div class="chat-container">
        <div class="chats-dashboard" id="chatsDashboard">
            <!-- Messages will appear here -->
        </div>

        <div class="input-section">
            <input type="text" id="messageInput" placeholder="Type your message here...">
            <button onclick="sendMessage()">Send</button>
        </div>
    </div>

    <script>
        function sendMessage() {
            const messageInput = document.getElementById('messageInput');
            const chatsDashboard = document.getElementById('chatsDashboard');

            // Get the user's message
            const messageText = messageInput.value.trim();

            // Only send if message is not empty
            if (messageText !== '') {
                // Create a new chat message
                const messageDiv = document.createElement('div');
                messageDiv.classList.add('chat-message');

                const userIcon = document.createElement('img');
                userIcon.src = 'https://cdn-icons-png.flaticon.com/512/3135/3135715.png';
                userIcon.alt = 'User';

                const messageContent = document.createElement('div');
                messageContent.classList.add('message-text');
                messageContent.textContent = messageText;

                messageDiv.appendChild(userIcon);
                messageDiv.appendChild(messageContent);

                // Append the new message to the dashboard
                chatsDashboard.appendChild(messageDiv);

                // Scroll to the bottom of the chat dashboard
                chatsDashboard.scrollTop = chatsDashboard.scrollHeight;

                // Clear the input field
                messageInput.value = '';
            }
        }
    </script>
</body>
</html>
    '''
            )

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

# Route for the Dashboard page
# TODO Fix error Template file 'dashboard. html' not found
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

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
