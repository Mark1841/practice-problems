# Change Roman Numeral to Integer
# August 16, 2018

def roman_to_int():

    translate = {"I" : 1,
                 "V" : 5,
                 "X" : 10,
                 "L" : 50,
                 "C" : 100,
                 "D" : 500,
                 "M" : 1000}

    cases = []

    c = int(input("Enter number of test cases: "))
    for i in range(c):
        cases.append(input("Enter Sequence of Roman Numerals: ").upper())

    for case in cases:
        total = 0
        previous = 0
        for letter in case[::-1]:
            if translate[letter] >= previous:
                total += translate[letter]
            else:
                total -= translate[letter]
            previous = translate[letter]
        print("The integer equivalent is: %d"%(total))