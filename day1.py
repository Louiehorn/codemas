file = open("day1input.txt", "r")
lines = file.readlines()
file.close()

linelistlength = len(lines)
prev = int(lines[0])
count = 0
windows = []

for i in range(0, linelistlength - 2):
    thisWindow = int(lines[i]) + int(lines[i+1]) + int(lines[i+2])
    windows.append(thisWindow)


for i in range(1, len(windows)):
    current = int(windows[i])

    if current > prev:
        count += 1
        swapped = True
    else:
        swapped = False
    print("\n\n\nvalue = ", str(windows[i]), "  iteration = ", str(i), "  prev = ", str(prev), "  curr = ", str(current), "  swapped =", str(swapped))

    prev = current

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("\n\n\nfinal value  = ", str(count))
