from collections import Counter

with open("day2/input") as f:
    content = f.readlines()

twos = 0
threes = 0
for e in content:
    c = Counter(e).values()
    print c
    if 2 in c:
        twos = twos + 1
    if 3 in c:
        threes = threes + 1

print twos
print threes

print twos * threes

#runningTotal = 0
#for row in content:
#    runningTotal = runningTotal + int(row)
