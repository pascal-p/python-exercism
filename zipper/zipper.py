"""
Creating a zipper for a binary tree.

Zippers are a purely functional way of navigating within a data structure and manipulating it.
They essentially contain a data structure and a pointer into that data structure (called the focus).
"""
class Zipper:
    @staticmethod
    def from_tree(tree):
        """
        get a zipper out of a rose tree, the focus is on the root node
        """
        return Zipper(_build_tree(tree))

    def __init__(self, tree):
        self._tree = tree
        self._root = tree   # for reset

    def value(self):
        """
        get the value of the focus node
        """
        return self._tree.data if self._tree is not None else None

    def set_value(self, value):
        self._tree.set_value(value)
        return self

    def left(self):
        """
        go to the left child of the focus node (I assume)
        """
        self._tree = self._tree.left
        return self._retref()

    def set_left(self, hvalue):
        """
        set left node of the focus node (I assume)
        """
        if hvalue is not None:
            self._tree.left = _build_tree(hvalue)
        else:
           self._tree.left = None
        return self

    def right(self):
        self._tree = self._tree.right
        return self._retref()

    def set_right(self, hvalue):
        if hvalue is not None:
            self._tree.right = _build_tree(hvalue)
        else:
            self._tree.right = None
        return self

    def up(self):
        """
        got to parent of focus node
        """
        self._tree = self._tree.parent
        return self._retref()

    def reset(self):
        self._tree = self._root
        return self

    def to_tree(self):
        """
        get the rose tree out of the zipper
        """
        return _tree_to_hsh(self._root)

    def _retref(self):
        return self if self._tree is not None else None


class TreeNode:
    def __init__(self, data, parent=None, left=None, right=None):
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right

    def set_value(self, value):
        self.data = value
        return self

    def __str__(self):
        fmt = 'TreeNode(data={}, left={}, right={})'
        return fmt.format(self.data, self.left, self.right)

#
# Internal Helpers
#

def _build_tree(treehsh):
    while treehsh is not None:
        v = treehsh["value"]
        ln = _build_tree(treehsh["left"])
        rn = _build_tree(treehsh["right"])
        cnode = TreeNode(v, left=ln, right=rn)
        if cnode.left is not None:
            cnode.left.parent = cnode
        if cnode.right is not None:
            cnode.right.parent = cnode
        return cnode

def _tree_to_hsh(tree):
    if tree is None:
        return None
    return {
        "value": tree.data,
        "left": _tree_to_hsh(tree.left),
        "right": _tree_to_hsh(tree.right)
    }
