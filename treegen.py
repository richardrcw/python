import math
import random


class tree:
    def _insert(self, root, num):
        if num < root[1]:
            if root[0]:
                return 1 + _insert(root[0], num)
            else:
                root[0] = [None, num, None]
                return 1
        else:
            if root[2]:
                return 1 + _insert(root[2], num)
            else:
                root[2] = [None, num, None]
                return 1

    def insert(self, num):
        _insert(self, self._root, num)

    def _ptree(self, root, center, depth):
        if depth == 1:
            print('\t'*(center - self._tabs), end=str(root[1]))
            self._tabs = center
        else:
            if root[0]:
                ptree(root[0],center-1,depth-1)
            if root[2]:
                ptree(root[2],center+1,depth-1)

    def ptree(self):
        self.ptree(self._root, self._depth, self._depth)

    def __init__(self, numNodes):
        _tabs=0
        _numNodes = numNodes
        _randTop = 10 ** (math.ceil(math.log10(_numNodes)) + 1)
        _numSet = set()
        while len(_numSet) < _numNodes:
            _numSet.add(random.randint(1, _randTop))
        _root = [None, _numSet.pop(), None]

        _depth = 1
        for i in _numSet:
            _depth = max(_depth, 1 + _insert(root, i))




    for printLevel in range(1, depth + 1):
        tabs=0
        ptree(root, depth, printLevel)
        print()
