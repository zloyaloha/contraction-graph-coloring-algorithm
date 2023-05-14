import networkx as nx

def IsComplete(graph):
    n = graph.order()
    s = graph.size()
    return n * (n - 1) // 2 == s

def Painting(graph, order):
    g1 = graph.copy()
    g2 = graph.copy()
    ord = graph.order()
    if (IsComplete(graph)):
        for i in graph.nodes():
            if graph.nodes()[i]['color'] == max([i[1] for i in graph.nodes(data = 'color', default=1)]) + 1:
                continue
            graph.nodes()[i]['color'] = max([i[1] for i in graph.nodes(data = 'color', default=1)]) + 1
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
    g2.add_node(max(graph.nodes()) + 1, color = graph.nodes()[node]['color'])
    edgesG2 = [(max(graph.nodes()) + 1, N) for N in list(set(nodeAllNeigh) | set(nodeNonNeighAllNeigh))]
    g2.add_edges_from(edgesG2)
    xG2 = Painting(g2, order)
    xG1 = Painting(g1, order)
    if xG1[0] < xG2[0]:
        for i in xG1[1].nodes():
            graph.nodes()[i]['color'] = xG1[1].nodes()[i]['color']
        return xG1[0], graph
    else:
        for i in xG2[1].nodes():
            if i > order:
                graph.nodes()[node]['color'] = xG2[1].nodes()[i]['color']
                graph.nodes()[nodeNonNeigh]['color'] = xG2[1].nodes()[i]['color']
            else:
                graph.nodes()[i]['color'] = xG2[1].nodes()[i]['color']
        return xG2[0], graph
    