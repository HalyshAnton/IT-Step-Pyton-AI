class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._recursive_insert(data, self.root)

    def _recursive_insert(self, data, current_node):
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                self._recursive_insert(data, current_node.left)
        else:
            if current_node.right is None:
                current_node.right = Node(data)
            else:
                self._recursive_insert(data, current_node.right)

    def min(self):
        if self.root is None:
            print('Дерево порожнє')
            return

        node = self.root

        while node.left is not None:
            node = node.left

        return node.data

    def max(self):
        if self.root is None:
            print('Дерево порожнє')
            return

        node = self.root

        while node.right is not None:
            node = node.right

        return node.data

    def __contains__(self, data):
        if self.root is None:
            print('Дерево порожнє')
            return

        node = self.root

        while node:
            if node.data == data:
                return True

            if data < node.data:
                node = node.left
            else:
                node = node.right

        return False

    def print(self):
        if self.root is None:
            print('Дерево порожнє')
            return

        self._inorder(self.root)
        print()

    def _inorder(self, node):
        if node is not None:
            self._inorder(node.left)
            print(node.data, end=' ')
            self._inorder(node.right)
    
    def _preorder(self, node):
        if node is not None:
            print(node.data, end=' ')
            self._preorder(node.left)
            self._preorder(node.right)
    
    def _postorder(self, node):
        if node is not None:
            self._postorder(node.left)
            self._postorder(node.right)
            print(node.data, end=' ')


tree = BinaryTree()
tree.insert(3)
tree.insert(2)
tree.insert(4)
tree.insert(9)
tree.insert(7)
tree.insert(6)

print(f'{tree.min()=}')
print(f'{tree.max()=}')
print(f'{4 in tree=}')
print(f'{8 in tree=}')

tree.print()

