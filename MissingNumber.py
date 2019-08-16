# Find the missing number in a continuous array
# August 16, 2019

class case:

    def __init__(self, size, arr):
        self.size = size
        self.arr = arr

    def find_difference(self):
        testArr = sum(range(1, self.size + 1))
        return testArr - sum(self.arr)


def missing_number():
    c = int(input("Enter number of test cases: "))
    cases = []
    for i in range(c):
        size = int(input("Enter size of the array: "))
        arr = [int(x) for x in input("Enter the array with missing number: \n").split()]
        newCase = case(size, arr)
        cases.append(newCase)

    for x in cases:
        print("\nThe missing number is %d\n"%(x.find_difference()))