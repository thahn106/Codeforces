import sys

input = sys.stdin.readline


class AVL_Tree(object):
    class TreeNode(object):
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None
            self.height = 1

    def insert(self, root, key):

        if not root:
            return self.TreeNode(key)
        elif key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        balance = self.getBalance(root)

        if balance > 1 and key < root.left.val:
            return self.rightRotate(root)

        if balance < -1 and key > root.right.val:
            return self.leftRotate(root)

        if balance > 1 and key > root.left.val:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        if balance < -1 and key < root.right.val:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def delete(self, root, key):
        if not root:
            return root
        elif key < root.val:
            root.left = self.delete(root.left, key)
        elif key > root.val:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.getMinValueNode(root.right)
            root.val = temp.val
            root.right = self.delete(root.right, temp.val)

        if root is None:
            return root

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        balance = self.getBalance(root)

        if balance > 1 and self.getBalance(root.left) >= 0:
            return self.rightRotate(root)

        if balance < -1 and self.getBalance(root.right) <= 0:
            return self.leftRotate(root)

        if balance > 1 and self.getBalance(root.left) < 0:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        if balance < -1 and self.getBalance(root.right) > 0:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def leftRotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    def rightRotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    def getHeight(self, root):
        if not root:
            return 0

        return root.height

    def getBalance(self, root):
        if not root:
            return 0

        return self.getHeight(root.left) - self.getHeight(root.right)

    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root

        return self.getMinValueNode(root.left)

    def preOrder(self, root):
        if not root:
            return
        print("{0} ".format(root.val), end="")
        self.preOrder(root.left)
        self.preOrder(root.right)

    def find(self, root, val, last=10**18):
        if not root:
            return last
        if val == root.val:
            return root.val
        if val < root.val:
            return self.find(root.left, val, root.val)
        if val > root.val:
            return self.find(root.right, val, last)


def print(s, end="\n"):
    sys.stdout.write(str(s) + end)


def f(n):
    ans = 0
    while n:
        n, r = divmod(n, 10)
        ans += r
    return ans


for t in range(int(input())):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    remaining = AVL_Tree()
    root = None
    for i in range(n):
        root = remaining.insert(root, i)
    update_count = [3] * n

    for _ in range(q):
        s = list(map(int, input().split()))
        if s[0] == 1:
            l, r = s[1:3]
            i = remaining.find(root, l - 1)
            while i < r and i < len(a):
                a[i] = f(a[i])
                update_count[i] -= 1
                if update_count[i] == 0:
                    root = remaining.delete(root, i)
                i = remaining.find(root, i + 1)
        else:
            x = s[1]
            print(a[x - 1])
