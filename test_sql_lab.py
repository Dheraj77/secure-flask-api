import sqlite3
from sql_lab import find_user

def test_normal_username():
    connection = sqlite3.connect(":memory:")
    connection.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT)")
    connection.execute("INSERT INTO users (username) VALUES (?)", ("alex",))

    result = find_user(connection, "alex")

    assert result == [(1, "alex")]
    connection.close()


def test_sql_injection_blocked():
    connection = sqlite3.connect(":memory:")
    connection.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT)")
    connection.execute("INSERT INTO users (username) VALUES (?)", ("alex",))

    result = find_user(connection, "' OR 1=1 --")

    assert result == []
    connection.close()