from src.DiGraph import DiGraph

class testDiGraph:

    graph = DiGraph()

    for x in range(7):
        graph.add_node(x)



    for key in graph.get_all_values():
        print("{} in -> {}".format(key.getKey(), graph.all_in_edges_of_node(key.getKey())))

    graph.add_edge(0,1,1)
    graph.add_edge(1,2,1)
    graph.add_edge(1,3,1)
    graph.add_edge(2,0,1)
    graph.add_edge(2,6,1)
    graph.add_edge(6,0,1)
    graph.add_edge(3,4,1)
    graph.add_edge(3,5,1)
    print()
    print("AFTER CONNECT THE GRAPH")
    print("size V= ", graph.v_size())
    print("size e_size = ", graph.e_size())
    print("size get_mc = ", graph.get_mc())
    print()
    for key in graph.get_all_values():
        print("{} in -> {}".format(key.getKey(), graph.all_in_edges_of_node(key.getKey())))
    print()
    for key in graph.get_all_values():
        print("{} out -> {}".format(key.getKey(), graph.all_out_edges_of_node(key.getKey())))

    print()
    graph.remove_node(0)
    print("after remove 0")
    # graph.remove_edge(0,1)
    # print("after remove the edge 0->1")
    print()
    for key in graph.get_all_values():
        print("{} in -> {}".format(key.getKey(), graph.all_in_edges_of_node(key.getKey())))
    print()
    for key in graph.get_all_values():
        print("{} out -> {}".format(key.getKey(), graph.all_out_edges_of_node(key.getKey())))

    print()
    print("size V= ", graph.v_size())
    print("size e_size = ", graph.e_size())
    print("size get_mc = ", graph.get_mc())
