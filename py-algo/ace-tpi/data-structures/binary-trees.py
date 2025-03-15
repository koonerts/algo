from collections import deque


class BinaryTreeNode:
    def __init__(self, data, left=None, right=None, parent=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right, self.next = None, None, None

    def print_level_order(self):
        next_level_root = self
        while next_level_root:
            current = next_level_root
            next_level_root = None
            while current:
                print(str(current.val) + " ", end="")
                if not next_level_root:
                    if current.left:
                        next_level_root = current.left
                    elif current.right:
                        next_level_root = current.right
                current = current.next
            print()


def are_identical(root1: BinaryTreeNode, root2: BinaryTreeNode):
    if root1 is None and root2 is None:
        return True

    if root1 and root2:
        return (
            root1.data == root2.data
            and are_identical(root1.left, root2.left)
            and are_identical(root1.right, root2.right)
        )
    else:
        return False


class InorderIterator:
    """
    TODO: Come back to -> https://www.educative.io/module/lesson/data-structures-in-python/m7wOjD0DlBO
    """

    def __init__(self, root: BinaryTreeNode):
        self.stack = []
        self.populate_stack(root)

    def populate_stack(self, root: BinaryTreeNode):
        while root:
            self.stack.append(root)
            root = root.left

    def hasNext(self):
        return len(self.stack) > 0

    def getNext(self):
        if not self.hasNext():
            return None

        val = self.stack.pop()
        self.populate_stack(val.right)
        return val


def inorder_using_iterator(root: BinaryTreeNode):
    iter = InorderIterator(root)
    result = ""
    while iter.hasNext():
        ptr = iter.getNext()
        result += str(ptr.data) + " "
    return result


def inorder_iterative(root: BinaryTreeNode):
    result = ""
    if not root:
        return result

    def populate_stack(node: BinaryTreeNode):
        while node:
            stk.append(node)
            node = node.left

    stk = []
    populate_stack(root)
    while stk:
        node = stk.pop()
        result += str(node.data) + " "
        populate_stack(node.right)
    return result


def inorder_successor_bst(root: BinaryTreeNode, d):
    if not root:
        return None

    node, successor = root, None
    while node:
        if node.data < d:
            node = node.right
        elif node.data > d:
            successor = node
            node = node.left
        else:
            if node.right:
                node = node.right
                while node and node.left:
                    node = node.left
                successor = node
            break
    return successor


def inorder_successor_bst_parent_pointers(root, d):
    node, successor = root, None
    while node:
        if node.data > d:
            node = node.left
        elif node.data < d:
            node = node.right
        else:
            if node.right:
                node = node.right
                while node and node.left:
                    node = node.left
                successor = node
                break
            else:
                while node and node.data <= d:
                    node = node.parent
                successor = node
                break
    return successor


def level_order_traversal(root: BinaryTreeNode):
    result = ""
    que = deque([root])

    while que:
        level_result = ""
        for _ in range(len(que)):
            node = que.popleft()
            level_result += str(node.data) + " "
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)
        result += level_result.rstrip() + "\n"
    return result


def traverse(root):
    if not root:
        return []
    q, result = deque([root]), deque()
    while q:
        level_result = []
        for _ in range(len(q)):
            node = q.popleft()
            level_result.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        result.appendleft(level_result)
    return list(result)


def find_level_averages(root):
    result = []
    q = deque([root])
    while q:
        level_result = []
        for _ in range(len(q)):
            node = q.popleft()
            level_result.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        result.append(sum(level_result) / len(level_result))
    return result


def find_level_order_successor(root, key):
    q, prev = deque([root]), None
    while q:
        for _ in range(len(q)):
            node = q.popleft()
            if prev and prev.val == key:
                return node
            else:
                prev = node
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
    return None


def zig_zag_level_order(root):
    result = []
    if not root:
        return result

    q = deque([root])
    is_forward = True
    while q:
        level_result = deque()
        for _ in range(len(q)):
            node = q.popleft()
            if is_forward:
                level_result.append(node.val)
            else:
                level_result.appendleft(node.val)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        result.append(list(level_result))
        is_forward = not is_forward
    return result


def connect_level_order_siblings(root):
    if not root:
        return
    q = deque([root])
    while q:
        prev = None
        for _ in range(len(q)):
            node = q.popleft()
            if prev:
                prev.next = node
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            prev = node


def is_bst(root):
    if not root:
        return True

    def is_valid(node, upper_limit=float("inf"), lower_limit=float("-inf")):
        if not node:
            return True
        else:
            return (
                (upper_limit > node.data > lower_limit)
                and is_valid(node.left, node.data, lower_limit)
                and is_valid(node.right, upper_limit, node.data)
            )

    return is_valid(root)


def convert_to_doubly_linked_list(root):
    if not root:
        return

    head, prev = None, None
    stk = []

    while stk or root:
        while root:
            stk.append(root)
            root = root.left

        root = stk.pop()

        if prev:
            prev.right = root
            root.left = prev

        if not head:
            head = root

        prev = root
        root = root.right
    return head


def convert_to_doubly_linked_list_recursive(root) -> BinaryTreeNode:
    return None


def main():
    root = BinaryTreeNode(100)
    root.left = BinaryTreeNode(50)
    root.right = BinaryTreeNode(200)
    root.left.left = BinaryTreeNode(25)
    root.left.right = BinaryTreeNode(75)
    root.right.left = BinaryTreeNode(125)
    root.right.right = BinaryTreeNode(350)
    root.left.left.right = BinaryTreeNode(30)
    root.left.right.left = BinaryTreeNode(60)
    head = convert_to_doubly_linked_list_recursive(root)
    print(head)


main()
