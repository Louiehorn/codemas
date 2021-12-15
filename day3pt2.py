file = open("day3input.txt", "r")
rawlines = file.readlines()
file.close()
c = 0
lines = []

lines2 = []

for i in rawlines:
    lines.append(i.rstrip('\n'))
    lines2.append(i.rstrip('\n'))



for j in range(0, 12):
    zeros = 0
    ones = 0

    for i in range(0, len(lines)):
        currentLine = lines[i]
        lineDigit = currentLine[j]

        if lineDigit == "0":
            zeros += 1
        elif lineDigit == "1":
            ones += 1


    tobepopped = []
    if zeros > ones:
        for k in range(0, len(lines)):
            currentLine = lines[k]
            if currentLine[j] == "1":
                tobepopped.append(k)
    elif zeros <= ones:
        for k in range(0, len(lines)):
            currentLine = lines[k]
            if currentLine[j] == "0":
                tobepopped.append(k)

    rtobepopped = sorted(tobepopped, reverse=True)

    for l in range(len(tobepopped)):
        popindex = int(rtobepopped[l])
        lines.pop(popindex)

o2rating = lines[0]
print("lines2 at 48", len(lines2))


currentLine = ""


for m in range(0, 12):
    if len(lines2) == 1:
        break
    zeros = 0
    ones = 0

    for i in range(0, len(lines2)):
        currentLine = lines2[i]
        lineDigit = currentLine[m]

        if lineDigit == "0":
            zeros += 1
        elif lineDigit == "1":
            ones += 1

    tobepopped2 = []
    if zeros <= ones:
        for k in range(0, len(lines2)):
            currentLine = lines2[k]
            if currentLine[m] == "1":
                tobepopped2.append(k)
    elif zeros > ones:
        for k in range(0, len(lines2)):
            currentLine = lines2[k]
            if currentLine[m] == "0":
                tobepopped2.append(k)


    rtobepopped2 = sorted(tobepopped2, reverse=True)

    for n in range(len(tobepopped2)):
        popindex = int(rtobepopped2[n])
        lines2.pop(popindex)




co2rating = lines2[0]
print(co2rating)
intco2rating, into2rating = int(co2rating, 2), int(o2rating, 2)
lsrating = intco2rating*into2rating
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(o2rating, co2rating, lsrating)