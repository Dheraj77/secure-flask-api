from flask import Flask, abort

app = Flask(__name__)

users = {
    101: {"name": "Dheraj", "email": "user101@example.com"},
    102: {"name": "Alex", "email": "user102@example.com"}
}

# Simulating a logged-in user
logged_in_user = 101

@app.route("/profile/<int:user_id>")
def profile(user_id):

    if user_id != logged_in_user:
        abort(403)

    return users.get(user_id, {"error": "User not found"})