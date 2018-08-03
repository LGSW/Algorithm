# Binary Search Tree
# Different Traverse methods
# (pre-order, in-order, post-order), (iteration, recursion) (level-order)

# Node Class
class TreeNode(object):
    def __init__(self, val = None):
        self.val = val
        self.left = None
        self.right = None

# Tree Class
class Tree():
    def __init__(self):
        self.root = TreeNode()

    def add(self, data):  # build a tree by using an array of nums
        node = TreeNode(data)
        if self.root.val == None:
            self.root = node
        else:
            myQueue = []
            treeNode = self.root
            myQueue.append(treeNode)
            while myQueue:
                treeNode = myQueue.pop(0)
                if not treeNode.left:
                    treeNode.left = node
                    return
                elif not treeNode.right:
                    treeNode.right = node
                    return
                else:
                    myQueue.append(treeNode.left)
                    myQueue.append(treeNode.right)

    def pre_order_recursion(self, root):  # recursively preorder
        if not root:
            return
        print(root.val)
        self.pre_order_recursion(root.left)
        self.pre_order_recursion(root.right)

    def in_order_recursion(self, root):  # recursively inorder
        if not root:
            return
        self.in_order_recursion(root.left)
        print(root.val)
        self.in_order_recursion(root.right)

    def post_order_recursion(self, root):  # recursively postorder
        if not root:
            return
        self.post_order_recursion(root.left)
        self.post_order_recursion(root.right)
        print(root.val)

    def pre_order_stack(self, root):  # iteratively preorder
        if not root:
            return
        myStack = []
        node = root
        while myStack or node:
            while node:
                print(node.val)
                myStack.append(node)
                node = node.left
            node = myStack.pop()
            node = node.right

    def in_order_stack(self, root):  # iteratively inorder
        if not root:
            return
        myStack = []
        node = root
        while myStack or node:
            while node:
                myStack.append(node)
                node = node.left
            node = myStack.pop()
            print(node.val)
            node = node.right

    def post_order_stack(self, root):  # iteratively postorder
        if not root:
            return
        myStack1 = []
        myStack2 = []
        node = root
        while myStack1 or node:
            while node:
                myStack2.append(node)
                myStack1.append(node)
                node = node.right
            node = myStack1.pop()
            node = node.left
        while myStack2:
            print(myStack2.pop().val)

    def level_order_queue(self, root):
        if not root:
            return
        myQueue = []
        node = root
        myQueue.append(node)
        while myQueue:
            node = myQueue.pop(0)
            print(node.val)
            if node.left:
                myQueue.append(node.left)
            if node.right:
                myQueue.append(node.right)


if __name__ == '__main__':
    datas = [1,2,3,4,5,6,7]
    tree = Tree()
    for data in datas:
        tree.add(data)

    print("recursively preorder traverse is:")
    tree.pre_order_recursion(tree.root)

    print("recursively inorder traverse is:")
    tree.in_order_recursion(tree.root)

    print("recursively postorder traverse is:")
    tree.post_order_recursion(tree.root)

    print("iteratively preorder traverse is:")
    tree.pre_order_stack(tree.root)

    print(" iteratively inorder traverse is:")
    tree.in_order_stack(tree.root)

    print(" iteratively postorder traverse is:")
    tree.post_order_stack(tree.root)

    print("recursively preorder traverse is:")
    tree.level_order_queue(tree.root)

