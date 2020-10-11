class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        fmt = 'TreeNode(data={}, left={}, right={})'
        return fmt.format(self.data, self.left, self.right)


class BinarySearchTree:
    def __init__(self, tree_data):
        if tree_data is None or len(tree_data) == 0:
            self.root = None
            return

        self.root = TreeNode(tree_data[0])
        for pnode in tree_data[1:]:
            self._insert_node(self.root, self.root, TreeNode(pnode))

    def data(self):
        return self.root

    def sorted_data(self, rev=False):
        if rev:
            return self._dfs_inf_rev(self.root, [])
        return self._dfs_inf(self.root, [])

    def _dfs_inf(self, root, l):
        """
        dfs traversal using infix-order: left / root / right
        """
        if root == None: return l
        self._dfs_inf(root.left, l)
        l.append(root.data)          # do something with root
        return self._dfs_inf(root.right, l)

    def _dfs_inf_rev(self, root, l):
        """
        dfs traversal using infix-order: right / root / left
        """
        if root == None: return l
        self._dfs_inf_rev(root.right, l)
        l.append(root.data)          # do something with root
        return self._dfs_inf_rev(root.left, l)

    def _dfs_post(self, root, l):
        """
        dfs traversal using post order: left / right / root
        """
        if root == None: return l
        self._dfs_pre(root.left, l)
        self._dfs_pre(root.right, l)
        l.append(root.data)          # do something with root

    def _insert_node(self, parent, root, node):
        if node == None: return

        def _insert_(parent, root, d='left'):
            if root == None:
                if d == 'left': parent.left = node
                else: parent.right = node
                return

            if node.data < root.data:
                return _insert_(root, root.left)

            elif node.data > root.data:
                return _insert_(root, root.right, 'right')

            else:
                # insert left!
                return _insert_(root, root.left)

        return _insert_(parent, root)
