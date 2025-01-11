# Windows HP templates route: C:\Users\HP\PycharmProjects\polytopia_python\app\templates
# Windows truncated templates route: C:\PycharmProjects\polytopia_python\app\templates
# relative templates route: polytopia_python\app\templates
from flask import Flask, render_template

# Create a Flask app
app = Flask(__name__)

# add Index page, Privacy, Dashboard, About, Settings, HallOfFame and ThroneRoom routes! I have the content for them, you just make the routes and the navigation!

# Route for the homepage
@app.route("/")
def home():
    return (
        """
            <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Index</title>
</head>
<body>
{% extends "base.html" %}

{% block content %}
<h1>Word in Context decision maker model</h1><p>The server is running at 127.0.0.1:5000</p>"
<p>This is the Index page. Explore other sections using the navigation above.</p>
{% endblock %}
@{
	ViewData["Title"] = "Home Page";
}

<div class="text-center">
	<form action="/chat" method="post">
		<label for="my-chats" class="toggle">
			<input type="submit" name="my-chats" value="My chats" />
			<span class="toggle-btn">

			</span>

		</label>
	</form>

</div>
<style>
	.toggle .toggle-btn {
		display: inline-block;
		width: 60px;
		text-align: center;
		padding: 5px 0;
		font-size: 14px;
		font-weight: bold;
		color: white;
		background-color: lightblue;
		border-radius: 5px;
		user-select: none;
		transition: all 0.3s ease;
	}

	.toggle .toggle-btn:hover {
		background-color: white;
		color: black;
		border: 1px solid black;
	}
</style>
</body>
</html>
    """
            )

@app.route("/chat")
def chat():
    return ""

# Route for the Privacy page
@app.route("/privacy")
def privacy():
    return
"""
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
"""

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




if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
