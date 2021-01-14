class Node:
    key = int()
    info = str()
    tag = int()
    weight = float()
    pos = str()

    def __init__(self, key: int, info=None, tag=None, weight=None, pos=None):
        """
        constructor - create new node
        @param key - the key of the node
        @param tag - the tag of the node
        @param info - the info of the node
        @param location - the location of the node
        @param weight - the weight of the node
        """
        self.key = int(key)
        self.info = "" if info is None else str(info)
        self.tag = 0 if tag is None else int(tag)
        self.weight = 0 if tag is None else float(weight)
        self.pos = "" if pos is None else self.createPos(pos)

    def createPos(self, pos: tuple):
        """"
        converts a tuple to a string value of the position of the node
        """
        string = "{},{},{}".format(pos[0], pos[1], pos[2])
        return string

    def getKey(self) -> int:
        """"
        get the key of the current node
        """
        return self.key


    def getPosAsString(self) -> str:
        """"
        get the pos as string of the current node
        """
        return self.pos

    def getPos(self) -> tuple:
        if self.pos == "":
            tuple = ()
            return tuple
        else:
            arr = self.pos.split(",")
            my_tuple = (float(arr[0]), float(arr[1]), float(arr[2]))
            return my_tuple

    def getInfo(self) -> str:
        """"
        get the Info of the current node
        """
        return self.info

    def getWeight(self) -> float:
        """"
        get the weight of the current node
        """
        return self.weight

    def getTag(self) -> int:
        """"
        get the tag of the current node
        """
        return self.tag

    def setInfo(self, info: str):
        """"
        set the info of the current node
        """
        self.info = info

    def setWeight(self, weight: float):
        """"
        set the weight of the current node
        """
        self.weight = weight

    def setPos(self, pos: tuple):
        """"
        set the pos of the current node and convert is to string
        """
        self.pos = self.createPos(pos)

    def setTag(self, tag: int):
        """"
        set the tag of the current node
        """
        self.tag = tag

    def __str__(self):
        return "#{0}, info: {1}, tag: {2}, weight: {3}, pos: {4}".format(self.key, self.info, self.tag, self.weight,
                                                                         self.pos)

    def __cmp__(self, other):
        """
        comparator for node by the weight
        """
        if other is None or not isinstance(other, Node) or self.weight > other.weight:
            return 1
        elif self.weight < other.weight:
            return -1
        else:
            return 0
