from palindrome import is_palindrome


def test_is_palindrome():
    assert is_palindrome("oso") == "is palindrome"
    assert is_palindrome("12321") == "is palindrome"
    assert is_palindrome("atar a la rata") == "is palindrome"
    assert is_palindrome(" ") == "is palindrome"
    assert is_palindrome("") == "is palindrome"


def test_is_not_a_palindrome():
    assert is_palindrome("Perro") == "is not a palindrome"
    assert is_palindrome("@gmail") == "is not a palindrome"
    assert is_palindrome("ana lava la ropa") == "is not a palindrome"





