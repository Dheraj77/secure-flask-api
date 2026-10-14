from flask import Flask, abort

app = Flask(__name__)

users = {
    101: {"name": "Dheraj"},
    102: {"name": "Alex"}
}

# Simulate User 101 being logged in
logged_in_user = 101

@app.route("/profile/<int:user_id>")
def profile(user_id):

    if user_id != logged_in_user:
        abort(403)

    if user_id not in users:
        abort(404)

    return users[user_id]