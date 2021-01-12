from GraphAlgo import GraphAlgo
from DiGraph import DiGraph
from os import walk
import glob
import os

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

    print("2 -> 2 is: {}".format(algo.shortest_path(2,2)))
    print("2 -> 7 is: {}".format(algo.shortest_path(2,7)))
    print("2 -> 3 is: {}".format(algo.shortest_path(2,3)))
    print("1 -> 6 is: {}".format(algo.shortest_path(1,6)))
    print("5 -> 1 is: {}".format(algo.shortest_path(5,1)))
    print("4 -> 0 is: {}".format(algo.shortest_path(4,0)))

    for x in graph.get_all_values():
        x.setPos((0.03454355435435,0.0443543543543,0.0))

    # graph.toString()
    print()
    print(algo.save_to_json("newFile.json"))
    print(algo.load_from_json("newFile.json"))
    print(algo.DFS(1,graph))


    # graph.toString()
   #print(glob.glob("gameClient\\Graphs_random_pos\\*.json")


    print(algo.maybenewSCC())
    my_list = []

    my_path = ["C:/Users/motid/PycharmProjects/pythonProject1/src/gameClient/Graphs_no_pos/","C:/Users/motid/PycharmProjects/pythonProject1/src/gameClient/Graphs_on_circle/","C:/Users/motid/PycharmProjects/pythonProject1/src/gameClient/Graphs_random_pos/"]
    for x in my_path:
        for root, dirs, files in os.walk(x):
            for file in files:
                if file.endswith('.json'):
                    string = "{}{}".format(x,file)
                    #print("string = ",string)
                    my_list.append(string)
                    print(string)

    for i in my_list:
        print(algo.load_from_json(i))

    #print(graph)