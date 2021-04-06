inp = open("inputTimetable.txt", newline="")
readData = inp.read()
print(readData)
opString = repr(readData)[1:-1]
print(opString)
op = open("outputTimetable.txt", "w", newline="")
op.write(opString)
