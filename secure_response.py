from flask import Flask, jsonify

app = Flask(__name__)

user = {
    "name": "Alex",
    "email": "alex@example.com",
    "password_hash": "dummy-hash-for-practice"
}

@app.route("/profile")
def profile():
    safe_user = {
        "name": user["name"],
        "email": user["email"]
    }

    return jsonify(safe_user)


if __name__ == "__main__":
    app.run(debug=False)