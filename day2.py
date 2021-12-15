file = open("day2input.txt", "r")
rawlines = file.readlines()
file.close()
c = 0
lines = []

for i in rawlines:
    c += 1
    lines.append(i.rstrip('\n'))
    print(c)



linelistlength = len(lines)
horizontalVal = 0
verticalVal = 0
aim = 0


for i in range(0, linelistlength):
    line = lines[i]
    value = int(line[-1])

    if line.startswith("forward"):
        horizontalVal += value
        verticalVal += value*aim
    elif line.startswith("down"):
        aim += value
    elif line.startswith("up"):
        aim -= value

    print("\nvalue = ", str(value),  "  verticalVal  = ", str(verticalVal), "  horizontalVal  = ", str(horizontalVal), "  count = ", str(i))

final = verticalVal*horizontalVal

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("\n\n\nfinal values    verticalVal  = ", str(verticalVal), "  horizontalVal  = ", str(horizontalVal), "  final  = ", str(final))
