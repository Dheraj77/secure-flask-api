import sqlite3


def find_user(connection, username):
    return connection.execute(
        "SELECT * FROM users WHERE username = ?",
        (username,)
    ).fetchall()


if __name__ == "__main__":
    connection = sqlite3.connect(":memory:")

    connection.execute("""
    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        username TEXT
    )
    """)

    connection.executemany(
        "INSERT INTO users (username) VALUES (?)",
        [("dheraj",), ("alex",), ("sam",)]
    )

    rows = connection.execute("SELECT * FROM users").fetchall()
    print(rows)

    username = "alex"

    query = "SELECT * FROM users WHERE username = '" + username + "'"
    print("Generated SQL:", query)

    result = find_user(connection, username)
    print("Query result:", result)

    connection.close()