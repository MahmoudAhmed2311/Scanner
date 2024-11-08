import re

token_specification = [
    ('COMMENT',     r'//[^\n]*|/\*[\s\S]*?\*/'),
    ('KEYWORD',     r'\b(if|else|while|for|return|int|float|char|void)\b'),
    ('IDENTIFIER',  r'\b[ء-يa-zA-Z_][ء-يa-zA-Z_0-9]*\b'),
    ('OPERATOR',    r'[+\-*/%=<>!&|]'),
    ('NUMERIC_CONST', r'\b\d+(\.\d*)?\b'),
    ('CHAR_CONST',  r"'(\\.|[^\\'])'"),
    ('SPECIAL_CHAR', r'[.,;:{}()[\]]'),
    ('WHITESPACE',  r'[ \t]+'),
    ('NEWLINE',     r'\n'),
]

token_regex = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in token_specification)

def scanner(code):
    line_num = 1
    tokens = []
    for match in re.finditer(token_regex, code):
        kind = match.lastgroup
        value = match.group()
        if kind == 'WHITESPACE':

            continue
        elif kind == 'NEWLINE':
            line_num += 1
        elif kind == 'MISMATCH':
            raise RuntimeError(f'Unexpected character {value} at line {line_num}')
        else:

            tokens.append((kind, value, line_num))
    return tokens


code = input("Please enter your syntax: ")


try:
    tokens = scanner(code)

    for token in tokens:
        if token[0] == "COMMENT":
            print(f'Type: COMMENT , Value: "{token[1]}", Line: {token[2]}')
        else:
            print(f'Type: {token[0]}, Value: "{token[1]}", Line: {token[2]}')
except RuntimeError as e:
    print(e)
