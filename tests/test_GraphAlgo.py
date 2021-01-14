import os
from pathlib import Path
from unittest import TestCase
import random as r
from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo


class TestGraphAlgo(TestCase):
    list_algo = []
    list_graph = []

    def setUp(self):
        """
        We are call to func1 that run by all the jsons in and create objects of algo and graphs,
        each object we added to list and check the other functions by the lists.
        """
        self.func2()

    def func1(self):
        """
        run by all the jsons in and create objects of algo and graphs,
        each object we added to list and check the other functions by the lists.
        """
        my_list = []
        dir_path = os.path.dirname(os.path.realpath(__file__))
        parent = Path(dir_path).parent
        my_path = ["/Graphs/Graphs_no_pos/", "/Graphs/Graphs_on_circle/", "/Graphs/Graphs_random_pos/"]
        for x in my_path:
            string = "{}{}".format(parent, x)
            for root, dirs, files in os.walk(string):
                for file in files:
                    if file.endswith('.json'):
                        path = "{}{}".format(string, file)
                        my_list.append(path)
        algo = GraphAlgo(DiGraph())
        for i in my_list:
            if algo.load_from_json(i) is True:
                algo = GraphAlgo(algo.get_graph())
                self.list_algo.append(algo)
                self.list_graph.append(algo.get_graph())

    def func2(self):
        """
        create specific graph for some tests.
        with 9 vertex.
        """
        graph = DiGraph()
        for x in range(7):
            graph.add_node(x)
        for x in graph.get_all_values():
            graph.add_edge(x.getKey(), x.getKey() + 1, x.getKey() + 1)
            graph.add_edge(x.getKey(), x.getKey() - 1, x.getKey() + 1)

        graph.add_node(8)
        graph.add_node(9)
        algo = GraphAlgo(graph)
        algo.plot_graph()
        str1 = "{}".format(algo.get_graph())
        str2 = "{}".format(graph.toStringInAndOut())
        print(str1)
        print(str2)
        self.list_algo = []
        self.list_graph = []
        self.list_algo.append(algo)
        self.list_graph.append(algo.get_graph())


    def test_connected_component(self):
        """
        run by func2 and check the connected_component by each node in the graph.
        This functions tests the connected_component function for the class DiGraph
        """
        self.func2()
        my_list = [[0, 1, 2, 3, 4, 5, 6],[8],[9]]
        i = 0

        for x in self.list_graph[0].get_all_v().values():
            str = "i = {} , {} -> {} == {}".format(i,x.getKey(), self.list_algo[0].connected_component(x.getKey()), my_list[0])
            if i < 7:
                self.assertEqual(my_list[0],self.list_algo[0].connected_component(x.getKey()))
            if i == 7:
                self.assertEqual(my_list[1],self.list_algo[0].connected_component(x.getKey()))

            if i == 8:
                self.assertEqual(my_list[2],self.list_algo[0].connected_component(x.getKey()))
            i += 1

    def test_connected_components(self):
        """
        run by func2 and check the connected_components of the graph.
        This functions tests the connected_components function for the class DiGraph
        """
        self.func2()
        my_list = [[0, 1, 2, 3, 4, 5, 6], [8], [9]]
        self.assertEqual(my_list, self.list_algo[0].connected_components())

    def test_create_transposed_graph(self):
        """
        run by func2 and check the create_transposed_graph of the graph.
        This functions tests the create_transposed_graph function for the class DiGraph
        """
        self.func2()
        for i in self.list_algo:
            for node in i.get_graph().get_all_v().keys():
                self.assertEqual(i.get_graph().all_out_edges_of_node(node).keys(),i.get_transposed_graph().all_in_edges_of_node(node).keys())

    def test_set_all_tags(self):
        """
        run by all the jsons file and check the set_all_tags of the graph.
        This functions tests the set_all_tags function for the class DiGraph
        """
        for i in self.list_algo:
            i.setAllTags(100)
        for i in i.getAllTags().values():
            self.assertEqual(100,i)

    def test_get_all_tags(self):
        """
        run by all the jsons file and check the get_all_tags of the graph.
        This functions tests the get_all_tags function for the class DiGraph
        """
        for i in self.list_algo:
            i.setAllTags(100)
        for i in i.getAllTags().values():
            self.assertEqual(100,i)

    def test_set_all_weight_and_info(self):
        """
        run by all the jsons file and check the set_all_weight_and_info of the graph.
        This functions tests the set_all_weight_and_info function for the class DiGraph
        """
        for i in self.list_algo:
            i.setAllWeightAndInfo(100)
        for i in i.get_graph().get_all_v().values():
            self.assertEqual(100,i.getWeight())

    def test_get_graph(self):
        """
        run by all the jsons file and check the get_graph of the graph.
        This functions tests the get_graph function for the class DiGraph
        """
        index = 0
        for i in self.list_graph:
            g1 = "".format(i)
            g2 = "".format(self.list_algo[0].get_graph())
            self.assertEqual(g1,g2)
            index += 1

    def test_load_from_json(self):
        """
        run by all the jsons file and check the load_from_json of the graph.
        This functions tests the load_from_json function for the class DiGraph
        """
        my_list = []
        dir_path = os.path.dirname(os.path.realpath(__file__))
        parent = Path(dir_path).parent
        my_path = ["/Graphs/Graphs_no_pos/", "/Graphs/Graphs_on_circle/", "/Graphs/Graphs_random_pos/"]
        for x in my_path:
            string = "{}{}".format(parent, x)
            for root, dirs, files in os.walk(string):
                for file in files:
                    if file.endswith('.json'):
                        path = "{}{}".format(string, file)
                        my_list.append(path)
        algo = GraphAlgo(DiGraph())
        for i in my_list:
            if algo.load_from_json(i) is True:
                algo = GraphAlgo(algo.get_graph())
                self.list_algo.append(algo)
                self.list_graph.append(algo)
        for x in self.list_algo:
            self.assertIsNotNone(x.get_graph())
            self.assertTrue(x.get_graph().v_size() > 0)

    def test_save_to_json(self):
        """
        run by all the jsons file and check the save_to_json of the graph.
        This functions tests the save_to_json function for the class DiGraph
        """
        for x in self.list_algo:
            graph = x.get_graph()
            x.save_to_json("saveCheck.json")
            x.load_from_json("saveCheck.json")
            str1 = "".format(graph)
            str2 = "".format(x.get_graph())
            self.assertEqual(str1,str2)

    def test_shortest_path(self):
        """
        run by func2 and check the shortest_path of the graph.
        This functions tests the shortest_path function for the class DiGraph
        """
        self.func2()
        for x in self.list_algo:
            nodeSize = x.get_graph().v_size()
            for v in x.get_graph().get_v_keys():
                for ni in x.get_graph().get_v_keys():
                    if v != ni and ni in x.get_graph().all_out_edges_of_node(v).keys():
                        id = v
                        run = 0
                        for theList in x.shortest_path(v,ni)[1]:
                            if run > 0:
                                self.assertTrue(theList in x.get_graph().all_out_edges_of_node(id).keys())
                                id = theList
                            run += 1
                        id = v
                        run = 0
                        run = 0
                        for theList in x.shortest_path(v,nodeSize*5):
                            if run == 0:
                                self.assertEqual(theList,-1)
                            if run == 1:
                                self.assertEqual(len(theList),0)
                            run += 1

    def test_split_pos(self):
        """
        run by func2 and check the split_pos of the graph.
        This functions tests the split_pos function for the class DiGraph
        """
        self.func2()
        for x in self.list_algo:
            rand1 = r.randint(-100, 100)*100
            rand2 = r.randint(-100, 100)*100
            check = [rand1,rand2]
            my_list = [rand1,rand2]
            if check[0] < 0:
                check[0] += 0.04
            else:
                check[0] -= 0.04
            if check[1] < 0:
                check[1] += 0.04
            else:
                check[1] -= 0.04

            result = x.checkValue(my_list)
            self.assertEqual(result[0] == check[0],result[1] == check[1])

    def test_chack_value(self):
        """
        run by func2 and check the chack_value of the graph.
        This functions tests the chack_value function for the class DiGraph
        """
        self.func2()
        for x in self.list_algo:
            rand1 = format(r.randint(-100, 100) * 100)
            rand2 = format(r.randint(-100, 100) * 100)
            check = "{},{}".format(rand1, rand2)
            result = x.splitPos(check)
            self.assertEqual(result[0] == "{}".format(rand1), result[1] == "{}".format(rand2))
