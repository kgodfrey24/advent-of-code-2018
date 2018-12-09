import string

input = open("day5/input").read().strip()

def is_match(a, b):
    return a != b and (a == b.lower() or a == b.upper())

shortest_result = 9999999
for letter_of_alphabet in string.ascii_lowercase:
    stack = []

    for char in input:
        if char.lower() == letter_of_alphabet:
            continue
        elif not stack:
            stack.append(char)
        elif is_match(char, stack[-1]):
            stack.pop()
        else:
            stack.append(char)

    if len(stack) < shortest_result:
        shortest_result = len(stack)    

print shortest_result