# Implement Binary tree
# Find height of a given tree
# Perform Pre-order, Post-order, In-order traversal
# Function to print all the leaves in a given binary tree
# Implement BFS (Breath First Search) and DFS (Depth First Search)
# Find sum of all left leaves in a given Binary Tree
# Find sum of all nodes of the given perfect binary tree
# Count subtress that sum up to a given value x in a binary tree
# Find maximum level sum in Binary Tree
# Print the nodes at odd levels of a tree


class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def height(self, node):
        if node is None:
            return 0
        else:
            left_height = self.height(node.left)
            right_height = self.height(node.right)
            return max(left_height, right_height) + 1

    def print_preorder(self, node):
        if node:
            print(node.val)
            self.print_preorder(node.left)
            self.print_preorder(node.right)

    def print_inorder(self, node):
        if node:
            self.print_inorder(node.left)
            print(node.val)
            self.print_inorder(node.right)

    def print_postorder(self, node):
        if node:
            self.print_postorder(node.left)
            self.print_postorder(node.right)
            print(node.val)

    def print_leaves(self, node):
        if node is None:
            return
        if node.left is None and node.right is None:
            print(node.val)
            return
        if node.left:
            self.print_leaves(node.left)
        if node.right:
            self.print_leaves(node.right)

    def bfs(self):
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            print(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def dfs(self):
        stack = [self.root]
        while stack:
            node = stack.pop()
            print(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    def sum_left_leaves(self, node):
        if node is None:
            return 0
        if node.left and node.left.left is None and node.left.right is None:
            return node.left.val + self.sum_left_leaves(node.right)
        else:
            return self.sum_left_leaves(node.left) + self.sum_left_leaves(node.right)

    def sum_nodes(self, node):
        if node is None:
            return 0
        else:
            return node.val + self.sum_nodes(node.left) + self.sum_nodes(node.right)

    def count_subtrees_sum_x(self, node, x):
        if node is None:
            return 0
        count = 0
        if node.left:
            count += self.count_subtrees_sum_x(node.left, x)
        if node.right:
            count += self.count_subtrees_sum_x(node.right, x)
        if node.val == x or (node.left and node.left.val == x - node.val) or (node.right and node.right.val == x - node.val):
            count += 1
        return count

    def max_level_sum(self, node):
        if node is None:
            return 0
        queue = [node]
        max_sum = node.val
        while queue:
            level_sum = 0
            for i in range(len(queue)):
                node = queue.pop(0)
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            max_sum = max(max_sum, level_sum)
        return max_sum

    def print_odd_level_nodes(self, node, level):
        if node is None:
            return
        if level % 2 != 0:
            print(node.val)
        self.print_odd_level_nodes(node.left, level+1)
        self.print_odd_level

# create a binary tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

# find the height of the tree
print("Height of the tree:", tree.height(tree.root))

# perform various traversals
print("Preorder traversal:")
tree.print_preorder(tree.root)
print("Inorder traversal:")
tree.print_inorder(tree.root)
print("Postorder traversal:")
tree.print_postorder(tree.root)

# print all leaves of the tree
print("Leaves of the tree:")
tree.print_leaves(tree.root)

# perform BFS and DFS
print("BFS traversal:")
tree.bfs()
print("DFS traversal:")
tree.dfs()

# find sum of all left leaves
print("Sum of left leaves:", tree.sum_left_leaves(tree.root))

# find sum of all nodes
print("Sum of all nodes:", tree.sum_nodes(tree.root))

# count subtrees that sum up to a given value
x = 10
count = tree.count_subtrees_sum_x(tree.root, x)
print(f"Number of subtrees that sum up to {x}: {count}")

# find maximum level sum
print("Maximum level sum:", tree.max_level_sum(tree.root))

# print nodes at odd levels
print("Nodes at odd levels:")
tree.print_odd_level_nodes(tree.root, 1)
