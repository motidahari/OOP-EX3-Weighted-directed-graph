import json as Js
import math
from typing import List
import matplotlib.pyplot as plt
from DiGraph import DiGraph
from src import GraphInterface
from src.GraphAlgoInterface import GraphAlgoInterface
import random as r


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph=None):
        self.tags = {}
        self.map = {}
        self.VISITED = 1
        self.NOT_VISITED = 0
        self.g = None if graph is None else graph
        self.mc = 0 if graph is None else graph.get_mc()
        self.nodeSize = 0 if graph is None else graph.v_size()
        self.edgeSize = 0 if graph is None else graph.e_size()
        self.TransposedGraph = None if graph is None else self.createTransposedGraph(graph)
        positive_infnity = float('inf')
        negative_infnity = float('-inf')

    def BFS(self, node_id: int, graph: DiGraph):
        """
        Finds all the Strongly Connected Component(SCC) in the graph.
        @return: The list all SCC
        """
        if self.g is None:
            return
        node = self.g.get_all_v()[node_id]
        node.setTag(self.VISITED)
        node.setTag(self.NOT_VISITED)
        queue = []
        queue.append(node)
        while len(queue) > 0:
            delNode = queue.pop(0)
            for e in self.g.all_out_edges_of_node(delNode.getKey()):
                node = self.g.get_all_v()[e]
                if node.getTag() == self.NOT_VISITED:
                    queue.append(node)
                    node.setTag(self.VISITED)

    def createTransposedGraph(self, graph) -> DiGraph:
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
        if self.g is None:
            return
        for x in self.g.get_all_values():
            self.tags[x] = t

    def setAllWeightAndInfo(self, t: float):
        if self.g is None:
            return
        for x in self.g.get_all_values():
            x.setWeight(t)
            x.setInfo("")
            # print(x)

    def printAllTags(self):
        if self.g is None:
            return
        for x in self.tags.items():
            print(x)

    def get_graph(self) -> GraphInterface:
        if self.g is None:
            return None
        """
        :return: the directed graph on which the algorithm works on.
        """
        return self.g

    def load_from_json(self, file_name: str) -> bool:
        """
        Loads a graph from a json file.
        @param file_name: The path to the json file
        @returns True if the loading was successful, False o.w.
        """
        try:
            new_graph = DiGraph()
            with open(file_name, 'r') as reader:
                json_graph = Js.load(reader)
                reader.close()
                edges = json_graph["Edges"]
                nodes = json_graph["Nodes"]
                for x in nodes:
                    pos = None
                    if 'pos' in x:
                        posString = x["pos"].split(",")
                        pos = (float(posString[0]), float(posString[1]), float(posString[2]))
                    new_graph.add_node(int(x["id"]), pos)
                for x in edges:
                    new_graph.add_edge(int(x["src"]), int(x["dest"]), float(x["w"]))
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
        # print("self.g in save = \n{}".format(self.g))
        my_dict = {}
        my_dict["Edges"] = []
        my_dict["Nodes"] = []
        for x in self.g.get_all_values():
            node_dict = {}
            node_dict["id"] = x.getKey()
            if len(x.getPos()) > 0:
                node_dict["pos"] = x.getPos()
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
            raise FileExistsError
            return False
        finally:
            writer.close()

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        """
        Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
        @param id1: The start node id
        @param id2: The end node id
        @return: The di.stance of the path, the path as a list
        Example:
        #        >>> from GraphAlgo import GraphAlgo
        #        >>> g_algo = GraphAlgo()
        #        >>> g_algo.addNode(0)
        #        >>> g_algo.addNode(1)
        #        >>> g_algo.addNode(2)
        #        >>> g_algo.addEdge(0,1,1)
        #        >>> g_algo.addEdge(1,2,4)
        #        >>> g_algo.shortestPath(0,1)
        #        (1, [0, 1])
        #        >>> g_algo.shortestPath(0,2)
        #        (5, [0, 1, 2])
        More info:
        https://en.wikipedia.org/wiki/Dijkstra's_algorithm
        """
        if self.g is None:
            return (-1, [])
        if id1 in self.g.get_v_keys() and id1 == id2:
            # print("if id1 in self.g.get_all_v_keys() and id1 == id2:")
            # my_tuple = (0, [self.g.get_all_v()[id1]])
            my_tuple = (0, [self.g.get_all_v()[id1].getKey()])
            return my_tuple
        # print(self.g.get_all_v().keys())
        if id1 not in self.g.get_all_v().keys() or id2 not in self.g.get_all_v().keys():
            # print("if id1 not in self.g.get_all_v_keys() or id2 not in self.g.get_all_v_keys():")
            my_tuple = (-1, [])
            return my_tuple
        queue = [id1]
        self.setAllWeightAndInfo(-1)
        self.g.get_all_v()[id1].setWeight(0)
        info = "{}".format(id1)
        self.g.get_all_v()[id1].setInfo(info)
        while queue:
            node = queue.pop(0)
            for x in self.g.all_out_edges_of_node(node).keys():
                # print(self.g.get_all_v())
                if self.g.get_all_v()[x].getWeight() == -1 or self.g.get_all_v()[x].getWeight() > self.g.get_all_v()[
                    node].getWeight() + self.g.all_out_edges_of_node(node)[x]:
                    self.g.get_all_v()[x].setWeight(
                        self.g.get_all_v()[node].getWeight() + self.g.all_out_edges_of_node(node)[x])
                    queue.append(x)
                    info = "{},{}".format(self.g.get_all_v()[node].getInfo(), x)
                    self.g.get_all_v()[x].setInfo(info)
        if self.g.get_all_v()[id2].getWeight() == -1:
            my_tuple = (math.inf, [])
            return my_tuple
        else:
            my_list = []
            for x in self.g.get_all_v()[id2].getInfo().split(','):
                my_list.append(int(x))
            my_tuple = (self.g.get_all_v()[id2].getWeight(), my_list)
            return my_tuple

    def connected_component(self, id1: int) -> list:
        """
        Finds the Strongly Connected Component(SCC) that node id1 is a part of.
        @param id1: The node id
        @return: The list of nodes in the SCC
        """
        if self.g is None:
            return []

        my_list = self.connected_components()
        if my_list:
            for x in my_list:
                if id1 in x:
                    return x
        return []

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
            for id in keys:
                if id not in f:
                    queue = [id]
                    while len(queue) > 0:
                        vertex = queue[-1]
                        if vertex not in p:
                            i = i + 1
                            p[vertex] = i
                        done = 1
                        v_nbrs = self.g.all_out_edges_of_node(vertex)
                        for w in v_nbrs:
                            if w not in p:
                                queue.append(w)
                                done = 0
                                break
                        if done == 1:
                            l[vertex] = p[vertex]
                            for w in v_nbrs:
                                if w not in f:
                                    if p[w] <= p[vertex]:
                                        l[vertex] = min([l[vertex], p[w]])
                                    else:
                                        l[vertex] = min([l[vertex], l[w]])
                            queue.pop()
                            if l[vertex] != p[vertex]:
                                my_list.append(vertex)
                            else:
                                f[vertex] = True
                                scc = [vertex]
                                while my_list and p[my_list[-1]] > p[vertex]:
                                    k = my_list.pop()
                                    f[k] = True
                                    scc.append(k)
                                result.append(scc)
            self.components = result
            return result

    def plot_graph(self) -> None:
        """
        Plots the graph.
        If the nodes have a position, the nodes will be placed there.
        Otherwise, they will be placed in a random but elegant manner.
        @return: None
        """
        list_X = []
        list_Y = []
        for x in self.g.get_all_v().keys():
            for e in self.g.all_out_edges_of_node(x).keys():
                # print(self.g.get_all_v()[x].getPos())
                listOfVector = self.splitPos(self.g.get_all_v()[x].getPos())
                if listOfVector is not None:
                    list_X.append(listOfVector[0])
                    list_Y.append(listOfVector[1])

                listOfEdgesByX = self.splitPos(self.g.get_all_v()[e].getPos())
                if listOfEdgesByX is not None:
                    list_X.append(listOfEdgesByX[0])
                    list_Y.append(listOfEdgesByX[1])

                plt.plot(list_X, list_Y, "*-b")

                #
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
            # print("values")
            x = float(pos.split(",")[0])
            y = float(pos.split(",")[1])
            return [x, y]
