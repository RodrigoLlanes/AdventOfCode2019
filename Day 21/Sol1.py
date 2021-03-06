from os import system, name

f = open("Input.txt", "r")
t = f.read()
inputList = list(map(str,t.split(",")))

inp = list(inputList)
rb = 0
image = []

end = False
nC = ""
def checkNext(pos, rot):
    global image
    if(rot == 0):
        if(pos[1] > 0):
            if(image[pos[1]-1][pos[0]] == "#"):
                return (True, [pos[0],pos[1]-1])
    elif(rot == 1):
        if(pos[0] < len(image[pos[1]]) - 1):
            if(image[pos[1]][pos[0]+1] == "#"):
                return (True, [pos[0]+1,pos[1]])
    elif(rot == 2):
        if(pos[1] < len(image) - 2):
            if(image[pos[1]+1][pos[0]] == "#"):
                return (True, [pos[0],pos[1]+1])
    elif(rot == 3):
        if(pos[0] > 0):
            if(image[pos[1]][pos[0]-1] == "#"):
                return (True, [pos[0]-1,pos[1]])
    return (False, None)

def changeRotation(pos, rot):
    global image
    if(rot == 0):
        if(checkNext(pos, 1)[0]): return (1, "R")
        elif(checkNext(pos, 3)[0]): return (3, "L")
        else: return None
    elif(rot == 1):
        if(checkNext(pos, 2)[0]): return (2, "R")
        elif(checkNext(pos, 0)[0]): return (0, "L")
        else: return None
    elif(rot == 2):
        if(checkNext(pos, 3)[0]): return (3, "R")
        elif(checkNext(pos, 1)[0]): return (1, "L")
        else: return None
    elif(rot == 3):
        if(checkNext(pos, 0)[0]): return (0, "R")
        elif(checkNext(pos, 2)[0]): return (2, "L")
        else: return None


def checkMemory(n, m):
    global inp
    global rb
    if(m == "1"):
        if(n >= len(inp)):
            inp += ["0" for j in range((n + 1) - len(inp))]
        return(n)
    elif(m == "0"):
        checkMemory(n, "1")
        return checkMemory(int(inp[n]), "1")
    elif(m == "2"):
        checkMemory(n, "1")
        return checkMemory(rb + int(inp[n]), "1")
    else:
        print("error> Invalid memory acces code (" + str(m) + ")")

def set(n, v, m):
    global inp
    index = checkMemory(n, m)
    inp[index] = v

def get(n, m):
    global inp
    index = checkMemory(n, m)
    return inp[index]

botPos=[]
line = ""
i=0
code=["NOT A T", "NOT C J", "OR T J", "AND D J", "WALK"]
while True:
    opCode = '{:0>2}'.format(inp[i])
    opCode = opCode[len(opCode) - 2:len(opCode)]
    if (opCode == "01"):
        aux = '{:0>5}'.format(inp[i])
        a = get(i + 1, aux[2])
        b = get(i + 2, aux[1])
        set(i + 3, str(int(a) + int(b)), aux[0])
        i+=4
    elif (opCode == "02"):
        aux = '{:0>5}'.format(inp[i])
        a = get(i + 1, aux[2])
        b = get(i + 2, aux[1])
        set(i + 3, str(int(a) * int(b)), aux[0])
        i+=4
    elif (opCode == "03"):
        aux = '{:0>3}'.format(inp[i])
        #inputData = str(input(">>"))
        if(len(code) > 0):
            if(len(code[0]) > 0):
                inputData = str(ord(code[0][0]))
                code[0] = code[0][1:]
                nC += chr(int(inputData))
            else:
                inputData = str(ord("\n"))
                print(nC)
                print()
                nC = ""
                code = code[1:]
        else:
            if(end):
                inputData = str(ord("\n"))
            else:
                inputData = str(ord(input(">>")[0]))
                end = True
        #print("inp>> " + chr(int(inputData)))
        set(i + 1, inputData, aux[0])
        i+=2
    elif (opCode == "04"):
        aux = '{:0>3}'.format(inp[i])
        outputData = get(i + 1, aux[0])
        #print("out> " + outputData)
        if(outputData == "35"):
            line += "#"
        elif(outputData == "46"):
            line += "."
        elif(outputData == "10"):
            print(line)
            line=""
        else:
            try:
                line += chr(int(outputData))
            except:
                print("Ascii error> " + outputData)
            #print("Error " + outputData)
            #break
        i+=2
    elif (opCode == "05"):
        aux = '{:0>4}'.format(inp[i])
        a = get(i + 1, aux[1])
        addres = get(i + 2, aux[0])
        if(a != "0"): i = int(addres)
        else: i = i+3
    elif (opCode == "06"):
        aux = '{:0>4}'.format(inp[i])
        a = get(i + 1, aux[1])
        addres = get(i + 2, aux[0])
        if(a == "0"): i = int(addres)
        else: i = i+3
    elif (opCode == "07"):
        aux = '{:0>5}'.format(inp[i])
        a = get(i + 1, aux[2])
        b = get(i + 2, aux[1])
        if(int(a) < int(b)): set(i + 3, "1", aux[0])
        else: set(i + 3, "0", aux[0])
        i += 4
    elif (opCode == "08"):
        aux = '{:0>5}'.format(inp[i])
        a = get(i + 1, aux[2])
        b = get(i + 2, aux[1])
        if(int(a) == int(b)): set(i + 3, "1", aux[0])
        else: set(i + 3, "0", aux[0])
        i += 4
    elif (opCode == "09"):
        aux = '{:0>3}'.format(inp[i])
        rb += int(get(i + 1, aux[0]))
        i+=2
    elif(opCode == "99"):
        print("fin")
        break
    else:
        print("error> " + inp[i])
        print(opCode)
