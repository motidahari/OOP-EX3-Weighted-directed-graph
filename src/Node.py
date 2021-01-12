import copy as c



class Node:
    key = int()
    info = str()
    tag = int()
    weight = float()
    pos = str()

    def __cmp__(self, other):
        if other is None or not isinstance(other, Node) or self.weight > other.weight:
            return 1
        elif self.weight < other.weight:
            return -1
        else:
            return 0

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

    def createPos(self,pos : tuple):
        string = "{},{},{}".format(pos[0], pos[1], pos[2])
        return string


    def getKey(self) -> int:
        return self.key

    def getPos(self) -> tuple:
        return self.pos

    def getInfo(self) -> str:
        return self.info

    def getWeight(self) -> float:
        return self.weight

    def getTag(self) -> int:
        return self.tag

    def setInfo(self, info: str):
        self.info = info

    def setWeight(self, weight: float):
        self.weight = weight

    def setPos(self, pos: tuple):
        self.pos = self.createPos(pos)

    def setTag(self, tag: int):
        self.tag = tag

    def __str__(self):
        return "#{0}, info: {1}, tag: {2}, weight: {3}, pos: {4}".format(self.key,self.info,self.tag,self.weight,self.pos)

# def __init__(self):
    #     """
    #     constructor - create new node
    #     """
    #     self.key = 0
    #     self.info = ""
    #     self.tag = 0
    #     self.weight = 0
    #
    # def __init__(self, *args, **kwargs):
    #
    #
    # def __init__(self, key: int):
    #     """
    #     constructor - create new node
    #     @param key - the key of the node
    #     """
    #     self.key = key
    #     self.info = ""
    #     self.tag = 0
    #     self.weight = 0
    # def __init__(self, other):
    #     """
    #     constructor - create new node
    #     @param o - the object data of the node
    #     """
    #     self.key = other.key
    #     self.info = other.info
    #     self.tag = other.tag
    #     self.weight = other.weight