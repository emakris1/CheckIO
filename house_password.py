def checkio(data):
    symbol_count = 0
    has_digit = False
    has_lower = False
    has_upper = False
    strong = False

    for d in data:
        symbol_count = symbol_count + 1
        if d.isdigit():
            has_digit = True
        if d.islower():
            has_lower = True
        if d.isupper():
            has_upper = True
        if symbol_count >= 10 and has_digit and has_lower and has_upper:
            strong = True
            break

    return strong
