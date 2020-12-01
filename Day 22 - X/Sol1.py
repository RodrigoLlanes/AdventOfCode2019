deck = [i for i in range(0, 14)]
length = len(deck)

def newStack():
    global deck
    deck.reverse()

def cut(n):
    global deck
    if(n > 0):
        aux = deck[0:n]
        deck = deck[n:] + aux
    elif(n < 0):
        aux = deck[n:]
        deck =  aux + deck[:n]

def dealWith(n):
    global deck
    global length
    nDeck = deck.copy()
    p = 0
    for i in deck:
        nDeck[p] = i
        p += n
        while(p >= length):
            p -= length
    deck = nDeck

f = open("Try.txt", "r")
print(deck)
print()
for line in f:
    if(line[:3] == "cut"):
        print("cut> " + line[3:-1])
        cut(int(line[3:]))
    elif(line[-6:-1] == "stack"):
        print("stack")
        newStack()
    else:
        print("deal> " + line[19:-1])
        dealWith(int(line[19:]))
    print(str(deck) + "\n")
#print(deck.index(2019))
