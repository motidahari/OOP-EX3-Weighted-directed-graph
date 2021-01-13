from DiGraph import DiGraph
from GraphAlgo import GraphAlgo
import random
import time
import networkx as nx
from GraphInterface import GraphInterface
import matplotlib.pyplot as plt


def make_graph(node_size):
    # start = time.time()
    g = DiGraph()
    for i in range(node_size):
        g.add_node(i, (random.randint(0, node_size), random.randint(0, node_size), 0))

    x = 0
    for i in range(node_size * 2):
        x += 1
        if x == node_size:
            x = 0
        g.add_edge(x, random.randint(0, node_size), (random.random() * 100))

    ga = GraphAlgo(g)
    # ga.save_to_json("/Users/yuval/PycharmProjects/OOP_EX3/src/data/ofir")
    # ga.load_from_json("/Users/yuval/PycharmProjects/OOP_EX3/src/data/ofir")

    # end = time.time()
    # Time = end - start
    # print(Time)

    # ga.plot_graph()
    return g


def check():
    """
        This file represents a simple function name tester.
        Make sure you run this example to check your naming.
        ** output: ***
        Graph: |V|=4 , |E|=5
        {0: 0: score inf, 1: 1: score inf, 2: 2: score inf, 3: 3: score inf}
        {0: 1}
        {0: 1.1, 2: 1.3, 3: 10}
        (3.4, [0, 1, 2, 3])
        [[0, 1], [2], [3]]
        (3.4, [0, 1, 2, 3])
        (inf, None)
        4.244296649514735 [1, 9, 10, 11, 7]
        20.546312400537253 [47, 46, 45, 44, 43, 42, 41, 40, 39, 15, 27, 26, 25, 17, 18, 19]
        18.197159401343114 [20, 21, 32, 31, 30, 29, 38, 14, 13, 12, 11, 9, 1, 0, 2]
        inf None
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]]
        """
    check0()
    check1()
    check2()


def checkME(graph: GraphAlgo):
    start = time.time()
    graph.connected_components()
    final1 = time.time() - start
    print("The time took for the Graph (GraphInterface) with ", len(graph.get_graph().get_all_v().keys()), "Nodes is: ",
          final1, "for connected_components")
    start = time.time()
    graph.shortest_path(0, 0)
    final2 = time.time() - start
    print("The time took for the Graph (GraphInterface) with ", len(graph.get_graph().get_all_v().keys()), "Nodes is: ",
          final2, "for shortestPath")
    start = time.time()
    graph.connected_component(0)
    final3 = time.time() - start
    print("The time took for the Graph (GraphInterface) with ", len(graph.get_graph().get_all_v().keys()), "Nodes is: ",
          final3, "for shortestPath")
    return final1, final2, final3


def checkNetworkX(graph: GraphInterface):
    G = nx.DiGraph()
    for i in graph.get_all_v().keys():
        G.add_node(i)
    for src in graph.get_all_v().keys():
        for dest, weight in graph.all_out_edges_of_node(i).items():
            G.add_edge(src, dest, weight=weight)

    start = time.time()
    nx.strongly_connected_components(G)
    final1 = time.time() - start
    print("The time took for the Graph (NetworkX) with ", len(graph.get_all_v().keys()), "Nodes is: ",
          final1, "for connected_components")
    start = time.time()
    nx.dijkstra_path(G=G, source=0, target=0)
    final2 = time.time() - start
    print("The time took for the Graph (NetworkX) with ", len(graph.get_all_v().keys()), "Nodes is: ",
          final2, "for shortestPath")
    return final1, final2


def check0():
    """
    This function tests the naming (main methods of the DiGraph class, as defined in GraphInterface.
    :return:
    """
    g = DiGraph()  # creates an empty directed graph
    for n in range(4):
        g.add_node(n)
    g.add_edge(0, 1, 1)
    g.add_edge(1, 0, 1.1)
    g.add_edge(1, 2, 1.3)
    g.add_edge(2, 3, 1.1)
    g.add_edge(1, 3, 1.9)
    g_algo = GraphAlgo(g)
    # print(g_algo.shortest_path(0, 3))
    g.remove_edge(1, 3)
    g.add_edge(1, 3, 10)
    g_algo2 = GraphAlgo(GraphInterface)
    g_algo2.load_from_json("/Users/Yuval/PycharmProjects/EX_3/Graphs/G_30000_240000_0.json")
    s1 = time.time()
    print("time taken for ")
    print(time.time() - s1)
    # print(g)  # prints the _repr_ (func output)
    # print(g.get_all_v())  # prints a dict with all the graph's vertices.
    # print(g.all_in_edges_of_node(1))
    # print(g.all_out_edges_of_node(1))
    # g_algo = GraphAlgo(g)
    #  g_algo.load_from_json("../data/A1")
    # g_algo.save_to_json("/Users/yuval/Desktop/g1.txt")
    s = time.time()
    # print(g_algo2.connected_components())
    # print(g_algo2.connected_components())
    f = time.time() - s


#  print(f)
# print(g_algo.shortest_path(0, 3))
# g_algo.connected_components()
# g_algo.load_from_json("/Users/yuval/Desktop/g.txt")
# g_algo.plot_graph()


