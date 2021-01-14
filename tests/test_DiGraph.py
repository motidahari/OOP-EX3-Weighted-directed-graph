from unittest import TestCase
from src.DiGraph import DiGraph
import random as r


class TestDiGraph(TestCase):
    graph = None

    def setUp(self):
        """
        We are running on range 200, we add 200 nodes to the graph.
        This functions tests the constructor function for the class DiGraph
        """
        g = DiGraph()
        for x in range(200):
            g.add_node(x)

        self.assertIsNotNone(g)
        self.assertEqual(200, g.get_mc())
        self.graph = g

    def test_v_size(self):
        """
        We are running on range 21, we remove 21 nodes from the graph.
        This functions tests the v_size function for the class DiGraph
        """
        self.assertEqual(200, len(self.graph.get_all_v()))
        for x in range(21):
            # rand = r.randrange(0,len(self.graph.get_V()))
            self.graph.remove_node(200 - 1 - x);

        self.assertEqual(179, len(self.graph.get_all_v()))
        self.assertNotEqual(200, len(self.graph.get_all_v()))

    def test_e_size(self):
        """
        We are running on by all vertex, connect each vertex to key + 1 and key + 2
        This functions tests the e_size function for the class DiGraph
        """
        for x in self.graph.get_all_values():
            self.graph.add_edge(x.getKey(), x.getKey() + 1, x.getKey() * 100)
            self.graph.add_edge(x.getKey(), x.getKey() + 2, x.getKey() * 100)
        self.assertEqual(len(self.graph.get_all_v()) * 2 - 3, self.graph.e_size())

    def test_get_all_v(self):
        """
        We are running on by all vertex in the graph, and try to add the same key from the graph to new graph.
        we check the keys from graph1 to graph2 and check the number of ms and e_size and v_size.
        This functions tests the get_all_v function for the class DiGraph.
        """
        newG = DiGraph()
        for x in self.graph.get_all_v().values():
            newG.add_node(x.getKey())
        for x in newG.get_all_v().values():
            self.assertEqual(x.getKey(), self.graph.get_all_v()[x.getKey()].getKey())

        self.assertEqual(len(newG.get_all_v()), len(self.graph.get_all_v()))
        self.assertEqual(newG.get_mc(), self.graph.get_mc())
        self.assertEqual(newG.e_size(), self.graph.e_size())
        self.assertEqual(newG.v_size(), self.graph.v_size())

    def test_get_all_values(self):
        """
        We are running on by all vertex in the graph, and try to add the same key from the graph to new graph.
        we check the keys from graph1 to graph2 and check the number of ms and e_size and v_size.
        This functions tests the get_all_values function for the class DiGraph.
        """
        newG = DiGraph()
        for x in self.graph.get_all_values():
            newG.add_node(x.getKey())
        for x in newG.get_all_values():
            self.assertEqual(x.getKey(), self.graph.get_all_v()[x.getKey()].getKey())
        self.assertEqual(len(newG.get_all_v()), len(self.graph.get_all_v()))
        self.assertEqual(newG.get_mc(), self.graph.get_mc())
        self.assertEqual(newG.e_size(), self.graph.e_size())
        self.assertEqual(newG.v_size(), self.graph.v_size())

    def test_get_v_keys(self):
        """
        We are running on by all vertex in the graph, and try to add the same key from the graph to new graph.
        we check the keys from graph1 to graph2 and check the number of ms and e_size and v_size.
        This functions tests the get_v_keys function for the class DiGraph.
        """
        newG = DiGraph()
        for x in self.graph.get_v_keys():
            newG.add_node(x)
        for x in newG.get_all_values():
            self.assertEqual(x.getKey(), self.graph.get_all_v()[x.getKey()].getKey())
        self.assertEqual(len(newG.get_all_v()), len(self.graph.get_all_v()))
        self.assertEqual(newG.get_mc(), self.graph.get_mc())
        self.assertEqual(newG.e_size(), self.graph.e_size())
        self.assertEqual(newG.v_size(), self.graph.v_size())

    def test_get_items(self):
        """
        We are running on by all vertex in the graph, and try to add the same key from the graph to new graph.
        we check the keys from graph1 to graph2 and check the number of ms and e_size and v_size.
        This functions tests the get_items function for the class DiGraph.
        """
        newG = DiGraph()
        for x in self.graph.get_items():
            newG.add_node(x[1].getKey())
        for x in newG.get_all_values():
            self.assertEqual(x.getKey(), self.graph.get_all_v()[x.getKey()].getKey())
        self.assertEqual(len(newG.get_all_v()), len(self.graph.get_all_v()))
        self.assertEqual(newG.get_mc(), self.graph.get_mc())
        self.assertEqual(newG.e_size(), self.graph.e_size())
        self.assertEqual(newG.v_size(), self.graph.v_size())

    def test_all_in_edges_of_node(self):
        """
        We are running on by all vertex, connect each vertex to key + 1 and key + 2.
        we check the number of the edges in the graph by node_id.
        This functions tests the all_in_edges_of_node function for the class DiGraph.
        """
        for x in self.graph.get_all_values():
            self.graph.add_edge(x.getKey(), x.getKey() + 1, x.getKey() * 100)
            self.graph.add_edge(x.getKey(), x.getKey() + 2, x.getKey() * 100)
        run = 0
        for x in self.graph.get_all_values():
            if run == 0:
                self.assertEqual(0, len(self.graph.all_in_edges_of_node(x.getKey())))
            if run == 1:
                self.assertEqual(1, len(self.graph.all_in_edges_of_node(x.getKey())))
                self.assertEqual(0, self.graph.all_in_edges_of_node(x.getKey())[0])
            run += 1
            z = 2
            for i in self.graph.all_in_edges_of_node(x.getKey()):
                if run > 2:
                    self.assertEqual(x.getKey() - z, i)
                    z -= 1

    def test_all_out_edges_of_node(self):
        """
        We are running on by all vertex, connect each vertex to key + 1 and key + 2.
        we check the number of the edges in the graph by node_id.
        This functions tests the all_out_edges_of_node function for the class DiGraph.
        """
        for x in self.graph.get_all_values():
            self.graph.add_edge(x.getKey(), x.getKey() + 1, x.getKey() * 100)
            self.graph.add_edge(x.getKey(), x.getKey() + 2, x.getKey() * 100)
        run = 0
        for x in self.graph.get_all_values():
            if run == 0:
                self.assertEqual(2, len(self.graph.all_out_edges_of_node(x.getKey())))
            if run == 198:
                self.assertEqual(1, len(self.graph.all_out_edges_of_node(x.getKey())))
            run += 1
            z = 1
            for i in self.graph.all_out_edges_of_node(x.getKey()):
                if run > 2:
                    if i != x.getKey()+ z:
                        self.assertEqual(x.getKey() + z, i)
                    z += 1



    def test_get_mc(self):
        """
        We are running on by all vertex, connect each vertex to key + 1.
        This functions tests the get_mc function for the class DiGraph
        """
        mc = 200
        self.assertEqual(self.graph.get_mc(), mc)
        for x in self.graph.get_all_values():
            if self.graph.add_edge(x.getKey(), x.getKey() + 1, x.getKey() * 100) is True:
                mc += 1
        self.assertEqual(self.graph.get_mc(), mc)
        for x in range(50):
            if self.graph.remove_node(self.graph.nodeSize - x) is True:
                mc += 1
        self.assertEqual(self.graph.get_mc(), mc)
        for x in range(50):
            if self.graph.remove_edge(x,x+1) is True:
                mc += 1
        self.assertEqual(self.graph.get_mc(), mc)

    def test_add_edge(self):
        """
        We are running on by all vertex, connect each vertex to key + 1.
        and try to make more connent from the vertex in the graph and remove nodes from the graph.
        This functions tests the add_edge function for the class DiGraph.
        """
        edges = 0
        self.assertEqual(self.graph.e_size(), edges)
        for x in self.graph.get_all_values():
            if self.graph.add_edge(x.getKey(), x.getKey() + 1, x.getKey() * 100) is True:
                edges += 1
        self.assertEqual(self.graph.e_size(), edges)

        for x in range(50):
            removedEdges = self.graph.e_size_by_id(self.graph.nodeSize - x)
            if self.graph.remove_node(self.graph.nodeSize - x) is True:
                edges -= removedEdges

        for x in self.graph.get_all_values():
            if self.graph.add_edge(x.getKey(), x.getKey() + 1, x.getKey() * 100) is True:
                edges += 1
        self.assertEqual(self.graph.e_size(), edges)

        for x in range(50):
            if self.graph.add_edge(x, x + 1,r.random()*10000) is True:
                edges += 1
            if self.graph.remove_edge(x, x + 1) is True:
                edges -= 1

            if self.graph.add_edge(x, x + 1,r.random()*10000) is True:
                edges += 1
            if self.graph.add_edge(x + 1, x + 2,r.random()*10000) is True:
                edges += 1

        for x in self.graph.get_all_values():
            if self.graph.add_edge(x.getKey(), x.getKey() + 1, x.getKey() * 100) is True:
                edges += 1

        self.assertEqual(self.graph.e_size(), edges)

    def test_add_node(self):
        """
        We are running on by range 200, try to add random key in the graph.
        and try to add and remove nodes from the graph.
        This functions tests the add_node function for the class DiGraph.
        """
        nodes = 200
        self.assertEqual(self.graph.v_size(), nodes)
        for x in range(200):
            if self.graph.add_node(r.random()*200) is True:
                nodes += 1
        self.assertEqual(self.graph.v_size(), nodes)
        for x in range(50):
            removedNodes = self.graph.e_size_by_id(self.graph.nodeSize - x)
            if self.graph.remove_node(self.graph.nodeSize - x) is True:
                nodes -= removedNodes
        for x in range(500):
            if self.graph.add_node(x*r.random()*10000 - 50000) is True:
                nodes += 1
        self.assertEqual(self.graph.v_size(), nodes)
        for x in range(50):
            if self.graph.add_node( r.random() * 10000) is True:
                nodes += 1
            if self.graph.remove_node(x) is True:
                nodes -= 1
            if self.graph.add_node( r.random() * 10000) is True:
                nodes += 1
            if self.graph.add_node( r.random() * 10000) is True:
                nodes += 1
        self.assertEqual(self.graph.v_size(), nodes)

    def test_remove_node(self):
        """
        We are running on by range 50, try to add random key in the graph.
        and try to add and remove nodes from the graph.
        This functions tests the add_node function for the class DiGraph.
        """
        nodes = 200
        self.assertEqual(self.graph.v_size(), nodes)
        self.assertEqual(self.graph.v_size(), nodes)
        for x in range(50):
            if self.graph.add_node(r.random() * 10000) is True:
                nodes += 1
            if self.graph.remove_node(x) is True:
                nodes -= 1
            if self.graph.add_node(r.random() * 10000) is True:
                nodes += 1
            if self.graph.add_node(r.random() * 10000) is True:
                nodes += 1
        for x in range(50):
            removedNodes = self.graph.e_size_by_id(self.graph.nodeSize - x)
            if self.graph.remove_node(self.graph.nodeSize - x) is True:
                nodes -= removedNodes
        for x in range(200):
            if self.graph.add_node(r.random() * 200) is True:
                nodes += 1
        self.assertEqual(self.graph.v_size(), nodes)
        for x in range(500):
            if self.graph.add_node(x * r.random() * 10000 - 50000) is True:
                nodes += 1
        self.assertEqual(self.graph.v_size(), nodes)

    def test_remove_edge(self):
        """
        We are running on by all the vertex, try to connect each node to node_key + 1.
        and try to add and remove nodes and edges from the graph.
        This functions tests the remove_edge function for the class DiGraph.
        """
        edges = 0
        self.assertEqual(self.graph.e_size(), edges)
        for x in self.graph.get_all_values():
            if self.graph.add_edge(x.getKey(), x.getKey() + 1, x.getKey() * 100) is True:
                edges += 1

        self.assertEqual(self.graph.e_size(), edges)
        for x in range(50):
            if self.graph.add_edge(x, x + 1, r.random() * 10000) is True:
                edges += 1
            if self.graph.remove_edge(x, x + 1) is True:
                edges -= 1
            if self.graph.add_edge(x, x + 1, r.random() * 10000) is True:
                edges += 1
            if self.graph.add_edge(x + 1, x + 2, r.random() * 10000) is True:
                edges += 1
        for x in self.graph.get_all_values():
            if self.graph.add_edge(x.getKey(), x.getKey() + 1, x.getKey() * 100) is True:
                edges += 1
        self.assertEqual(self.graph.e_size(), edges)
        for x in self.graph.get_all_values():
            if self.graph.add_edge(x.getKey(), x.getKey() + 1, x.getKey() * 100) is True:
                edges += 1
        for x in range(50):
            removedEdges = self.graph.e_size_by_id(self.graph.nodeSize - x)
            if self.graph.remove_node(self.graph.nodeSize - x) is True:
                edges -= removedEdges
        self.assertEqual(self.graph.e_size(), edges)

