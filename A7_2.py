from collections import deque

def getTableElement(nonTerminal, terminal, table):
    indexNon = 0
    indexTerm = 0
    for row in table:
        if row[0] == nonTerminal:
            indexNon = table.index(row)
    indexTerm = table[0].index(terminal)
    return table[indexNon][indexTerm]

stack = deque()
stackString = "" 
table = [
    [None, "a", "+", "*", "(", ")", "$", "-", "/", "="],
    ["S", "aW", "Missing +", "Missing *", "Missing (", "Missing )", "Missing $", "Missing -", "Missing /", "Missing ="],
    ["W", "Missing a", "Missing +", "Missing *", "Missing (", "Missing )", "Missing $", "Missing -", "Missing /", "=E"],
    ["E", "TQ", "Missing +", "+TQ","*FR","(E)","λ","-TQ","/FR", "Missing ="],
    ["Q","Missing a","+TQ","*FR","Missing (","λ","λ","-TQ","/FR", "Missing ="],
    ["T","FR","Missing +","Missing *","FR","Missing )","Missing $","Missing -","Missing /", "Missing ="],
    ["R","Missing a","λ","*FR","Missing (","λ","λ","λ","/FR", "Missing ="]
]

input = input("Enter input ending with $ to test: ")

stack.append("$")
stackString += "$"
stack.append(table[1][0])
stackString += table[1][0]
print("Push: $" + ", Push: S")
print("Stack: " + stackString + "\n")
i = 0
toRead = True
while True:
    popped = stack.pop()
    stackString = stackString[0:-1]
    if i < len(input):
        toPush = getTableElement(popped, input[i], table)
    else:
        break
    print("Pop: " + popped)
    if toRead:
        print("Read: " + input[i] + "")
        toRead = not toRead
    if (popped == input[i]):
        print("Matched with " + input[i] + "")
        toRead = not toRead
        i = i+1
        if len(stack) == 0:
            print("\n\nThe statement is accepted!")
            break
    else:
        if toPush == "λ":
            print("Go to [" +popped + ", " + input[i] + "] = " + toPush + "")
        elif toPush[0].isnumeric():
            print("Go to [" +popped + ", " + input[i] + "] = blank")
            print("\n\nThe input string is rejected." + toPush[1:])
            break
        else:
            print("Go to [" +popped + ", " + input[i] + "] = " + toPush + "")
            for element in reversed(toPush):
                print("Push: " + element, end = "\n")
                if len(toPush) > 1 and toPush.index(element) != 0:
                    print(", ", end = "")
                stack.append(element)
                stackString += element
    print("\nStack: " + stackString + "\n")