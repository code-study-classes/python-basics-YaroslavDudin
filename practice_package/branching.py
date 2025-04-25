def is_weekend(day):
  days = {
      6: True,
      7: True
  }
  return days.get(day, False)

def get_discount(amount):
    discount1 = amount * 0.1 if amount >= 5000 else 0
    discount2 = amount * 0.05 if amount >= 1000 and amount < 5000 else 0
    return discount1 or discount2

def describe_number(n):
    if n < 10:
        digits = "однозначное"
    elif n < 100:
        digits = "двузначное"
    else:
        digits = "трехзначное"

    parity = "четное" if n % 2 == 0 else "нечетное"

    return f"{parity} {digits} число"


def convert_to_meters(unitNumber, lengthInUnits):
    units = {
        1: lengthInUnits * 0.1,
        2: lengthInUnits * 1000,
        3: lengthInUnits * 1,
        4: lengthInUnits * 0.001,
        5: lengthInUnits * 0.01
    }
    return units.get(unitNumber, 0)

def describe_age(age):
    last_digit = age % 10

    if last_digit == 1 and age != 11:
        year_word = "год"
    elif 2 <= last_digit <= 4 and (age < 10 or age > 20):
        year_word = "года"
    else:
        year_word = "лет"

    ages = {
        20: "двадцать",
        30: "тридцать",
        40: "сорок",
        50: "пятьдесят",
        60: "шестьдесят",
        70: "семьдесят",
        80: "восемьдесят",
        90: "девяносто",
        100: "сто"
    }

    if age in ages:
        age_string = ages[age]
    else:
        tens = (age // 10) * 10
        ones = age % 10

        tens_str = ages.get(tens, "")

        ones_strings = {
            1: "один",
            2: "два",
            3: "три",
            4: "четыре",
            5: "пять",
            6: "шесть",
            7: "семь",
            8: "восемь",
            9: "девять"
        }

        ones_str = ones_strings.get(ones, "")
        age_string = f"{tens_str} {ones_str}"

    return f"{age_string} {year_word}"
