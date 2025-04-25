extract_file_name = lambda file_path: file_path.split('/')[-1].split('.')[0]


def encrypt_sentence(sentence):
    odd = ""
    even = ""
    for i in range(len(sentence)):
        if i % 2 == 0:
            even += sentence[i]
        else:
            odd += sentence[i]
    return odd + even[::-1]


def check_brackets(expression):
    open_brackets = []
    for i, char in enumerate(expression):
        if char == '(':
            open_brackets.append(i)
        elif char == ')':
            if not open_brackets:
                return i + 1
            else:
                open_brackets.pop()

    if open_brackets:
        return -1
    else:
        return 0


def reverse_domain(domain):
    parts = domain.split('.')
    reversed_parts = []
    for i in range(len(parts) - 1, -1, -1):
        reversed_parts.append(parts[i])
    return '.'.join(reversed_parts)


def count_vowel_groups(word):
    vowels = "aeiouyAEIOUY"
    group_count = 0
    is_in_group = False
    for char in word:
        if char in vowels and not is_in_group:
            group_count += 1
            is_in_group = True
        elif char not in vowels:
            is_in_group = False
    return group_count
