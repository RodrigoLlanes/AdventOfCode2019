f = open("Input.txt", "r")
t = f.read()
inputList = list(map(str,t.split(",")))

inp = list(inputList)
i=0
a=0
b=0
while True:
    if (len(str(inp[i])) == 1):
        if (inp[i] == "1"):
            inp[int(inp[i+3])] = str(int(inp[int(inp[i+1])]) + int(inp[int(inp[i+2])]))
            i+=4
        elif (inp[i] == "2"):
            inp[int(inp[i+3])] = str(int(inp[int(inp[i+1])]) * int(inp[int(inp[i+2])]))
            i+=4
        elif (inp[i] == "3"):
            inp[int(inp[i+1])] = str(input(">>"))
            i+=2
        elif (inp[i] == "4"):
            print("out> " + str(inp[int(inp[i+1])]))
            i+=2
        elif (inp[i] == "5"):
            if(int(inp[int(inp[i+1])]) != 0): i = int(inp[i+2])
            else: i+=3
        elif (inp[i] == "6"):
            if(int(inp[int(inp[i+1])]) == 0): i = int(inp[i+2])
            else: i+=3
        elif (inp[i] == "7"):
            if(int(inp[int(inp[i+1])]) < int(inp[int(inp[i+2])])): inp[int(inp[i+3])] = 1
            else: inp[int(inp[i+3])] = 0
            i+=4
        elif (inp[i] == "8"):
            if(int(inp[int(inp[i+1])]) == int(inp[int(inp[i+2])])): inp[int(inp[i+3])] = 1
            else: inp[int(inp[i+3])] = 0
            i+=4
        else: print("error " + inp[i])
    else:
        if (inp[i][len(inp[i])-2: len(inp[i])] == "01"):
            aux = '{:0>5}'.format(inp[i])
            if(aux[2] == "0"): a = inp[int(inp[i+1])]
            else: a = inp[i+1]
            if(aux[1] == "0"): b = inp[int(inp[i+2])]
            else: b = inp[i+2]
            if(aux[0] == "0"): inp[int(inp[i+3])] = str(int(a) + int(b))
            else: inp[i+3] = str(int(a) + int(b))
            i+=4
        elif (inp[i][len(inp[i])-2: len(inp[i])] == "02"):
            aux = '{:0>5}'.format(inp[i])
            if(aux[2] == "0"): a = inp[int(inp[i+1])]
            else: a = inp[i+1]
            if(aux[1] == "0"): b = inp[int(inp[i+2])]
            else: b = inp[i+2]
            if(aux[0] == "0"): inp[int(inp[i+3])] = str(int(a) * int(b))
            else: inp[i+3] = str(int(a) * int(b))
            i+=4
        elif (inp[i][len(str(inp[i]))-2: len(inp[i])] == "03"):
            inp[i+1] = str(input(">>"))
            i+=2
        elif (inp[i][len(str(inp[i]))-2: len(inp[i])] == "04"):
            print(inp[i+1])
            i+=2
        elif (inp[i][len(inp[i])-2: len(inp[i])] == "05"):
            aux = '{:0>4}'.format(inp[i])
            if(aux[1] == "0"): a = inp[int(inp[i+1])]
            else: a = int(inp[i+1])
            if(aux[0] == "0"):
                if(int(a) != 0): i = int(inp[int(inp[i+2])])
                else: i = i+3
            else:
                if(int(a) != 0): i = int(inp[i+2])
                else: i = i+3
        elif (inp[i][len(inp[i])-2: len(inp[i])] == "06"):
            aux = '{:0>4}'.format(inp[i])
            if(aux[1] == "0"): a = inp[int(inp[i+1])]
            else: a = inp[i+1]
            if(aux[0] == "0"):
                if(int(a) == 0): i = int(inp[int(inp[i+2])])
                else: i = i+3
            else:
                if(int(a) == 0): i = int(inp[i+2])
                else: i = i+3
        elif (inp[i][len(inp[i])-2: len(inp[i])] == "07"):
            aux = '{:0>5}'.format(inp[i])
            if(aux[2] == "0"): a = inp[int(inp[i+1])]
            else: a = inp[i+1]
            if(aux[1] == "0"): b = inp[int(inp[i+2])]
            else: b = inp[i+2]
            if(aux[0] == "0"):
                if(int(a) < int(b)): inp[int(inp[i+3])] = 1
                else: inp[int(inp[i+3])] = 0
            else:
                if(int(a) < int(b)): inp[i+3] = 1
                else: inp[i+3] = 0
            i += 4
        elif (inp[i][len(inp[i])-2: len(inp[i])] == "08"):
            aux = '{:0>5}'.format(inp[i])
            if(aux[2] == "0"): a = inp[int(inp[i+1])]
            else: a = inp[i+1]
            if(aux[1] == "0"): b = inp[int(inp[i+2])]
            else: b = inp[i+2]
            if(aux[0] == "0"):
                if(int(a) == int(b)): inp[int(inp[i+3])] = 1
                else: inp[int(inp[i+3])] = 0
            else:
                if(int(a) == int(b)): inp[i+3] = 1
                else: inp[i+3] = 0
            i += 4
        elif(inp[i] == "99"):
            print("fin")
            break
        else: print("error " + inp[i])
