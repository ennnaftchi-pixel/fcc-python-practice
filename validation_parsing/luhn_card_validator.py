def luhn_validate(card_number: str) -> str:
    """
    Validate a credit/debit card number using the Luhn algorithm.

    Args:
        card_number (str): Card number as a string. Can contain spaces or dashes.

    Returns:
        str: "VALID!" if the card number passes the Luhn check, otherwise "INVALID!".

    Example:
        >>> luhn_validate("4539 1488 0343 6467")
        'VALID!'
        >>> luhn_validate("1234 5678 9012 3456")
        'INVALID!'
    """
    # Remove spaces and dashes
    card_number = card_number.replace(" ", "").replace("-", "")
    
    # Check for invalid characters
    if not card_number.isdigit():
        return "INVALID!"
    
    digits = [int(d) for d in card_number]

    # Apply the Luhn algorithm
    for i in range(len(digits) - 2, -1, -2):
        doubled = digits[i] * 2
        if doubled > 9:
            doubled -= 9
        digits[i] = doubled

    # Sum all digits and check divisibility by 10
    return "VALID!" if sum(digits) % 10 == 0 else "INVALID!"


if __name__ == "__main__":
    sample_cards = [
        "4539 1488 0343 6467",  # valid
        "6011-1111-1111-1117",  # valid
        "1234 5678 9012 3456"   # invalid
    ]

    for card in sample_cards:
        print(f"{card}: {luhn_validate(card)}")

