import math
calculate_distance = lambda x, y: abs(x - y)


calculate_segments = lambda a, b: math.floor(a / b)


calculate_digit_sum = lambda n: sum(map(int, str(abs(n))))


def calculate_rect_area(x1, y1, x2, y2):
    width = abs(x2 - x1)
    height = abs(y2 - y1)
    return width * height

def round_to_multiple(number, multiple):
    return round(number / multiple) * multiple