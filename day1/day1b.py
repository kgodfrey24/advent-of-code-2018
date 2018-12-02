with open("day1/input") as f:
    content = f.readlines()

freq = set([0])
i = 1;
currentFreq = 0
while True:
    for row in content:
        currentFreq = currentFreq + int(row)
        freq.add(currentFreq) 
        i = i + 1
        if len(freq) != i:
            print "done"
            print currentFreq
            exit()


 