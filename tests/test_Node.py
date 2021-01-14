from unittest import TestCase
from src.Node import Node
import random as r


class TestNode(TestCase):
    """
    Unitest for class Node, using setUp() method to create Node objects before each test is executed.
    """

    def setUp(self):
        """
        Computing 200 new Node objects, and checking if the each node had being created successfully without any error
        by the lenght of the list to which the Nodes were added.
        """
        i = 0
        my_list = []
        for x in range(200):
            my_list.append(Node(x))
        self.assertEqual(len(my_list), 200)
        for x in my_list:
            self.assertIsNotNone(x)
        self.listNodes = my_list

    def test_create_pos(self):
        """
        test to create 3D positions to the Node.
        :return: asserts if the two strings are equal.
        """
        for x in self.listNodes:
            a = r.random()*100
            b = r.random()*50
            c = r.random()*20
            pos = "{},{},{}".format(a,b,c)
            self.assertEqual(x.createPos((a,b,c)),pos)

    def test_get_key(self):
        """
        test for get_key() method for Node object while iterating over the list created in setUp() method.
        In case one of the nodes key doesn't match i in the range of indexes raises not equal error.
        """
        i = 0
        for x in self.listNodes:
            self.assertEqual(x.getKey(),i)
            i += 1

    def test_get_pos(self):
        """
        Iterating over the list of Nodes and comparing between the two 3D pos strings, in case they aren't equal raises
        a not equal error.
        """
        for x in self.listNodes:
            a = r.random()*100
            b = r.random()*50
            c = r.random()*20
            pos = "{},{},{}".format(a,b,c)
            x.setPos((a,b,c))
            self.assertEqual(x.getPosAsString(),pos)

    def test_get_info(self):
        """
        Iterating over the list of Nodes assigning info and then comparing between the info strings, in case they
        aren't equal raises a not equal error.
        """
        for x in self.listNodes:
            a = r.random()*100
            b = r.random()*50
            c = r.random()*20
            string = "check{},{},{}".format(a,b,c)
            x.setInfo(string)
            self.assertEqual(x.getInfo(),string)

    def test_get_weight(self):
        """
        Iterating over the list of Nodes and assigning the random number as the weight,then comparing between the
        random number and the value returned by get_weight() method.
        """
        for x in self.listNodes:
            a = r.random() * 100
            x.setWeight(a)
            self.assertEqual(x.getWeight(), a)

    def test_get_tag(self):
        """
        Iterating over the list of Nodes and assigning the random number as the tag,then comparing between the
        random number and the value returned by get_tag() method.
        """
        for x in self.listNodes:
            a = int(r.random() * 100)
            x.setTag(a)
            self.assertEqual(x.getTag(), a)

    def test_set_info(self):
        """
        Iterating over the list of Nodes and assigning the random string as the info,then comparing between the
        two to check if the value returned by get_info() method is equal to the stringSet created and the old info string,
        raises a not equal error in case the new stringSet isn't equal to the value return by the get_info() method
        meaning the set function didn't work.
        """
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
        """
        Iterating over the list of Nodes and assigning the random number as the weight,then comparing between the
        random number and the value returned by get_weight() method to confirm set_weight() function worked properly.
        """
        for x in self.listNodes:
            a = int(r.random() * 100)+1
            weight = x.getWeight()
            x.setWeight(a)
            self.assertEqual(x.getWeight(), a)
            self.assertNotEqual(x.getWeight(), weight)

    def test_set_pos(self):
        """
        Iterating over the list of Nodes and assigning the random number as the pos,then comparing between the
        random number and the value returned by get_pos() method to confirm set_pos() function worked properly.
        and between the old pos that was assigned to the Node.
        """
        for x in self.listNodes:
            a = int(r.random() * 100)
            b = int(r.random() * 100)
            c = int(r.random() * 100)
            getPos = x.getPosAsString()
            newPos = "{},{},{}".format(a, b, c)
            x.setPos((a,b,c))
            self.assertEqual(x.getPosAsString(), newPos)
            self.assertNotEqual(x.getPosAsString(), getPos)

    def test_set_tag(self):
        """
        Iterating over the list of Nodes and assigning the random number as the tag,then comparing between the
        random number and the value returned by get_tag() method to confirm set_tag() function worked properly.
        and between the old tag that was assigned to the Node.
        """
        for x in self.listNodes:
            a = int(r.random() * 100)
            b = int(r.random() * 100)
            c = int(r.random() * 100)
            getTag = x.getTag()
            newTag = 100
            x.setTag(newTag)
            self.assertEqual(x.getTag(), newTag)
            self.assertNotEqual(x.getTag(), getTag)

