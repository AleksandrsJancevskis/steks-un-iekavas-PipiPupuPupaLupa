# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code her
            opening_brackets_stack.append((next, i + 1))

        if next in ")]}":
            # Process closing bracket, write your code here
            if len(opening_brackets_stack)==0 or not(opening_brackets_stack.top().are_matching(next)):
                print(i+1)
            opening_brackets_stack.pop()


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    if opening_brackets_stack:
        opening_brackets_stack.top().position
    else:
        print("Success")


if __name__ == "__main__":
    main()
