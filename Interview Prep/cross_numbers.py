import re


def solution(input_string):
    result = []
    i = 0
    while i < len(input_string):
        if input_string[i].isdigit():
            num_start = i
            while i < len(input_string) and input_string[i].isdigit():
                i += 1
            number = input_string[num_start:i]

            while i < len(input_string) and not input_string[i].isalpha():
                i += 1

            if i < len(input_string) and input_string[i].isalpha():
                first_letter = input_string[i]
                result.append(first_letter + number)
                i += 1
            else:
                result.append(number)
        else:
            result.append(input_string[i])
            i += 1

    return "".join(result)
