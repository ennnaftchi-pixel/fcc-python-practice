"""
FreeCodeCamp Python Practice
Exercise: PIN Extractor from Poems

Goal:
- Practice string manipulation
- Work with loops and indexing
- Handle edge cases safely

Description:
Each poem hides a numeric PIN.
For each line, the PIN digit is the length of the word
at the same index as the line number.
If the word does not exist, 0 is used.

Status: Learning exercise (not production code)
"""
def pin_extractor(poems):
    secret_codes = []
    for poem in poems:
        secret_code = ''
        lines = poem.split('\n')
        for line_index, line in enumerate(lines):
            words = line.split()
            if len(words) > line_index:
                secret_code += str(len(words[line_index]))
            else:
                secret_code += '0'
        secret_codes.append(secret_code)
    return secret_codes

poem = """Stars and the moon
shine in the sky
white and
until the end of the night"""

poem2 = 'The grass is green\nhere and there\nhoping for rain\nbefore it turns yellow'
poem3 = 'There\nonce\nwas\na\ndragon'

print(pin_extractor([poem, poem2, poem3]))