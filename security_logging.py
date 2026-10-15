import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

def login(username, password):
    if username == "alex" and password == "practice123":
        logging.info("Login successful for user: %s", username)
        return True

    logging.warning("Failed login attempt for user: %s", username)
    return False


login("alex", "practice123")
login("alex", "wrongpassword")