def check1():
    """
       This function tests the naming (main methods of the GraphAlgo class, as defined in GraphAlgoInterface.
    :return:
    """
    g_algo = GraphAlgo()  # init an empty graph - for the GraphAlgo
    file = "../data/T0.json"
    g_algo.load_from_json(file)  # init a GraphAlgo from a json file
    print(g_algo.connected_components())
    print(g_algo.shortest_path(0, 3))
    print(g_algo.shortest_path(3, 1))
    g_algo.save_to_json(file + '_saved')
    g_algo.plot_graph()


def check2():
    """ This function tests the naming, basic testing over A5 json file.
      :return:
      """
    g_algo = GraphAlgo()
    file = '../data/A5'
    g_algo.load_from_json(file)
    g_algo.get_graph().remove_edge(13, 14)
    g_algo.save_to_json(file + "_edited")
    dist, path = g_algo.shortest_path(1, 7)
    print(dist, path)
    dist, path = g_algo.shortest_path(47, 19)
    print(dist, path)
    dist, path = g_algo.shortest_path(20, 2)
    print(dist, path)
    dist, path = g_algo.shortest_path(2, 20)
    print(dist, path)
    print(g_algo.connected_component(0))
    print(g_algo.connected_components())
    g_algo.plot_graph()


if __name__ == '__main__':
    # **check 10/80
    g = GraphAlgo(DiGraph())
    g.load_from_json("C:/Users/motid/PycharmProjects/OOP-EX3-Weighted-directed-graph/Graphs/Graphs_on_circle/G_10_80_1.json")
    v1 = checkNetworkX(g.get_graph())
    w1 = checkME(g)
    # g.plot_graph()
    # **check 100/800
    g.load_from_json("C:/Users/motid/PycharmProjects/OOP-EX3-Weighted-directed-graph/Graphs/Graphs_on_circle/G_100_800_1.json")
    v2 = checkNetworkX(g.get_graph())
    w2 = checkME(g)
    # g.plot_graph()
    # **check 1000/8000
    g.load_from_json("C:/Users/motid/PycharmProjects/OOP-EX3-Weighted-directed-graph/Graphs/Graphs_on_circle/G_1000_8000_1.json")
    v3 = checkNetworkX(g.get_graph())
    w3 = checkME(g)
    # g.plot_graph()
    # **check 10000/80000
    g.load_from_json("C:/Users/motid/PycharmProjects/OOP-EX3-Weighted-directed-graph/Graphs/Graphs_on_circle/G_10000_80000_1.json")
    v4 = checkNetworkX(g.get_graph())
    w4 = checkME(g)
    # g.plot_graph()
    # **check 20000/16000
    g.load_from_json("C:/Users/motid/PycharmProjects/OOP-EX3-Weighted-directed-graph/Graphs/Graphs_on_circle/G_20000_160000_1.json")
    v5 = checkNetworkX(g.get_graph())
    w5 = checkME(g)
    # g.plot_graph()
    # **check 30000/240000
    g.load_from_json("C:/Users/motid/PycharmProjects/OOP-EX3-Weighted-directed-graph/Graphs/Graphs_on_circle/G_30000_240000_1.json")
    v6 = checkNetworkX(g.get_graph())
    w6 = checkME(g)
    # g.plot_graph()
    listV0 = [v1[0], v2[0], v3[0], v4[0], v5[0], v6[0]]
    listofNodes = [10, 100, 1000, 10000, 20000, 30000]
    listV1 = [v1[1], v2[1], v3[1], v4[1], v5[1], v6[1]]
    listW0 = [w1[0], w2[0], w3[0], w4[0], w5[0], w6[0]]
    listW1 = [w1[1], w2[1], w3[1], w4[1], w5[1], w6[1]]
    listU0 = [w1[0] / 2, w2[0] / 2, w3[0] / 2, w4[0] / 2, w5[0] / 2, w6[0] / 2]
    listU1 = [w1[1] / 2, w2[1] / 2, w3[1] / 2, w4[1] / 2, w5[1] / 2, w6[1] / 2]
    listW2 = [w1[2], w2[2], w3[2], w4[2], w5[2], w6[2]]
    listU2 = [w1[2] / 2.5, w2[2] / 3, w3[2] / 3.5, w4[2] / 4.5, w5[2] / 5.5, w6[2] / 6.5]
    plt.plot(listofNodes, listW0, "r")
    plt.plot(listofNodes, listV0)
    plt.plot(listofNodes, listU0, "b")
    plt.xlabel("Nodes")
    plt.ylabel("time (in seconds)")
    plt.title("Connected Components")
    plt.legend
    plt.show()
    plt.plot(listofNodes, listW1, "r")
    plt.plot(listofNodes, listV1)
    plt.plot(listofNodes, listU1, "b")
    plt.xlabel("Nodes")
    plt.ylabel("time (in seconds)")
    plt.title("Shortest path")
    plt.show()
    plt.plot(listofNodes, listW2)
    plt.plot(listofNodes, listU2, "b")
    plt.xlabel("Nodes")
    plt.ylabel("time (in seconds)")
    plt.title("Connected Component")
    plt.show()