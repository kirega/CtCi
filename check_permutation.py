"""
Given two strings,write a method to decide if one is a permutation of the
other.
"""
def check_permutation(a, b):
    b_map = {}
    if len(a) != len(b):
        return False
    for each in b:
        
