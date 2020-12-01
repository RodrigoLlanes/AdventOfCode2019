import copy

f = open("Input.txt", "r")

m = [["." for i in range(7)]]

for line in f:
    aux = ["."]
    for char in line:
        if(char == "\n"): continue
        aux.append(char)
    aux.append(".")
    m.append(aux)
m.append(["." for i in range(7)])

def show(img):
    print("--M--")
    for i in range(1,6):
        s=""
        for j in range(1,6):
            s += img[i][j]
        print(s)
    print("-----")
    print()

h=[]
t=0
while True:
    show(m)
    if(m in h):
        #print(m)
        break
    h.append(copy.deepcopy(m))
    aux = copy.deepcopy(m)
    for i in range(1,6):
        for j in range(1,6):
            cont = 0
            if(m[i-1][j] == "#"): cont += 1
            if(m[i+1][j] == "#"): cont += 1
            if(m[i][j-1] == "#"): cont += 1
            if(m[i][j+1] == "#"): cont += 1
            if(m[i][j] == "."):
                if(cont == 1) or (cont == 2):
                    aux[i][j] = "#"
            else:
                if(cont != 1):
                    aux[i][j] = "."
    m = aux
    t += 1
res = 0
for i in range(1,6):
    s=""
    for j in range(1,6):
        if(m[i][j] == "#"):
            res += 2 ** ((5 * (i-1)) + (j-1))
        s += m[i][j]
    print(s)
#X ? 341643520
#X < 2080376768
    #32505887
