class Btree:

    def __init__(self, root_value, left=None, right=None):

        self.value = root_value
        self.left = left
        self.right = right

    def __str__(self):
        return self.value

    def other_name(self, level=0):

        print ' ' * level + (self.root_value)
        child.left(level+1)
        child.right(level+1)



def buildtree(inorder, preorder):

    root_val = preorder[0]
    left_size = inorder.index(root_val) # size of the left subtree

    if left_size > 0:
        left = buildtree(inorder[:left_size], preorder[1:left_size+1])
    else:
        left = None

    if (left_size + 1) < len(inorder):
        right = buildtree(inorder[left_size+1:], preorder[left_size+1:])
    else:
        right = None

    return Btree(root_val, left, right)


from collections import deque

def print_level_order(head, queue = deque()):
    if head is None:
        return
    print head.value
    [queue.append(node) for node in [head.left, head.right] if node]
    if queue:
        print_level_order(queue.popleft(), queue)



t =  buildtree("acbd","abcd")

print_level_order(t)


# Unsolved
