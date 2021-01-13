from src.GraphAlgo import GraphAlgo
from src.DiGraph import DiGraph
from os import walk
import glob
import os
from pathlib import Path
import random as r


class testAlgo:
    graph = DiGraph()

    for x in range(7):
        graph.add_node(x)




    for x in graph.get_all_values():
        graph.add_edge(x.getKey(),x.getKey()+1,x.getKey()+1)
        graph.add_edge(x.getKey(),x.getKey()-1,x.getKey()+1)

    graph.add_node(8)
    graph.add_node(9)

    print("size get_mc = ", graph.get_mc())
    print("size e_size = ", graph.e_size())

    # print all in edges
    for key in graph.get_all_values():
        print("{} in -> {}".format(key.getKey(), graph.all_in_edges_of_node(key.getKey())))

    print()
    # print all out edges
    for key in graph.get_all_values():
        print("{} out -> {}".format(key.getKey(), graph.all_out_edges_of_node(key.getKey())))

    algo = GraphAlgo(graph)
    #algo.setAllTags(100)
    #algo.printAllTags()

    # print("2 -> 2 is: {}".format(algo.shortest_path(2,2)))
    # print("2 -> 7 is: {}".format(algo.shortest_path(2,7)))
    # print("2 -> 3 is: {}".format(algo.shortest_path(2,3)))
    # print("1 -> 6 is: {}".format(algo.shortest_path(1,6)))
    # print("5 -> 1 is: {}".format(algo.shortest_path(5,1)))
    # print("4 -> 0 is: {}".format(algo.shortest_path(4,0)))

    for x in graph.get_all_values():
        x.setPos((r.random()*5,r.random()*5,0.0))

    # print()
    # print(algo.save_to_json("newFile.json"))
    # print(algo.load_from_json("newFile.json"))
    # algo.save_to_json("newFile.json")
    # algo.load_from_json("newFile.json")
    #algo.load_from_json("../Graphs/Graphs_on_circle/G_10_80_1")
    # algo.save_to_json("newFile.json")
    # algo.load_from_json("newFile.json")
    # algo.load_from_json("../Graphs/Graphs_on_circle/G_10_80_1.json")
    # print(algo.plot_graph())
    # algo.load_from_json("../Graphs/Graphs_on_circle/G_100_800_1.json")
    # print(algo.plot_graph())
    # algo.load_from_json("../Graphs/Graphs_on_circle/G_1000_8000_1.json")
    # print(algo.plot_graph())
    # algo.load_from_json("../Graphs/Graphs_on_circle/G_10000_80000_1.json")
    # print(algo.plot_graph())

    # print(algo.load_from_json("../Graphs/Graphs_no_pos/G_10_80_0.json"))
    # print(algo.plot_graph())
    # print(algo.get_graph().toStringInAndOut())

    # algo.load_from_json("newFile.json")
    # print(algo.plot_graph())




    #load all json files
    my_list = []
    dir_path = os.path.dirname(os.path.realpath(__file__))
    parent = Path(dir_path).parent
    my_path = ["/Graphs/Graphs_no_pos/", "/Graphs/Graphs_on_circle/", "/Graphs/Graphs_random_pos/"]

    for x in my_path:
        string = "{}{}".format(parent, x)
        print(string)

        for root, dirs, files in os.walk(string):
            for file in files:
                print("run")
                if file.endswith('.json'):
                    path = "{}{}".format(string, file)
                    print(path)
                    my_list.append(path)
    for i in my_list:
        print(algo.load_from_json(i))
        algo.plot_graph()


    #print(graph)