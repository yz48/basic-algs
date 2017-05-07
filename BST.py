class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


def insert(root, node):
    if root is None:
        root = node

    else:
        if root.val > node.val:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)

        else:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
def in_order_print(root):
    if not root:
        return
    in_order_print(root.left)
    print root.val
    in_order_print(root.right)

def pre_order_print(root):
    if not root:
        return
    print root.val
    pre_order_print(root.left)
    pre_order_print(root.right)

r = Node(3)
insert(r, Node(7))
insert(r, Node(1))
insert(r, Node(5))

print "in order:"
in_order_print(r)

print "pre order"
pre_order_print(r)
