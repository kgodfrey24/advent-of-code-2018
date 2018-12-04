

def check_strings(e1, e2):
    differences = 0
    sharedLetters = []
    for index, item in enumerate(e1):
        if e1[index] != e2[index]:
            differences = differences + 1
        else:
            sharedLetters.append(e1[index])

    if differences == 1:
        print e1 + " " + e2 + " " + ''.join(sharedLetters)
        exit()

with open("day2/input") as f:
    input = f.readlines()

for e1 in input:
    print e1
    for e2 in input:
        check_strings(e1.replace('\n',''), e2.replace('\n', ''))
