import sys
import copy
import math
from pprint import pprint

# Nodo de un grafo
class Node():
    def __init__(self, name, aristas=[]):
        self.aristas = {}
        self.name = name
        for a, d in aristas:
            self.add(a, d)

    # Añade una arista (Nodo objetivo, peso arista)
    def add(self, arista, distancia):
        if arista in self.aristas:
            self.aristas[arista] = min(self.aristas[arista], distancia)
        elif self.name != arista:
            self.aristas[arista] = distancia

    #Elimina una arista
    def delete(self, arista):
        if arista in self.aristas:
            del self.aristas[arista]

    #Calcula la longitud de una arista
    def dist(self, arista):
        if arista in self.aristas:
            return self.aristas[arista]
        else:
            return -1


class Graph():
    def __init__(self, nodes={}):
        self.nodes = nodes

    def add_node(self, node, adyacentes=[]):
        if node not in self.nodes:
            self.nodes[node] = Node(node, adyacentes)
        for n, dist in adyacentes:
            self.nodes[n].add(node, dist)
    
    def del_node(self, node):
        if node not in self.nodes:
            return
        for k, v in list(self.nodes[node].aristas.items()):
            for k1, v1 in list(self.nodes[node].aristas.items()):
                if k1 != k:
                    self.nodes[k].add(k1, self.nodes[k].dist(node) +\
                                      self.nodes[node].dist(k1))
            self.nodes[k].delete(node)
        del self.nodes[node]

    def from_vaultMap(self, pos, v_map):
        ady = self._nodos_adyacentes(pos, v_map)
        visited = ["@"]
        for n, _, _ in ady:
            self.add_node(n)
        self.add_node("@", [(n, d) for n, d, _ in ady])
        while len(ady) > 0:
            node, dist, n_pos = ady[0]
            if node not in visited:
                ady_n = self._nodos_adyacentes(n_pos, v_map)
                for n, _, _ in ady_n:
                    self.add_node(n)
                self.add_node(node, [(n, d) for n, d, _ in ady_n])
                visited.append(node)
                ady += ady_n
            ady.pop(0)
        return self.nodes

    def find_keys(self, n_keys, actual="@", prev=None):
        next_step = None
        if prev != None:
            self.del_node(prev)
        for n, d in self.nodes[actual].aristas.items():
            if n.islower():
                if next_step == None or d < next_step[1]:
                    next_step = (n, d)
        n_keys -= 1
        self.del_node(next_step[0].upper())
        if n_keys == 0:
            return next_step[1]
        else:
            return next_step[1] + self.find_keys(n_keys, next_step[0], actual)

        
    def _nodos_adyacentes(self, pos, v_map):
        return self._nodos_adyacentes_rec([], pos, v_map)
    

    def _nodos_adyacentes_rec(self, visited, n_pos, v_map, dist=0):
        ret = []
        visited.append(n_pos)
        for x, pos in self._adyacentes(n_pos, v_map):
            if pos not in visited:
                if x.isalpha():
                    ret.append((x, dist + 1, pos))
                elif x == ".":
                    ret += self._nodos_adyacentes_rec(visited, pos, v_map, dist + 1)
        return ret
    
    
    def _pos_adyacentes(self, pos):
        yield (pos[0] + 1, pos[1])
        yield (pos[0] - 1, pos[1])
        yield (pos[0], pos[1] + 1)
        yield (pos[0], pos[1] - 1)
        

    def _adyacentes(self, pos, v_map):
        for i in (self._pos_adyacentes(pos)):
            yield (v_map[i[1]][i[0]],i)


def find_keys_2(n_keys, graph, actual="@", path=""):
    sol = []
    path += actual
    for n, d in graph.nodes[actual].aristas.items():
        if n.islower():
            new_keys = n_keys - 1
            new_graph = copy.deepcopy(graph)
            new_graph.del_node(n.upper())
            new_graph.del_node(actual)
            if new_keys == 0:
                sol.append(d)
            else:
                sol.append(d + find_keys_2(new_keys, new_graph, n, path))
    print(path)
    return min(sol)
    

f = open("Input.txt", "r")

vaultMap = []
startPos = []
nKeys = 0

#Lectura del mapa
y = -1
for i in f:
    y+=1
    x = -1
    line = []
    for j in i:
        x += 1
        if(j != "\n"):
            line.append(j)
        if(j == "@"):
            line[-1] = chr(ord("@"))
            startPos = [x,y]
        if(j.isalpha()):
            if(j.islower()):
                nKeys += 1
    vaultMap.append(line)
g = Graph()
for k, v in g.from_vaultMap(startPos, vaultMap).items():
    pprint((k, v.aristas))
print("Grafo generado")
print(find_keys_2(nKeys, g))

