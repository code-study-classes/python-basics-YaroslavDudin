def square_odds(numbers):
    result = []
    for num in numbers:
        if num % 2 != 0:
            result.append(num * num)
    return result

def normalize_names(names):
    result = []
    for name in names:
        result.append(name.capitalize())
    return result

def remove_invalid_emails(emails):
    result = []
    for email in emails:
        if email.count('@') == 1 and len(email) >= 5 and not email.startswith('@') and not email.endswith('@'):
            result.append(email)
    return result

def filter_palindromes(words):
    result = []
    for word in words:
        word_lower = word.lower()
        if word_lower == word_lower[::-1]:
            result.append(word)
    return result

def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        return factorial

def find_common_prefix(strings):
    if not strings:
        return ""

    prefix = strings[0]
    for i in range(1, len(strings)):
        while not strings[i].startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix
