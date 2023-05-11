import matplotlib.pyplot as plt
import networkx as nx

def IsComplete(graph):
    n = graph.order()
    s = graph.size()
    return n * (n - 1) // 2 == s

def Painting(graph, k):
    g1 = graph.copy()
    g2 = graph.copy()

    if (IsComplete(graph)):
        ord = graph.order()
        colour = 1
        for i in graph.nodes():
            if graph.nodes()[i]['color'] == colour:
                continue
            graph.nodes()[i]['color'] = colour
            colour += 1
        return ord, graph
    
    nodes = list(graph.nodes())
    for n in nodes:
        nodesNonNeigh = list(nx.non_neighbors(graph, n))
        if (len(nodesNonNeigh) != 0):
            nodeNonNeigh = nodesNonNeigh[0]
            node = n
            break
    g1.add_edge(node, nodeNonNeigh)

    nodeAllNeigh = list(nx.all_neighbors(graph, node))
    nodeNonNeighAllNeigh = list(nx.all_neighbors(graph, nodeNonNeigh))

    g2.remove_nodes_from((node, nodeNonNeigh))
    g2.add_node(k, color = 0)
    edgesG2 = [(k, N) for N in list(set(nodeAllNeigh) | set(nodeNonNeighAllNeigh)) if k != N]

    g2.add_edges_from(edgesG2)
    k += 1
    xG2 = Painting(g2, k)
    xG1 = Painting(g1, k)

    if xG1[0] <= xG2[0]:
        for i in xG1[1].nodes():
            graph.nodes()[i]['color'] = xG1[1].nodes()[i]['color']
        return xG1[0], graph
    else:
        for i in xG2[1].nodes():
            if type(i) == int:
                graph.nodes()[node]['color'] = xG2[1].nodes()[i]['color']
                graph.nodes()[nodeNonNeigh]['color'] = xG2[1].nodes()[i]['color']
            else:
                graph.nodes()[i]['color'] = xG2[1].nodes()[i]['color']
        return xG2[0], graph
    


graph = nx.Graph()

nodes = [i for i in "abcde"]

edges = [('a','b'), ('d','b'), ('c','d'), ('a', 'c')]


graph.add_nodes_from(nodes, color = 0)


graph.add_edges_from(edges)
nx.draw(graph, with_labels=True, font_weight='bold')
plt.show()
res = Painting(graph, 0)
print(res[0])
for i in res[1].nodes():
    print(res[1].nodes()[i], i)
print("\n")

