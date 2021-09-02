#!/bin/python

import re

def sum_numbers(text: str) -> int:
    numbers_sum = 0

    # use regex to find matches
    # pattern is one or more digits not contained within a word boundary
    numbers_matches = re.findall("\\b\\d+\\b", text)

    # convert string matches to ints and sum them
    for match in numbers_matches:
        numbers_sum = numbers_sum + int(match)

    return numbers_sum
