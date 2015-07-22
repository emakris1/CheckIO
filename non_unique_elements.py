def checkio(data):
    non_unique = []

    for d in data:
        if data.count(d) > 1:
            non_unique.append(d)

    return non_unique
