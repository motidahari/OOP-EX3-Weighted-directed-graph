import unittest

from GraphAlgo import GraphAlgo
from GraphAlgoInterface import GraphAlgoInterface
from GraphInterface import GraphInterface
from DiGraph import DiGraph


class MyTestCase(unittest.TestCase):
    # def test_something(self):
    #     self.assertEqual(True, False)

    def test0(self):
        """ testing an empty graph """
        g = DiGraph()
        g_algo = GraphAlgo(g)
        a = g.remove_edge(0, 1)  # False
        b = g.remove_node(0)  # False
        c = g.add_edge(0, 1, 9)  # False
        eSize = g.e_size()  # 0
        vSize = g.v_size()  # 0
        path = g_algo.shortest_path(0, 1)
        connected = g_algo.connected_components()
        self.assertEqual(a, False)
        self.assertEqual(b, False)
        self.assertEqual(c, False)
        self.assertEqual(eSize, 0)
        self.assertEqual(vSize, 0)
        self.assertEqual(path, (-1, []))
        self.assertEqual(connected, [])

    def test1(self):
        """ testing on graph with 1 node """
        g = DiGraph()
        g.add_node(0)
        g_algo = GraphAlgo(g)
        a1 = g.remove_edge(0, 1)  # False
        a2 = g.remove_edge(1, 0)  # False
        b1 = g.remove_node(1)  # False
        c1 = g.add_edge(0, 1, 9)  # False
        c2 = g.add_edge(1, 0, 9)  # False
        eSize = g.e_size()  # 0
        vSize = g.v_size()  # 1
        path1 = g_algo.shortest_path(0, 1)
        path2 = g_algo.shortest_path(1, 0)
        path3 = g_algo.shortest_path(0, 0)
        connected = g_algo.connected_components()
        b2 = g.remove_node(0)  # True
        self.assertEqual(a1, False)
        self.assertEqual(a2, False)
        self.assertEqual(b1, False)
        self.assertEqual(b2, True)
        self.assertEqual(c1, False)
        self.assertEqual(c2, False)
        self.assertEqual(eSize, 0)
        self.assertEqual(vSize, 1)
        self.assertEqual(path1, (-1, []))
        self.assertEqual(path2, (-1, []))
        self.assertEqual(path3, (0, [0]))
        self.assertEqual(connected, [[0]])

    def test2(self):
        """ testing on graph with 2 nodes and 1 edge """
        g = DiGraph()
        g.add_node(0)
        g.add_node(1)
        g.add_edge(0, 1, 9)
        g_algo = GraphAlgo(g)
        a1 = g.remove_edge(1, 0)  # False
        a2 = g.remove_edge(0, 1)  # True
        c1 = g.add_edge(0, 1, 9)  # True
        c2 = g.add_edge(0, 1, 10)  # True
        print(g.all_out_edges_of_node(0))
        eSize = g.e_size()  # 1
        vSize = g.v_size()  # 2
        path1 = g_algo.shortest_path(0, 1)  # (9, [0,1])
        connected = g_algo.connected_components()  # [[0,1]]
        mc1 = g.get_mc()  # 6
        b1 = g.remove_node(1)  # True
        mc2 = g.get_mc()  # 8
        eSize2 = g.e_size()  # 0
        vSize2 = g.v_size()  # 1
        self.assertEqual(a1, False)
        self.assertEqual(a2, True)
        self.assertEqual(b1, True)
        self.assertEqual(c1, True)
        self.assertEqual(eSize, 1)
        self.assertEqual(vSize, 2)
        self.assertEqual(eSize2, 0)
        self.assertEqual(vSize2, 1)
        self.assertEqual(path1, (9, [0, 1]))
        self.assertEqual(connected, [[1], [0]])
        self.assertEqual(mc1, 5)
        self.assertEqual(mc2, 7)

    def test3(self):
        """ testing on a specific graph """
        g = DiGraph()
        g.add_node(1)
        g.add_node(2)
        g.add_node(3)
        g.add_node(4)
        g.add_node(5)
        g.add_node(6)
        g.add_node(7)
        g.add_node(8)
        g.add_node(9)
        g.add_node(10)
        g.add_edge(1, 4, 20)
        g.add_edge(1, 5, 20)
        g.add_edge(1, 6, 5)
        g.add_edge(1, 7, 15)
        g.add_edge(1, 2, 10)
        g.add_edge(2, 4, 10)
        g.add_edge(2, 3, 5)
        g.add_edge(3, 4, 5)
        g.add_edge(3, 2, 15)
        g.add_edge(4, 5, 10)
        g.add_edge(5, 6, 5)
        g.add_edge(7, 6, 10)
        g.add_edge(8, 1, 5)
        g.add_edge(8, 2, 20)
        g.add_edge(8, 7, 5)
        g.add_edge(9, 2, 15)
        g.add_edge(9, 8, 20)
        g.add_edge(9, 10, 10)
        g.add_edge(10, 2, 5)
        g.add_edge(10, 3, 15)
        g_algo = GraphAlgo(g)

        path1 = g_algo.shortest_path(8, 2)  # (15, [8,1,2])
        connected1 = g_algo.connected_component(6)  # [6]
        connected2 = g_algo.connected_component(3)  # [2, 3]
        self.assertEqual(path1, (15, [8, 1, 2]))
        self.assertEqual(connected1, [6])
        self.assertEqual(connected2, [2, 3])


if __name__ == '__main__':
    unittest.main()
