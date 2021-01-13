from unittest import TestCase
from src.GraphAlgo import GraphAlgo
from src.DiGraph import DiGraph
from os import walk
import glob
import os
from pathlib import Path
import random as r

class TestGraphAlgo(TestCase):
    list_algo = []
    list_graph = []


    def func1(self):
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
                break
    def func2(self):
        graph = DiGraph()
        for x in range(7):
            graph.add_node(x)
        for x in graph.get_all_values():
            graph.add_edge(x.getKey(), x.getKey() + 1, x.getKey() + 1)

        graph.add_node(8)
        graph.add_node(9)
        algo = GraphAlgo(graph)
        self.list_algo.append(algo)
        self.list_graph.append(algo)

    def setUp(self):
        # self.func1()
        self.func2()
        # my_list = []
        # dir_path = os.path.dirname(os.path.realpath(__file__))
        # parent = Path(dir_path).parent
        # my_path = ["/Graphs/Graphs_no_pos/", "/Graphs/Graphs_on_circle/", "/Graphs/Graphs_random_pos/"]
        # for x in my_path:
        #     string = "{}{}".format(parent, x)
        #     for root, dirs, files in os.walk(string):
        #         for file in files:
        #             if file.endswith('.json'):
        #                 path = "{}{}".format(string, file)
        #                 my_list.append(path)
        # algo = GraphAlgo(DiGraph())
        # for i in my_list:
        #     if algo.load_from_json(i) is True:
        #         algo = GraphAlgo(algo.get_graph())
        #         self.list_algo.append(algo)
        #         break



    def test_create_transposed_graph(self):
        for i in self.list_algo:
            for node in i.get_graph().get_all_v().keys():
                 self.assertEqual(i.get_graph().all_out_edges_of_node(node).keys(),i.get_transposed_graph().all_in_edges_of_node(node).keys())

    def test_set_all_tags(self):
        for i in self.list_algo:
            print(i.get_graph())
            i.setAllTags(100)
        for i in i.getAllTags().values():
            self.assertEqual(100,i)

    def test_get_all_tags(self):
        for i in self.list_algo:
            print(i.get_graph())
            i.setAllTags(100)
        for i in i.getAllTags().values():
            self.assertEqual(100,i)

    def test_set_all_weight_and_info(self):
        for i in self.list_algo:

            i.setAllWeightAndInfo(100)
        for i in i.get_graph().get_all_v().values():
            self.assertEqual(100,i.getWeight())

    def test_get_graph(self):
        i = 0
        for i in self.list_graph:
            print("i = {}".format(i))
            print("list_algo.pop = {}".format(self.list_algo[0].get_graph()))
            # self.assertEqual(self.i,self.list_algo[i])
            i += 1

        pass

    def test_load_from_json(self):
        pass

    def test_save_to_json(self):
        pass

    def test_shortest_path(self):
        pass

    def test_connected_component(self):
        pass

    def test_connected_components(self):
        pass

    def test_plot_graph(self):
        pass

    def test_chack_value(self):
        pass

    def test_split_pos(self):
        pass
