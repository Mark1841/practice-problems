# Geeks for Geeks Website
# Solved Problems

import MissingNumber
import RomeToNum
import SubArraySum


menu_items = ["Find Missing Number",
        "Roman Numerals to Integers",
        "Find sub array with given sum",
        "Exit"]

def displayMenu(items):
    """ Displays menu items submitted as list and returns selection """

    selection = 0
                    
    for i in range(0,len(items)):
        print(str(i + 1) + ". " + items[i])
                    
    while selection <1 or selection > len(items):
        selection = int(input("\nMake your selection (1 - " + str(len(items)) +")   :" ))
                    
    return selection

def main():

    end_program = False

    while not end_program:
        print("\n** Select App to Run **\n")
        selection = displayMenu(menu_items)

        if selection == 1:
            MissingNumber.missing_number()
        elif selection == 2:
            RomeToNum.roman_to_int()
        elif selection == 3:
            SubArraySum.find_sub_array()
        else:
            end_program = True

if __name__ == "__main__":
    main()

