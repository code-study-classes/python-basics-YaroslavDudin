def sum_even_digits(number):
    number_str = str(abs(number))
    total = 0
    for digit in number_str:
        digit_int = int(digit)
        if digit_int % 2 == 0:
            total += digit_int
    return total


def count_vowel_triplets(text):
    text = text.lower()
    count = 0
    vowels = "aeiouy"
    for i in range(len(text) - 2):
        if (text[i] in vowels and
            text[i + 1] in vowels and
            text[i + 2] in vowels):
            count += 1
    return count


def find_fibonacci_index(number):
    a = 0
    b = 1
    index = 1
    while b <= number:
        if b == number:
            return index
        a, b = b, a + b
        index += 1
    return -1


def remove_duplicates(string):
    result = ""
    for char in string:
        if not result or char != result[-1]:
            result += char
    return result
