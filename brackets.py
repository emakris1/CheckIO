def checkio(expression):
    open_brackets  = '{(['
    close_brackets = '})]'
    openers = []

    for e in expression:
        if e in open_brackets:
            openers.append(e)
        elif e in close_brackets:
            if not openers:
                return False
            else:
                if close_brackets.index(e) == open_brackets.index(openers[-1]):
                    openers.pop()
                else:
                    return False

    if openers:
        return False
    else:
        return True
