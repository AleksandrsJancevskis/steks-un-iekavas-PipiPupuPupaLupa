# python3
#Aleksandrs Jančevskis 221RDB340
from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])   

def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]

def find_mismatch(text):
    opening_brackets_stack = []
    for i, next_char in enumerate(text):
        if next_char in "([{": 
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(next_char, i + 1)) 

        if next_char in ")]}":
            # Process closing bracket, write your code here
            if len(opening_brackets_stack) == 0 or not are_matching(opening_brackets_stack[-1].char, next_char):
                print(i+1)
                return
            opening_brackets_stack.pop() 

    if len(opening_brackets_stack) != 0:
        print(opening_brackets_stack[-1].position)
    else:
        print("Success")

def main(): 
    text = input()
    find_mismatch(text)

if __name__ == "__main__":
    main()