from input_validation import validate_username


def test_valid_username():
    assert validate_username("alex123") is True


def test_short_username():
    assert validate_username("ab") is False


def test_invalid_characters():
    assert validate_username("<script>") is False


def test_username_not_string():
    assert validate_username(12345) is False