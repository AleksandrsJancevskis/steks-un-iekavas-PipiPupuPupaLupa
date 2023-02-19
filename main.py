# python3
#Aleksandrs Jančevskis 221RDB340
from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])

def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{": 
            # Process opening bracket
            opening_brackets_stack.append(Bracket(next, i + 1))
  
        if next in ")]}":
            # Process closing bracket
            if len(opening_brackets_stack) == 0 or not are_matching(opening_brackets_stack[-1].char, next):
                return i + 1
            opening_brackets_stack.pop()

    if len(opening_brackets_stack) != 0:
        return opening_brackets_stack[-1].position
  
    return "Success"

def main():
    text = input() 
    if len(text) == 0:
        print("Success")
        return
 
    mismatch = find_mismatch(text)
    # Printing answer
    if mismatch == "Success":
        print("Success")
    else:
        print(mismatch) 

if __name__ == "__main__": 
    main()