from GraphInterface import GraphInterface
from Node import Node


class DiGraph(GraphInterface):
    """This abstract class represents an interface of a graph."""
    V = {}
    Nin = {}
    Nout = {}
    total_E = {}
    key = int()
    nodeSize = int()
    edgeSize = int()
    mc = int()

    def __init__(self):
        self.V = {}
        self.Nin = {}
        self.Nout = {}
        self.total_E = {}
        self.key = 0
        self.nodeSize = 0
        self.edgeSize = 0
        self.mc = 0

    def v_size(self) -> int:
        """
        Returns the number of vertices in this graph
        @return: The number of vertices in this graph
        """
        return self.nodeSize

    def e_size(self) -> int:
        """
        Returns the number of edges in this graph
        @return: The number of edges in this graph
        """
        return self.edgeSize
    def e_size_by_id(self,id1) -> int:
        """
        Returns the number of edges in this graph
        @return: The number of edges in this graph
        """
        if id1 in self.total_E.keys():
            return self.total_E[id1]
        return 0

    def get_all_v(self) -> dict:
        """return a dictionary of all the nodes in the Graph, each node is represented using apair  (key, node_data)
        """
        return self.V

    def get_all_values(self) -> dict:
        """need to change


        return a dictionary of all the nodes in the Graph, each node is represented using apair  (key, node_data)
        """
        return self.V.values()

    def get_items(self) -> dict:
        """need to change

        return a dictionary of all the nodes in the Graph, each node is represented using apair  (key, node_data)
        """
        return self.V.items()

    def get_v_keys(self) -> dict:
        """need to change
        return a dictionary of all the key in the dict, each node is represented using apair  (key, node_data)
        """
        return self.V.keys()

    def all_in_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected to (into) node_id ,
        each node is represented using a pair (key, weight)
         """
        return self.Nin[id1]

    def all_out_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected from node_id , each node is represented using a pair (key,
        weight)
        """
        return self.Nout[id1]

    def get_mc(self) -> int:
        """
        Returns the current version of this graph,
        on every change in the graph state - the MC should be increased
        @return: The current version of this graph.
        """
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        """
        Adds an edge to the graph.
        @param id1: The start node of the edge
        @param id2: The end node of the edge
        @param weight: The weight of the edge
        @return: True if the edge was added successfully, False o.w.

        Note: If the edge already exists or one of the nodes dose not exists the functions will do nothing
        """
        if id1 != id2 and id1 in self.V and id2 in self.V and id1 in self.Nin \
                and id2 in self.Nin and id1 in self.Nout and id2 in self.Nout \
                and id1 not in self.Nin[id2] and id2 not in self.Nout[id1]:
            self.Nout[id1][id2] = float(weight)
            self.Nin[id2][id1] = float(weight)
            self.mc += 1
            self.total_E[id1] += 1
            self.total_E[id2] += 1
            self.edgeSize += 1
            return True
        else:
            return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        """
        Adds a node to the graph.
        @param node_id: The node ID
        @para
        m pos: The position of the node
        @return: True if the node was added successfully, False o.w.
        Note: if the node id already exists the node will not be added
        :param pos:
        :param pos:
        """
        if node_id not in self.V and node_id not in self.Nin and node_id not in self.Nout:
            node = Node(node_id, "", 0, 0, pos)
            self.V[node_id] = node
            self.Nout[node_id] = {}
            self.Nin[node_id] = {}
            self.key += 1
            self.total_E[node_id] = 0
            self.nodeSize += 1
            self.mc += 1
            return True
        else:
            return False
            return False

    def remove_node(self, node_id: int) -> bool:
        """
        Removes a node from the graph.
        @param node_id: The node ID
        @return: True if the node was removed successfully, False o.w.
        Note: if the node id does not exists the function will do nothing
        """
        if node_id in self.V:
            inComingEdges = self.all_in_edges_of_node(node_id).keys()
            outGoingEdges = self.all_out_edges_of_node(node_id).keys()
            removedEdges = 0
            for x in inComingEdges:
                del self.Nout[x][node_id]
                removedEdges += 1
            for x in outGoingEdges:
                del self.Nin[x][node_id]
                removedEdges += 1

            del self.Nin[node_id]
            del self.Nout[node_id]
            del self.V[node_id]
            del self.total_E[node_id]
            self.edgeSize -= removedEdges
            self.nodeSize -= 1
            self.mc += 1
            return True
        else:
            return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        """
        Removes an edge from the graph.
        @param node_id1: The start node of the edge
        @param node_id2: The end node of the edge
        @return: True if the edge was removed successfully, False o.w.

        Note: If such an edge does not exists the function will do nothing
        """
        if node_id1 != node_id2 and node_id1 in self.V and node_id2 in self.V and node_id2 in self.Nout[node_id1] and node_id1 in self.Nin[node_id2]:

            self.Nin[node_id2].pop(node_id1)
            self.Nout[node_id1].pop(node_id2)
            self.mc += 1
            self.edgeSize -= 1
            return True
        else:
            return False

    # def __str__(self) -> str:
    #     str = ""
    #     for element in self.V.values():
    #             print(element)
    #     return str

    def __str__(self) -> str:
        str = "Vertices: {}, Edges: {}, MC: {}\n".format(self.nodeSize , self.edgeSize, self.mc)
        for element in self.V.values():
            for ni in self.Nout[element.getKey()].keys():
                str += "({0} -> {1}) w = {2}, \n".format(element.getKey(), ni, self.Nout[element.getKey()][ni])
        return str

    def toStringInAndOut(self) -> str:
        str = "Vertices: {}, Edges: {}, MC: {}\n".format(self.nodeSize , self.edgeSize, self.mc)
        str += "Graph's nodes predecessors = { "
        for element in self.V.values():
            str += "#{} in -> :{}\n".format(element.getKey(),self.all_in_edges_of_node(element.getKey()))
        str += "}\n\n"
        str += "Graph's nodes successors  = { \n"
        for element in self.V.values():
            str += "#{} out -> :{}\n".format(element.getKey(), self.all_out_edges_of_node(element.getKey()))
        str += "}\n\n"
        return str


