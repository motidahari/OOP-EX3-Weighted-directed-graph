import json as Js
import math
from queue import PriorityQueue
from typing import List
import matplotlib.pyplot as plt
from src.DiGraph import DiGraph
from src import GraphInterface
from src.Node import Node
from src.GraphAlgoInterface import GraphAlgoInterface
import random as r

import matplotlib.path as mpath
import numpy as np





class GraphAlgo(GraphAlgoInterface):

    def strongly_connected_components2(self):
        therealist = []
        p = {}
        l = {}
        f = {}
        list = []
        i = 0
        for source in self.g.get_all_v().keys():
            if source not in f:
                queue = [source]
                while queue:
                    v = queue[-1]
                    if v not in p:
                        i = i + 1
                        p[v] = i
                    done = 1
                    v_nbrs = self.g.all_out_edges_of_node(v)
                    for w in v_nbrs:
                        if w not in p:
                            queue.append(w)
                            done = 0
                            break
                    if done == 1:
                        l[v] = p[v]
                        for w in v_nbrs:
                            if w not in f:
                                if p[w] <= p[v]:
                                    l[v] = min([l[v], p[w]])
                                else:
                                    l[v] = min([l[v], l[w]])
                        queue.pop()
                        if l[v] != p[v]:
                            list.append(v)
                        else:
                            f[v] = True
                            scc = [v]
                            while list and p[list[-1]] > p[v]:
                                k = list.pop()
                                f[k] = True
                                scc.append(k)
                            therealist.append(scc)

        return therealist
