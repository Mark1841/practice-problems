# Find Index of subarray with given sum
# August 15, 2019


class numberArray:

    def __init__(self, numbers, size, total):
        self.numbers = numbers
        self.size = size
        self.total = total
        
    def check_sub_array(self):
        start = 0
        found = False
        for end in range(1, self.size + 1):
            sub_array_sum = sum(self.numbers[start:end])
            while sub_array_sum > self.total:
                start +=1
                sub_array_sum = sum(self.numbers[start:end])       
            if sub_array_sum == self.total:
                found = True
                print("\nThe sub array is found between the following indices - %d : %d" %(start + 1, end))
                break

        if not found:
            print("\nNo sub array with the given sum was found\n")

# Main
def find_sub_array():

    cases = []    # List to store cases to check

    number_cases = int(input("Enter number of test cases: "))

    for i in range(number_cases):
        size, total = [int(x) for x in input("Enter size of the array and sum to look for: ").split()]
        number_list = [int(x) for x in input("Enter the array of numbers: ").split()]
        newArray = numberArray(number_list, size, total)
        cases.append(newArray)

    for case in cases:
        case.check_sub_array()