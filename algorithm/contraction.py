import networkx as nx
import matplotlib.pyplot as plt

def IsComplete(graph):
    n = graph.order()
    s = graph.size()
    return n * (n - 1) // 2 == s

def Convert(list):
    return {list[i][0]: (list[i][1], list[i][0])  for i in range(len(list))}

def Painting(graph):
    ord = graph.order()
    if (IsComplete(graph)):
        for i in graph.nodes():
            graph.nodes()[i]['color'] = max([i[1] for i in graph.nodes(data = 'color', default=1)]) + 1
        return ord, graph
    g1 = graph.copy()
    g2 = graph.copy()
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
    maxNum = max(graph.nodes())
    g2.add_node(maxNum + 1, color = graph.nodes()[node]['color'])
    edgesG2 = [(maxNum + 1, N) for N in list(set(nodeAllNeigh) | set(nodeNonNeighAllNeigh))]
    g2.add_edges_from(edgesG2)
    xG2 = Painting(g2)
    xG1 = Painting(g1)
    if xG1[0] < xG2[0]:
        for i in xG1[1].nodes():
            graph.nodes()[i]['color'] = xG1[1].nodes()[i]['color']
        nx.draw(graph, labels=Convert(list(graph.nodes(data = 'color', default = 1))), font_weight='bold')
        plt.suptitle("xg1")
        plt.show()
        return xG1[0], graph
    else:
        for i in xG2[1].nodes():
            if i == max(xG2[1].nodes()):
                graph.nodes()[node]['color'] = xG2[1].nodes()[i]['color']
                graph.nodes()[nodeNonNeigh]['color'] = xG2[1].nodes()[i]['color']
            else:
                graph.nodes()[i]['color'] = xG2[1].nodes()[i]['color']
        return xG2[0], graph
    