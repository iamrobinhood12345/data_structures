"""Implementation of a binary search tree."""


class BinarySearchTree(object):
    """Binary Search Tree."""

    def __init__(self):
        """Init bst."""
        self._values = {}
        self._root_node = None

    def insert(self, value):
        """insert a values, ignores if value is already in bst."""
        self._values.setdefault(value, True)
        if self._root_node is None:
            self._root_node = Node(value)


class Node(object):
    """Node."""

    def __init__(self, val, left=None, right=None):
        """Init node."""
        self.value = val