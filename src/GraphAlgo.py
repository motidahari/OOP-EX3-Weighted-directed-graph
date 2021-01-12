import json as Js
import math
from queue import PriorityQueue
from typing import List
import matplotlib.pyplot as plt
from DiGraph import DiGraph
from src import GraphInterface
from Node import Node
from src.GraphAlgoInterface import GraphAlgoInterface

class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph):
        self.tags = {}
        self.map = {}
        self.VISITED = 1
        self.NOT_VISITED = 0
        #self.g = DiGraph() if graph is None else graph
        self.g = graph
        self.createTransposedGrapg(graph)
        positive_infnity = float('inf')
        negative_infnity = float('-inf')

    def BFS(self, node_id: int, graph: DiGraph):
        """
        Finds all the Strongly Connected Component(SCC) in the graph.
        @return: The list all SCC
        """
        node = self.g.get_V()[node_id]
        node.setTag(self.VISITED)
        node.setTag(self.NOT_VISITED)
        queue = []
        queue.append(node)
        while len(queue) > 0:
            delNode = queue.pop(0)
            for e in self.g.all_out_edges_of_node(delNode.getKey()):
                node = self.g.get_V()[e]
                if node.getTag() == self.NOT_VISITED:
                    queue.append(node)
                    node.setTag(self.VISITED)

    def createTransposedGrapg(self, graph):
        new_graph = DiGraph()
        for x in self.g.get_all_values():
            new_graph.add_node(x.getKey())
        for x in self.g.get_all_values():
            for e in self.g.all_out_edges_of_node(x.getKey()):
                new_graph.add_edge(e,x.getKey(),self.g.all_out_edges_of_node(x.getKey())[e])
        self.transposed_grapg = new_graph

    def setAllTags(self, t: float):
        for x in self.g.get_all_values():
            self.tags[x] = t

    def setAllWeightAndInfo(self, t: float):
        for x in self.g.get_all_values():
            x.setWeight(t)
            x.setInfo("")
            #print(x)

    def printAllTags(self):
        for x in self.tags.items():
            print(x)

    def get_graph(self) -> GraphInterface:
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
                # print("json_graph = " , json_graph)
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
            raise FileExistsError
            return False

    def save_to_json(self, file_name: str) -> bool:
        """
        Saves the graph in JSON format to a file
        @param file_name: The path to the out file
        @return: True if the save was successful, Flase o.w.
        """
        #print("self.g in save = \n{}".format(self.g))
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
        if id1 in self.g.get_V_keys() and id1 == id2:
            #print("if id1 in self.g.get_V_keys() and id1 == id2:")
            #my_tuple = (0, [self.g.get_V()[id1]])
            my_tuple = (0, [self.g.get_V()[id1].getKey()])
            return my_tuple
        #print(self.g.get_V().keys())
        if id1 not in self.g.get_V().keys() or id2 not in self.g.get_V().keys():
            #print("if id1 not in self.g.get_V_keys() or id2 not in self.g.get_V_keys():")
            my_tuple = (-1, [])
            return my_tuple
        queue = [id1]
        self.setAllWeightAndInfo(-1)
        self.g.get_V()[id1].setWeight(0)
        info = "{}".format(id1)
        self.g.get_V()[id1].setInfo(info)
        while queue:
            node = queue.pop(0)
            for x in self.g.all_out_edges_of_node(node).keys():
                #print(self.g.get_V())
                if self.g.get_V()[x].getWeight() == -1 or self.g.get_V()[x].getWeight() > self.g.get_V()[node].getWeight() + self.g.all_out_edges_of_node(node)[x]:
                    self.g.get_V()[x].setWeight(self.g.get_V()[node].getWeight() + self.g.all_out_edges_of_node(node)[x])
                    queue.append(x)
                    info = "{},{}".format(self.g.get_V()[node].getInfo(),x)
                    self.g.get_V()[x].setInfo(info)
        if self.g.get_V()[id2].getWeight() == -1:
            my_tuple = (math.inf, [])
            return my_tuple
        else:
            my_list = []
            for x in self.g.get_V()[id2].getInfo().split(','):
                my_list.append(int(x))
            my_tuple = (self.g.get_V()[id2].getWeight(), my_list)
            return my_tuple

    def shortest_path2(self, id1: int, id2: int) -> bool:
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
        if id1 in self.g.get_V_keys() and id1 == id2:
            # print("if id1 in self.g.get_V_keys() and id1 == id2:")
            # my_tuple = (0, [self.g.get_V()[id1]])
            my_tuple = (0, [self.g.get_V()[id1].getKey()])
            return my_tuple
        if id1 not in self.g.get_V_keys() or id2 not in self.g.get_V_keys():
            # print("if id1 not in self.g.get_V_keys() or id2 not in self.g.get_V_keys():")
            my_tuple = (-1, [])
            return my_tuple
        queue = [id1]
        self.setAllWeightAndInfo(-1)
        self.g.get_V()[id1].setWeight(0)
        info = "{}".format(id1)
        self.g.get_V()[id1].setInfo(info)
        while queue:
            node = queue.pop(0)
            for x in self.g.all_out_edges_of_node(node).keys():
                # print(self.g.get_V())
                if self.g.get_V()[x] == id2:
                    return True
                if self.g.get_V()[x].getWeight() == -1 or self.g.get_V()[x].getWeight() > self.g.get_V()[
                    node].getWeight() + self.g.all_out_edges_of_node(node)[x]:
                    self.g.get_V()[x].setWeight(
                        self.g.get_V()[node].getWeight() + self.g.all_out_edges_of_node(node)[x])
                    queue.append(x)
                    info = "{},{}".format(self.g.get_V()[node].getInfo(), x)
                    self.g.get_V()[x].setInfo(info)
        return False

    def connected_component(self, id1: int) -> list:
        """
        Finds the Strongly Connected Component(SCC) that node id1 is a part of.
        @param id1: The node id
        @return: The list of nodes in the SCC
        """
        my_list = self.strongly_connected_components()
        for x in my_list:
            if id1 in x:
                return x
        return []

    def connected_components(self) -> List[list]:
        """
        Finds all the Strongly Connected Component(SCC) in the graph.
        @return: The list all SCC
        """
        return self.strongly_connected_components()

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
                list_X.append(float(x.getPos().split(",")[0]))
                list_Y.append(float(x.getPos().split(",")[1]))

                # list_X.append(e.getPos().split(",")[1])
                # list_Y.append(e.getPos().split(",")[1])
            plt.plot(list_X, list_Y)

        plt.xlabel('x - axis')
        plt.ylabel('y - axis')
        plt.title('Shai Sason Yehuda Aharon #1')
        plt.show()
        pass

    def strongly_connected_components(self):
        therealist = []
        preorder = {}
        lowlink = {}
        scc_found = {}
        scc_queue = []
        i = 0  # Preorder counter
        for source in self.g.get_all_v().keys():
            if source not in scc_found:
                queue = [source]
                while queue:
                    v = queue[-1]
                    if v not in preorder:
                        i = i + 1
                        preorder[v] = i
                    done = 1
                    v_nbrs = self.g.all_out_edges_of_node(v)
                    for w in v_nbrs:
                        if w not in preorder:
                            queue.append(w)
                            done = 0
                            break
                    if done == 1:
                        lowlink[v] = preorder[v]
                        for w in v_nbrs:
                            if w not in scc_found:
                                if preorder[w] > preorder[v]:
                                    lowlink[v] = min([lowlink[v], lowlink[w]])
                                else:
                                    lowlink[v] = min([lowlink[v], preorder[w]])
                        queue.pop()
                        if lowlink[v] == preorder[v]:
                            scc_found[v] = True
                            scc = [v]
                            while scc_queue and preorder[scc_queue[-1]] > preorder[v]:
                                k = scc_queue.pop()
                                scc_found[k] = True
                                scc.append(k)
                            #yield scc
                            therealist.append(scc)
                        else:
                            scc_queue.append(v)
        return therealist