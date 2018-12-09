input = open("day5/input").read().strip()

def is_match(a, b):
    return a != b and (a == b.lower() or a == b.upper())

stack = []

for char in input:
    if not stack:
        stack.append(char)
    elif is_match(char, stack[-1]):
        stack.pop()
    else:
        stack.append(char)

print stack
print len(stack)