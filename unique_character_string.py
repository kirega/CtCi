"""
Is Unique: Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?
"""
def unique(sentense):
    distinct_chars =  set();
    for each in sentense:
        distinct_chars.add(each)
    if len(distinct_chars) < len(sentense):
        return False
    return True