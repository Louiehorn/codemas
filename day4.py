file = open("day4input.txt", "r")
strings = file.readlines()
file.close()

numsCalled = [int(i) for i in strings[0].split(',')]  # this creates a list of the numbers to be called
print(numsCalled)



Boards = []
for index in range(2, len(strings), 6):
    boardStringList = []
    for i in range(5):
        boardStringList.append()