import networkx as nx
import numpy as np
from sys import argv
from contraction import Painting


file = argv[1]
colorsList = ["green", "red", "blue", "cyan", "pink", "yellow", "white", "black", "dark-green", "dark-red ", "dark-blue", "dark-cyan", "dark-pink", "dark-yellow"]


with open(file, "r+") as f:
    size = int(f.readline())
    matrix = []
    for i in range(size):
        line = f.readline().split()
        line = [int(i) for i in line]
        matrix.append(line)
    numpyMatrix = np.array(matrix)
    graphy = nx.from_numpy_array(numpyMatrix)
    nx.set_node_attributes(graphy, 0, "color")
    res = Painting(graphy)
    f.write("<Vertex_Colors>\n")
    for line in res[1].nodes(data = 'color', default=1):
        copyLine = " ".join((str(line[0]), colorsList[int(line[1])],))
        f.write(copyLine + "\n")
