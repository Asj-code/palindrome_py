from palindrome import is_palindrome


def test_is_palindrome_word():
    assert is_palindrome("oso") == "is palindrome"
    assert is_palindrome("") == "is palindrome"


def test_is_palindrome_strings():
    assert is_palindrome("atar a la rata") == "is palindrome"
    assert is_palindrome(" ") == "is palindrome"


def test_is_palindrome_numbers():
    assert is_palindrome("12321") == "is palindrome"












