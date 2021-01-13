from unittest import TestCase
from src.DiGraph import DiGraph
from src.Node import Node
import random as r


class TestNode(TestCase):
    listNodes = []

    def testInit(self):
        i = 0
        my_list = []
        for x in range(200):
            my_list.append(Node(x))
        self.assertEqual(len(my_list), 200)
        for x in my_list:
            self.assertIsNotNone(x)
        self.listNodes = my_list

    def test_create_pos(self):
        self.testInit()
        for x in self.listNodes:
            a = r.random()*100
            b = r.random()*50
            c = r.random()*20
            pos = "{},{},{}".format(a,b,c)
            self.assertEqual(x.createPos((a,b,c)),pos)

    def test_get_key(self):
        self.testInit()
        i = 0
        for x in self.listNodes:
            self.assertEqual(x.getKey(),i)
            i += 1

    def test_get_pos(self):
        self.testInit()
        for x in self.listNodes:
            a = r.random()*100
            b = r.random()*50
            c = r.random()*20
            pos = "{},{},{}".format(a,b,c)
            x.setPos((a,b,c))
            self.assertEqual(x.getPos(),pos)

    def test_get_info(self):
        self.testInit()
        for x in self.listNodes:
            a = r.random()*100
            b = r.random()*50
            c = r.random()*20
            string = "check{},{},{}".format(a,b,c)
            x.setInfo(string)
            self.assertEqual(x.getInfo(),string)

    def test_get_weight(self):
        self.testInit()
        for x in self.listNodes:
            a = r.random() * 100
            x.setWeight(a)
            self.assertEqual(x.getWeight(), a)

    def test_get_tag(self):
        self.testInit()
        for x in self.listNodes:
            a = int(r.random() * 100)
            x.setTag(a)
            self.assertEqual(x.getTag(), a)

    def test_set_info(self):
        self.testInit()
        for x in self.listNodes:
            a = int(r.random() * 100)
            b = int(r.random() * 100)
            c = int(r.random() * 100)
            string = x.getInfo()
            stringSet = "check{},{},{}".format(a, b, c)
            x.setInfo(stringSet)
            self.assertEqual(x.getInfo(), stringSet)
            self.assertNotEqual(x.getInfo(), string)

    def test_set_weight(self):
        self.testInit()
        for x in self.listNodes:
            a = int(r.random() * 100)+1
            weight = x.getWeight()
            x.setWeight(a)
            self.assertEqual(x.getWeight(), a)
            self.assertNotEqual(x.getWeight(), weight)

    def test_set_pos(self):
        self.testInit()
        for x in self.listNodes:
            a = int(r.random() * 100)
            b = int(r.random() * 100)
            c = int(r.random() * 100)
            getPos = x.getPos()
            newPos = "{},{},{}".format(a, b, c)
            x.setPos((a,b,c))
            self.assertEqual(x.getPos(), newPos)
            self.assertNotEqual(x.getPos(), getPos)

    def test_set_tag(self):
        self.testInit()
        for x in self.listNodes:
            a = int(r.random() * 100)
            b = int(r.random() * 100)
            c = int(r.random() * 100)
            getTag = x.getTag()
            newTag = 100
            x.setTag(newTag)
            self.assertEqual(x.getTag(), newTag)
            self.assertNotEqual(x.getTag(), getTag)