def checkio(num):
    numerals = [('M',  1000),
                ('CM', 900),
                ('D',  500),
                ('CD', 400),
                ('C',  100),
                ('XC', 90),
                ('L',  50),
                ('XL', 40),
                ('X',  10),
                ('IX', 9),
                ('V',  5),
                ('IV', 4),
                ('I',  1)]

    num = int(num)
    numeral_str = ''

    for numeral, value in numerals:
        count = int(num / value)
        numeral_str = numeral_str + (numeral * count)
        num = num % value

    return numeral_str
