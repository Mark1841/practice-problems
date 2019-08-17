# Find out if two strings are Anagrams
# August 16, 2019

import collections

def anagram():

    cases = []

    number_cases = int(input())

    for i in range(number_cases):
        string = input()
        cases.append(string)

    for case in cases:
        first_str, second_str = case.split()
        first_str = collections.Counter(first_str)
        second_str = collections.Counter(second_str)

        if first_str == second_str:
            print("YES")
        else:
            print("NO")