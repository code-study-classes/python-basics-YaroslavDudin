check_between_numbers = lambda a, b, c: (a < b and b < c) or (c < b and b < a)

check_odd_three = lambda number: number >= 100 and number <= 999 and number % 2 != 0 or number <= -100 and number >= -999 and number % 2 != 0

check_unique_digits = lambda number: (
    number >= 100
    and number <= 999
    and str(number)[0] != str(number)[1]
    and str(number)[0] != str(number)[2]
    and str(number)[1] != str(number)[2]
    or number <= -100
    and number >= -999
    and str(abs(number))[0] != str(abs(number))[1]
    and str(abs(number))[0] != str(abs(number))[2]
    and str(abs(number))[1] != str(abs(number))[2]
)

def check_palindrome_number(number):
    number_str = str(number)
    reversed_str = number_str[::-1]
    return number_str == reversed_str

check_ascending_digits = lambda number: (
    number >= 100
    and number <= 999
    and int(str(number)[0]) < int(str(number)[1])
    and int(str(number)[1]) < int(str(number)[2])
)
