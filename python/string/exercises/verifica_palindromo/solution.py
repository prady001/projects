def eh_palindromo(s):
    return s[::-1].lower() == s[::].lower()