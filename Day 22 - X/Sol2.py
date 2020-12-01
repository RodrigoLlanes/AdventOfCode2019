length = 119315717514047
oPos = 2020

def newStack():
    global length
    global oPos
    oPos = length -1 - oPos

def cut(n):
    global deck
    global oPos
    oPos = oPos + n
    while(oPos < 0): oPos += length
    while(oPos >= length): oPos -= length

def dealWith(n):
    global oPos
    global length
    aux = oPos
    #print((aux%n))
    while((aux%n) != 0): aux += length
    #print(aux)
    oPos = aux // n


f = open("Input.txt", "r")
order = []

for line in f:
    order.append(line)
order.reverse()

l=[]

for it in range(101741582076661):
    print(oPos)
    if(oPos in l):
        print(it)
        break
    l.append(oPos)
    for line in order:
        #print(length)
        #print(oPos)
        #print(line)
        #print(deck)
        if(line[:3] == "cut"):
            #print("cut> " + line[3:])
            cut(int(line[3:]))
        elif(line[-6:-1] == "stack"):
            #print("stack \n")
            newStack()
        else:
            #print("deal> " + line[19:])
            dealWith(int(line[19:]))
print(oPos)

#59528120146436
#46594391815007
