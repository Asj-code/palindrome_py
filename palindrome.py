def is_palindrome(text):
    text = text.lower()
    text = text.replace(" ", "")
    if text == text[::-1]:
        return "is palindrome"
    else:
        return "is not a palindrome"



