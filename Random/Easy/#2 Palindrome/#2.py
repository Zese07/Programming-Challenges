def is_palindrome(s):
    if s == s[::-1]:
        return "String is palindrome."

    return "String is not palindrome."

while True:
    s = input("String: ").lower().replace(" ", "")
    print(s)
    if not any(c.isdigit() for c in s):
        print(is_palindrome(s))
        break
    else:
        print("String not valid.")
