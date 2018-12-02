with open("day1/input") as f:
    content = f.readlines()

runningTotal = 0
for row in content:
    runningTotal = runningTotal + int(row)

print runningTotal