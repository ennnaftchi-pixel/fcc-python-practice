"""
FreeCodeCamp Python Practice
Exercise: ISBN Validator

Concepts practiced:
- String manipulation and slicing
- Loops and arithmetic
- Conditional logic
- Exception handling
- Functions with helper functions

Description:
This script validates ISBN-10 and ISBN-13 codes. It checks:
- Correct length
- Valid characters
- Correct check digit according to ISBN rules

Status: Learning exercise
"""

def validate_isbn(isbn, length):
    if len(isbn) != length:
        print(f'ISBN-{length} code should be {length} digits long.')
        return

    main_digits = isbn[:-1]
    given_check_digit = isbn[-1]

    try:
        main_digits_list = [int(digit) for digit in main_digits]
    except ValueError:
        print('Invalid character was found.')
        return

    if length == 10:
        expected_check_digit = calculate_check_digit_10(main_digits_list)
    else:
        expected_check_digit = calculate_check_digit_13(main_digits_list)

    if given_check_digit == expected_check_digit:
        print('Valid ISBN Code.')
    else:
        print('Invalid ISBN Code.')


def calculate_check_digit_10(main_digits_list):
    digits_sum = 0
    for index, digit in enumerate(main_digits_list):
        digits_sum += digit * (10 - index)

    result = 11 - digits_sum % 11

    if result == 11:
        return '0'
    elif result == 10:
        return 'X'
    else:
        return str(result)


def calculate_check_digit_13(main_digits_list):
    digits_sum = 0
    for index, digit in enumerate(main_digits_list):
        if index % 2 == 0:
            digits_sum += digit
        else:
            digits_sum += digit * 3

    result = 10 - digits_sum % 10

    if result == 10:
        return '0'
    else:
        return str(result)


def main():
    user_input = input('Enter ISBN and length: ')

    try:
        values = user_input.split(',')
        isbn = values[0]
        length = values[1]
    except IndexError:
        print('Enter comma-separated values.')
        return

    try:
        length = int(length)
    except ValueError:
        print('Length must be a number.')
        return

    if length != 10 and length != 13:
        print('Length should be 10 or 13.')
        return

    validate_isbn(isbn, length)

if __name__ == "__main__":
    main()
    
