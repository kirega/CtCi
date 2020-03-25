"""
The idea is to create a full binary tree with the following methods:
- create a binary tree
- insert into a binary tree
- remove an item from a binary tree
- search the tree 

the tree being created 
           8 
         /   \ 
        6      10 
     /    \    /  \ 
    4     7   9   12  
   /
   3
"""


def in_order(root):
    if root is not None:
        in_order(root.left)
        print(root.value,)
        in_order(root.right)


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        self.visited = False


class BinaryTree:
    def __init__(self):
        """
        Create the binary tree here
        """
        self.root = Node(8)
        self.root.left = Node(6)
        self.root.right = Node(10)
        self.root.left.left = Node(4)
        self.root.left.right = Node(7)
        self.root.left.left.left = Node(3)
        self.root.right.left = Node(9)
        self.root.right.right = Node(12)

    def insert(self, key):
        """
        Given a key find the correct positions to include it in the binary tree, this does not care about the binary tree
        remaining a BST
        :return:
        """
        queue = []
        node = self.root
        while node:
            if node.left:
                queue.insert(0, node.left)
            else:
                node.left = Node(key)
                return
            if node.right:
                queue.insert(0, node.right)
            else:
                node.right = Node(key)
                return
            if queue:
                node = queue.pop()
            else:
                break

    @staticmethod
    def insert_bst(node, key):
        """
        This kind of insertion should ensure that the tree remains searchable and the order is maintained
        :return:
        """
        if not node:
            return Node(key)
        if node.value == key:
            raise Exception("BST must have no duplicate", key)
        if node.value < key:
            if not node.right:
                node.right = Node(key)
                return
            BinaryTree.insert_bst(node.right, key)
        else:
            if not node.left:
                node.left = Node(key)
                return
            BinaryTree.insert_bst(node.left, key)

    @staticmethod
    def remove(root, key):
        if not root:
            return root
        # if root.value == key:
        #     return root
        if root.value < key:
            root.right = BinaryTree.remove(root.right, key)
        elif root.value > key:
            root.left = BinaryTree.remove(root.left, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = BinaryTree.min_value_node(root.right)
            root.key = temp.key
            root.right = BinaryTree.remove(root.right, temp.key)
        return root

    @staticmethod
    def min_value_node(node):
        current = node
        # loop down to find the leftmost leaf
        while current.left:
            current = current.left
        return current

    def print(self, root=None):
        """
            breadth first traversal with printing
            expected output is :
            8 6 10 4 7 9 12 3
        :return:
        """
        if root:
            self.bfs(root)
        else:
            self.bfs(self.root)

    def print_dfs(self):
        """
        depth first traversal with printing
        expected output is :
        8 6 4 3 7 10 9 12
        :return:
        """
        self.dfs(self.root)

    @staticmethod
    def bfs(node):
        """
        By performing this search it is trivial to perform a search on this
        :param node:
        :return:
        """
        queue = []
        while node:
            print(node.value)
            if node.left:
                queue.insert(0, node.left)
            if node.right:
                queue.insert(0, node.right)
            if queue:
                node = queue.pop()
            else:
                break

    @staticmethod
    def dfs(node):
        """
          By performing this search it is trivial to perform a search on this
          :param node:
          :return:
          """
        while node and node.visited == False :
            print(node.value)
            node.visited = True
            if node.left:
                BinaryTree.dfs(node.left)
            if node.right:
                BinaryTree.dfs(node.right)


bin_tree = BinaryTree()
print("------Before any edits--------")
in_order(bin_tree.root)
# bin_tree.print()
print("------After some Edits--------")
bin_tree.root = bin_tree.remove(bin_tree.root, 4)
in_order(bin_tree.root)
# bin_tree.print_dfs()
# print("--------------")
# bin_tree.insert(16)
# bin_tree.print()

# bin_tree.insert_bst(bin_tree.root, 12)
# bin_tree.insert_bst(bin_tree.root, 2)
# bin_tree.print_dfs()

# in_order(root)

# bin_tree.print()
