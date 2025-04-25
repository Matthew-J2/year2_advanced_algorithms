"""
Time complexity:
https://www.freecodecamp.org/news/binary-search-trees-bst-explained-with-examples/
Recursion limit:
https://docs.python.org/3/library/sys.html#sys.setrecursionlimit
"""


class Node:
    """ Node class"""

    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


""" BST class with insert and display methods. Display pretty prints the tree."""


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, cur_node):
        if data < cur_node.data:
            if cur_node.left is None:
                cur_node.left = Node(data)
            else:
                self._insert(data, cur_node.left)
        elif data > cur_node.data:
            if cur_node.right is None:
                cur_node.right = Node(data)
            else:
                self._insert(data, cur_node.right)
        else:
            print("Value already present in tree")

    def display(self, cur_node):
        # Fixes Nonetype error in given code
        if self.root is None:
            return None
        lines, _, _, _ = self._display(cur_node)
        for line in lines:
            print(line)

    def _display(self, cur_node):

        if cur_node.right is None and cur_node.left is None:
            line = '%s' % cur_node.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        if cur_node.right is None:
            lines, n, p, x = self._display(cur_node.left)
            s = '%s' % cur_node.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        if cur_node.left is None:
            lines, n, p, x = self._display(cur_node.right)
            s = '%s' % cur_node.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        left, n, p, x = self._display(cur_node.left)
        right, m, q, y = self._display(cur_node.right)
        s = '%s' % cur_node.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    def find_i(self, target):
        """
        Checks if the tree is empty.
        While the current node exists, check if the current node's data is greater,
        smaller, or the same as the target value.
        If the value is the same as the target return True as we have found the value
        If the current node is larger than the target, change the current node to the
        left child node, if the current node is smaller than the target, change the
        current node to the right child node.
        If the target node is not found, and the current node is set to None, breaking
        the while loop, return False.
        """
        if self.root:
            current_node = self.root
            while current_node is not None:
                if current_node.data == target:
                    return True
                elif current_node.data > target:
                    current_node = current_node.left
                else:
                    current_node = current_node.right
            return False
        else:
            return None

    def find_r(self, target):
        """
        Checks if the tree is empty.
        If the tree is not empty it recursively calls the private method _find_r to
        perform the binary search on the tree.
        If the target value is found (_find_r() returns True), True is returned, otherwise
        False is returned.
        If the tree object has no root and is therefore empty, it returns None.
        """
        if self.root:
            if self._find_r(target, self.root):
                return True
            return False
        else:
            return None

    def _find_r(self, target, cur_node):
        """
        Checks if the current node's value is greater or less than the target.
        If this is true and a child node exists on the correct side of the tree relative
        to the current node's value and the target, it recursively calls itself using the
        respective child node as the new current node.
        If the current node is equal to the target, it returns true to find_r(), leading
        find_r() to also return True.
        Otherwise, the function is broken without a return, leading to None being returned by
        all layers of recursion.
        As None is falsy, this leads to the if statement in find_r() being rejected, and False
        being returned by find_r().
        """
        if target > cur_node.data and cur_node.right:
            return self._find_r(target, cur_node.right)
        elif target < cur_node.data and cur_node.left:
            return self._find_r(target, cur_node.left)
        if target == cur_node.data:
            return True

    def remove(self, target):
        """
        Checks if the tree is empty, if so returns False

        If the tree root is the target value, check if the root has any children, and change the root
        to be the child value or call the function to handle two children, if there are no children set
        it to None.

        If the tree root isn't the target value, then set the root to be the current node.

        The tree is then searched for the target value. If it is not found False is returned.

        If the target node has no children, the previous node's edge to the target node is removed.

        If the target node has a child to the left or right, the previous node's edge is set to the left
        or right depending on if the target node's child is smaller or larger than it.

        If the target has a left and right child, call if_left_and_right() to remove it.
        """
        # If no tree
        if self.root is None:
            return False
        # If tree root is target
        elif self.root.data == target:
            if self.root.left is None and self.root.right is None:
                self.root = None
            elif self.root.left and self.root.right is None:
                self.root = self.root.left
            elif self.root.left is None and self.root.right:
                self.root = self.root.right
            elif self.root.left and self.root.right:
                self.if_left_and_right(self.root)

        # If tree root is not target
        parent = None
        node = self.root

        while node and node.data != target:
            parent = node
            if target < node.data:
                node = node.left
            elif target > node.data:
                node = node.right

        # Case 1: target not found
        if node is None or node.data != target:
            return False

        # Case 2: target has no children
        elif node.left is None and node.right is None:
            if target < parent.data:
                parent.left = None
            else:
                parent.right = None
            return True

        # Case 3: Target has left child only
        elif node.left and node.right is None:
            if target < parent.data:
                parent.left = node.left
            else:
                parent.right = node.left
            return True

        # Case 4 to be implemented: Right child only
        elif node.right and node.left is None:
            if target > parent.data:
                parent.right = node.right
            else:
                parent.left = node.right
            return True

        # Case 5: Target has left and right children
        else:
            self.if_left_and_right(node)
            return True

    def if_left_and_right(self, node):
        """
        Used in the case where target has left and right children.

        Finds the leftmost node to the right of the target and replaces
        the target node's data with this node's data.

        Then updates the parent node of the replaced node to connect to
        any node below the replaced node in the tree.
        """
        del_node_parent = node
        del_node = node.right

        while del_node.left:
            del_node_parent = del_node
            del_node = del_node.left

        node.data = del_node.data

        if del_node.right:
            if del_node_parent.data > del_node.data:
                del_node_parent.left = del_node.right
            else:
                del_node_parent.right = del_node.right

        else:
            if del_node.data < del_node_parent.data:
                del_node_parent.left = None
            else:
                del_node_parent.right = None


def main():
    # example calls, which construct and display the tree
    bst = BinaryTree()
    bst.insert(4)
    bst.insert(2)
    bst.insert(6)
    bst.insert(1)
    bst.insert(3)
    bst.insert(5)
    bst.insert(7)
    bst.insert(9)
    bst.insert(8)
    bst.insert(10)
    bst.insert(12)
    bst.insert(11)
    bst.insert(13)
    bst.insert(14)
    bst.insert(15)
    bst.insert(100)
    bst.insert(200)

    print("Original tree:")
    bst.display(bst.root)
    print("Check for 5 and 1000:")
    print(bst.find_r(5))
    print(bst.find_i(1000))
    print("Remove 4, 5, 12, 13, 1000, -1:")
    print(bst.remove(4))
    print(bst.remove(5))
    print(bst.remove(12))
    print(bst.remove(13))
    print(bst.remove(1000))
    print(bst.remove(-1))

    bst.display(bst.root)

    bst2 = BinaryTree()
    print("Second BST.")
    print("Remove from empty tree:")
    print(bst2.remove(56))
    print("Insert 2 then 1, remove 2.")
    bst2.insert(2)
    bst2.insert(1)
    print(bst2.remove(2))
    bst2.display(bst2.root)



if __name__ == "__main__":
    main()
