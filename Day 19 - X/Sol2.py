def minX(iterations):
    x = 0
    t = 0
    yield x
    while ((t * 5) + 1 < iterations):
        x += 1
        for i in range(2): yield x
        x += 1
        for i in range(3): yield x

def maxX(iterations):
    x = 0
    t = 0
    while (t*24 < iterations):
        t += 1
        for i in range(6):
            for j in range(2): yield x
            x += 1
        yield x
        x += 1
        for i in range(5):
            for j in range(2): yield x
            x += 1
        yield x
        x += 1

img=[]
f=None
itera = 1100
mini = minX(itera)
maxi = maxX(itera)
for i in range(itera):
    m = next(mini)
    M = next(maxi)
    if(M - m >= 100) and (f == None):
        f = i
        minD = m
    for j in range(m, M+1):
        img.append([j, i])

maxD = max([i[0] for i in img])
print(maxD)
print(minD)

for i in range(981, itera):
    s=""
    #print(i)
    for j in range(432, maxD):
        if([j,i] in img):
            s+="#"
            if([j+100, i] in img):
                if([j,i+100] in img):
                    print("sol> " + str(j) + " , " + str(i))
        else: s+="."
    s += " " + str(i)
    print(s)
#432981
