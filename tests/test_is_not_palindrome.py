from palindrome import is_palindrome


def test_is_not_a_palindrome_word():
    assert is_palindrome("Perro") == "is not a palindrome"


def test_is_not_palindrome_strings():
    assert is_palindrome("ana lava la ropa") == "is not a palindrome"
    assert is_palindrome("@gmail") == "is not a palindrome"