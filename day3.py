file = open("day3input.txt", "r")
rawlines = file.readlines()
file.close()
c = 0
lines = []

for i in rawlines:
    lines.append(i.rstrip('\n'))

# this finds the gamma rate
gammaRate = ""
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

    if zeros > ones:
        gammaRate = gammaRate + "0"
    else:
        gammaRate = gammaRate + "1"

epsilonRate = gammaRate
epsilonRate = epsilonRate.replace("0", "A")
epsilonRate = epsilonRate.replace("1", "0")
epsilonRate = epsilonRate.replace("A", "1")

intgammaRate, intepsilonRate = int(gammaRate, 2), int(epsilonRate, 2)

power = intgammaRate*intepsilonRate
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("\n\n\nfinal values   = ", gammaRate, epsilonRate, power)
