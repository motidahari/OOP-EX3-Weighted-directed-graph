import json as Js
import math
from typing import List
import matplotlib.pyplot as plt
from DiGraph import DiGraph
from GraphInterface import GraphInterface
from src.GraphAlgoInterface import GraphAlgoInterface
import random as r


class GraphAlgo(GraphAlgoInterface):
    """
    GraphAlgo class implements GraphAlgoInterface methods to perform all sort of manipulations on a Directed weighted
    graph of DiGraph object. The different algorithms performed on the graph include finding the shortest path usnig
    Dijkstra's algorithm and finding how many SCCs exist in the graph using Tarjan's algorithm.
    """

    def __init__(self, graph=None):
        """
            GraphAlgo implements the interface GraphAlgoInterface. The different methods to be performed on a directed
            weighted graph such as shortest path from two given vertices (Dijkstra's algorithm), determine how many SCC (strongly connected
            component) exists in the graph. exploration of the graph with BFS algorithm. Other methods such as save/load a graph into a json file format,
            As well as a method for a user GUI.
            """
        self.tags = {}
        self.VISITED = 1
        self.NOT_VISITED = 0
        self.g = None if graph is None else graph
        self.mc = 0 if graph is None else graph.get_mc()
        self.nodeSize = 0 if graph is None else graph.v_size()
        self.edgeSize = 0 if graph is None else graph.e_size()
        self.transposed_graph = None if graph is None else self.createTransposedGraph(graph)
        self.positive_infnity = float('inf')
        self.negative_infnity = float('-inf')

    def createTransposedGraph(self, graph) -> DiGraph:
        """
        Generates a reversed version of the given graph by iterating over the graph and creating a new DiGraph with the opposite direction of the arrows.
        """
        if self.g is None:
            return
        new_graph = DiGraph()
        for x in self.g.get_all_values():
            new_graph.add_node(x.getKey())
        for x in self.g.get_all_values():
            for e in self.g.all_out_edges_of_node(x.getKey()):
                new_graph.add_edge(e, x.getKey(), self.g.all_out_edges_of_node(x.getKey())[e])
        return new_graph

    def setAllTags(self, t: float):
        """
        Sets al nodes' tags value to a given integer number t
        @param t - value of the tag to set.
        """
        if self.g is None:
            return
        for x in self.g.get_all_values():
            self.tags[x] = t

    def getAllTags(self):
        return self.tags

    def setAllWeightAndInfo(self, t: float):
        """
        Sets the weight and info of all vertices in the graph to 't' and and empty string.
        :param t: the weight to set.
        """
        if self.g is None:
            return
        for x in self.g.get_all_values():
            x.setWeight(t)
            x.setInfo("")

    def printAllTags(self):
        if self.g is None:
            return
        for x in self.tags.items():
            print(x)

    def get_graph(self) -> GraphInterface:
        """
        :return: the directed graph on which the algorithm works on.
        """
        if self.g is None:
            return None
        return self.g

    def get_transposed_graph(self) -> GraphInterface:
        """
        :return: the transposed directed graph on which the algorithm works on.
        """
        if self.transposed_graph is None:
            return None
        return self.transposed_graph

    def load_from_json(self, file_name: str) -> bool:
        """
        Loads a graph from a json file.
        @param file_name: The path to the json file
        @returns True if the loading was successful, False o.w.
        """
        try:
            new_graph = DiGraph()  # creating a new DiGraph
            with open(file_name, 'r') as reader:  # reading from a file in 'r' mode
                json_graph = Js.load(reader)
                reader.close()
                edges = json_graph["Edges"]  # accessing the position of the key "Edges" being a list
                nodes = json_graph["Nodes"]  # accessing the position of the key "Nodes" being a list of node objects
                for x in nodes:
                    pos = None
                    if 'pos' in x:  # if the value of x contains a key for 'pos'
                        posString = x["pos"].split(",")  # splitting the string of pos
                        pos = (float(posString[0]), float(posString[1]), float(posString[2]))  # assigning the information on the string into a pos tuple
                    new_graph.add_node(int(x["id"]), pos)  # adding the node to the graph with the given value of 'id' and the pos
                for x in edges:
                    new_graph.add_edge(int(x["src"]), int(x["dest"]), float(x["w"])) # adding the edges
                self.g = new_graph
                return True
        except:
            # raise FileExistsError
            return False

    def save_to_json(self, file_name: str) -> bool:
        """
        Saves the graph in JSON format to a file
        @param file_name: The path to the out file
        @return: True if the save was successful, Flase o.w.
        """
        if self.g is None:
            return False
        my_dict = {}
        my_dict["Edges"] = []
        my_dict["Nodes"] = []
        for x in self.g.get_all_values():
            node_dict = {}
            node_dict["id"] = x.getKey()
            if len(x.getPosAsString()) > 0:
                node_dict["pos"] = x.getPosAsString()
            my_dict["Nodes"].append(node_dict)
            for e in self.g.all_out_edges_of_node(x.getKey()):
                edges_dict = {}
                edges_dict["src"] = x.getKey()
                edges_dict["w"] = self.g.all_out_edges_of_node(x.getKey())[e]
                edges_dict["dest"] = e
                my_dict["Edges"].append(edges_dict)
        try:
            with open(file_name, 'w') as writer:
                writer.write(Js.dumps(my_dict))
                return True
        except:
            # raise FileExistsError
            return False
        finally:
            writer.close()

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        """
       Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm.
       after checking for both id1 and id2 exist in the graph and they're not equal we initially reset all vertices weight and info to -1.
       iterating over the node neighbours and calculating the weight of the different paths, on the occasion that the last known distance
       (the sum of weight) is larger than the current known distance we update it to the current weight, and thread the previous info to the current node info.
        @param id1: The start node id
        @param id2: The end node id
        @return: a tuple of the distance of the path, and the path as a list.


        Examples of paths:
#        >>> g_algo.addEdge(0,1,1) 0----->1
#        >>> g_algo.addEdge(1,2,4) 1---->2
#        >>> g_algo.shortestPath(0,1)
#        (1, [0, 1]) given there's one edge connecting them
#        >>> g_algo.shortestPath(0,2)
#        (5, [0, 1, 2]) 5 being the total weight of the edges and the list as the path.

        """
        if self.g is None:  # in case the graph is none
            return (-1,[])  # returns a tuple with -1 and empty list.
        if id1 in self.g.get_v_keys() and id1 == id2: # if id1=id2 the result is a tuple with 0 and a list containing
            # only the node id
            my_tuple = (0, [self.g.get_all_v()[id1].getKey()])
            return my_tuple
        if id1 not in self.g.get_all_v().keys() or id2 not in self.g.get_all_v().keys():  # if one of the given ids doesn't exist in the graph dictionary
            my_tuple = (-1, [])
            return my_tuple
        queue = [id1]  # if neither of the above cases happened adds id1 to a queue
        self.setAllWeightAndInfo(-1)  # resets all nodes weight and info to -1
        self.g.get_all_v()[id1].setWeight(0)  # sets the weight of id1 to 0
        info = "{}".format(id1)
        self.g.get_all_v()[id1].setInfo(info)
        while queue:  # while the queue isn't empty
            node = queue.pop(0)  # pops the first item in the queue
            for x in self.g.all_out_edges_of_node(node).keys():  # iterating over node neighbours
                if self.g.get_all_v()[x].getWeight() == -1 or self.g.get_all_v()[x].getWeight() > self.g.get_all_v()[
                    node].getWeight() + self.g.all_out_edges_of_node(node)[x]:
                    self.g.get_all_v()[x].setWeight(
                        self.g.get_all_v()[node].getWeight() + self.g.all_out_edges_of_node(node)[x]) # updating the current vertex and its predecessor weight.
                    queue.append(x)
                    info = "{},{}".format(self.g.get_all_v()[node].getInfo(), x)  # formating the info of the current vertex x
                    self.g.get_all_v()[x].setInfo(info)
        if self.g.get_all_v()[id2].getWeight() == -1:  # if we didn't visit that node yet
            my_tuple = (math.inf, [])  # we return a tuple with the distance of infinity and an empty list.
            return my_tuple
        else:  # there's a path
            my_list = []
            for x in self.g.get_all_v()[id2].getInfo().split(','):  # iterating over the array of the info string after splitting it
                my_list.append(int(x))
            my_tuple = (self.g.get_all_v()[id2].getWeight(), my_list) # a tuple with the weight of id2 and the list containing the path.
            return my_tuple

    def connected_component(self, id1: int) -> list:
        """
        Finds the Strongly Connected Component(SCC) that node id1 is a part of.
        @param id1: The node id
        @return: The list of nodes in the SCC
        """
        if self.g is None or id1 not in self.g.get_all_v():
            return []
        my_list = self.connected_components()  # defining my_list as a list to hold all the lists of SCC in the graph.
        if my_list:
            for x in my_list:  # iterating over the list
                if id1 in x:  # in case the desired id exist in x (list)
                    return x  # returns the list containing id1 in the SCC
        return []  # in case id1 wasn't found in neither of the lists returns an empty list.

    def connected_components(self) -> List[list]:
        """
        Finds all the Strongly Connected Component(SCC) in the graph.
        @return: The list all SCC
        """
        if self.g is not None:
            result = []
            p = {}
            l = {}
            f = {}
            my_list = []
            i = 0
            keys = self.g.get_all_v().keys()
            for id in keys:  # iterates over the vertices IDs'
                if id not in f:  # in case the current id doesn't exist in the dictionary of known SCC
                    queue = [id]
                    while len(queue) > 0:  # while the queue isn't empty
                        vertex = queue[-1]
                        if vertex not in p:  # in case the current id doesn't exist in the dictionary of p
                            i = i + 1
                            p[vertex] = i
                        done = 1
                        niById = self.g.all_out_edges_of_node(vertex)
                        for w in niById:  # iteration over the neighbors of the current vertex
                            if w not in p:  # in case the current id doesn't exist in the dictionary of q
                                queue.append(w)
                                done = 0
                                break
                        if done == 1:
                            l[vertex] = p[vertex]
                            for w in niById:  # iteration over the neighbors of the current vertex
                                if w not in f:
                                    if p[w] <= p[vertex]:  # comparing between the weight of vertices
                                        l[vertex] = min([l[vertex], p[w]])
                                    else:
                                        l[vertex] = min([l[vertex], l[w]])
                            queue.pop()
                            if l[vertex] != p[vertex]:
                                my_list.append(vertex)
                            else:
                                f[vertex] = True  # marking the vertex as true being a part of the SCC
                                scc = [vertex]
                                while my_list and p[my_list[-1]] > p[vertex]:  # iterating over the list while it's
                                    # not empty & the last value in p larger than p[vertex] adds the vertices to the
                                    # SCC dictionary
                                    k = my_list.pop()
                                    f[k] = True
                                    scc.append(k)
                                result.append(scc)  # adds the list of SCC to the result list.
            self.components = result
            return result

    def plot_graph(self) -> None:
        """
        Plots the graph, if the nodes have a position, the nodes will be placed there.
        Otherwise, they will be placed in a random position.
        @return: None
        """
        list_X = []
        list_Y = []
        for x in self.g.get_all_v().keys():
            for e in self.g.all_out_edges_of_node(x).keys():
                # print(self.g.get_all_v()[x].getPosAsString())
                listOfVector = self.splitPos(self.g.get_all_v()[x].getPosAsString())
                if listOfVector is not None:
                    list_X.append(listOfVector[0])
                    list_Y.append(listOfVector[1])

                listOfEdgesByX = self.splitPos(self.g.get_all_v()[e].getPosAsString())
                if listOfEdgesByX is not None:
                    list_X.append(listOfEdgesByX[0])
                    list_Y.append(listOfEdgesByX[1])

                plt.plot(list_X, list_Y, "*-b")
                # listOfVector = self.checkValue(listOfVector)
                # listOfEdgesByX = self.checkValue(listOfEdgesByX)
                # #plt.scatter(listOfVector[0], listOfVector[1], s=150, zorder=5)
                # dx = listOfEdgesByX[0]-listOfVector[0]
                # dy = listOfEdgesByX[1]-listOfVector[1]
                # plt.arrow(listOfVector[0], listOfVector[1], dx, dy, head_length=0.07, head_width=0.05, ec='black')
        plt.xlabel('x - axis')
        plt.ylabel('y - axis')
        plt.title('Shai Sason Yehuda Aharon #1, V = {}, E = {}'.format(self.g.v_size(), self.g.e_size()))
        plt.show()
        return None

    def checkValue(self, checkList) -> list:
        if checkList[0] < 0:
            checkList[0] += 0.04
        else:
            checkList[0] -= 0.04

        if checkList[1] < 0:
            checkList[1] += 0.04
        else:
            checkList[1] -= 0.04
        return checkList

    def splitPos(self, pos: str) -> list:
        if pos == "":
            x = float((r.random() * 5) + 2)
            y = float((r.random() * 5) + 2)
            return [x, y]
        else:
            x = float(pos.split(",")[0])
            y = float(pos.split(",")[1])
            return [x, y]
