def validate_username(username):
    if not isinstance(username, str):
        return False

    if len(username) < 3 or len(username) > 20:
        return False

    if not username.isalnum():
        return False

    return True


if __name__ == "__main__":
    print(validate_username("alex"))
    print(validate_username("ab"))
    print(validate_username("<script>"))
    print(validate_username("alex123"))