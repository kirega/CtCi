"""
Given two strings,write a method to decide if one is a permutation of the
other.
"""
from collections import defaultdict


def check_permutation(a, b):
    b_map = defaultdict(int)
    if len(a) != len(b):
        return False
    for each in b:
        b_map[each] += 1
    for each in a:
        b_map[each] -= 1
    for ch in b_map:
        if b_map[ch] != 0:
            return False
    return True


a = 'abcddsds'
b = 'abcddsds'
print(check_permutation(a, b))
