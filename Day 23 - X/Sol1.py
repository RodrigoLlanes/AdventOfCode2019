class program():
    def __init__(self):
        f = open("Input.txt", "r")
        t = f.read()
        inputList = list(map(str,t.split(",")))

        self.inp = list(inputList)
        self.rb = 0
        self.i = 0
        self.packetW = []
        self.packetR = []
        self.inputQueue = []
    
    def checkMemory(self, n, m):
        if(m == "1"):
            if(n >= len(self.inp)):
                self.inp += ["0" for j in range((n + 1) - len(self.inp))]
            return(n)
        elif(m == "0"):
            self.checkMemory(n, "1")
            return self.checkMemory(int(self.inp[n]), "1")
        elif(m == "2"):
            self.checkMemory(n, "1")
            return self.checkMemory(self.rb + int(self.inp[n]), "1")
        else:
            print("error> Invalid memory acces code (" + str(m) + ")")

    def set(self, n, v, m):
        index = self.checkMemory(n, m)
        self.inp[index] = v

    def get(self, n, m):
        index = self.checkMemory(n, m)
        return self.inp[index]

    def enqueue(self, p):
        self.inputQueue.append(p)
        print(self.inputQueue)

    def send(self, d):
        if(len(self.packetW) < 3):
            self.packetW.append(d)
            return None
        else:
            return self.packetW
    
    def dequeue(self):
        if(len(self.packetR) > 0):
            print(self.packetR)
            a = self.packetR.pop(0)
            print(self.packetR)
            return a
        elif(len(self.inputQueue) > 0):
            print(self.inputQueue)
            self.packetR = self.inputQueue.pop(0)
            print(self.inputQueue)
            return self.packetR.pop(0)
        else:
            return -1
    
    def execute(self):
        if True:
            opCode = '{:0>2}'.format(self.inp[self.i])
            #print(self.inp[self.i])
            opCode = opCode[len(opCode) - 2:len(opCode)]
            if (opCode == "01"):
                aux = '{:0>5}'.format(self.inp[self.i])
                a = self.get(self.i + 1, aux[2])
                b = self.get(self.i + 2, aux[1])
                self.set(self.i + 3, str(int(a) + int(b)), aux[0])
                self.i+=4
            elif (opCode == "02"):
                aux = '{:0>5}'.format(self.inp[self.i])
                a = self.get(self.i + 1, aux[2])
                b = self.get(self.i + 2, aux[1])
                self.set(self.i + 3, str(int(a) * int(b)), aux[0])
                self.i+=4
            elif (opCode == "03"):
                aux = '{:0>3}'.format(self.inp[self.i])
                #inputData = str(input(">>"))
                inputData = str(self.dequeue())
                print(inputData)
                self.set(self.i + 1, inputData, aux[0])
                self.i+=2
            elif (opCode == "04"):
                aux = '{:0>3}'.format(self.inp[self.i])
                outputData = self.get(self.i + 1, aux[0])
                #print("out> " + outputData)
                da = self.send(outputData)
                if(da != None):
                    self.packetW = []
                    return da
                self.i+=2
            elif (opCode == "05"):
                aux = '{:0>4}'.format(self.inp[self.i])
                a = self.get(self.i + 1, aux[1])
                addres = self.get(self.i + 2, aux[0])
                if(a != "0"): self.i = int(addres)
                else: self.i = self.i+3
            elif (opCode == "06"):
                aux = '{:0>4}'.format(self.inp[self.i])
                a = self.get(self.i + 1, aux[1])
                addres = self.get(self.i + 2, aux[0])
                if(a == "0"): self.i = int(addres)
                else: self.i = self.i+3
            elif (opCode == "07"):
                aux = '{:0>5}'.format(self.inp[self.i])
                a = self.get(self.i + 1, aux[2])
                b = self.get(self.i + 2, aux[1])
                if(int(a) < int(b)): self.set(self.i + 3, "1", aux[0])
                else: self.set(self.i + 3, "0", aux[0])
                self.i += 4
            elif (opCode == "08"):
                aux = '{:0>5}'.format(self.inp[self.i])
                a = self.get(self.i + 1, aux[2])
                b = self.get(self.i + 2, aux[1])
                if(int(a) == int(b)): self.set(self.i + 3, "1", aux[0])
                else: self.set(self.i + 3, "0", aux[0])
                self.i += 4
            elif (opCode == "09"):
                aux = '{:0>3}'.format(self.inp[self.i])
                self.rb += int(self.get(self.i + 1, aux[0]))
                self.i+=2
            elif(opCode == "99"):
                print("fin")
                return [-2]
            else:
                print("error> " + self.inp[self.i])
                print(opCode)
            return [-1]


ended = []
programs=[]
for i in range(50):
    programs.append(program())
    programs[i].enqueue([i])
t = 0
while (True):
    #print(t)
    if(len(ended) == 50):
        print("All threads stoped")
        break
    for i in range(50):
        if(i in ended): continue
        n = programs[i].execute()
        if(int(n[0]) == -2): ended.append(i)
        elif(int(n[0]) == 255):
            print(n)
            break
        elif(int(n[0]) > -1):
            print(n)
            programs[int(n[0])].enqueue([n[1],n[2]])
    t += 1



    
