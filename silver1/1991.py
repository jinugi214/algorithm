# 노드, 왼쪽자식, 오른쪽자식
# 항상 A가 루트노드, 자식노드 없는 경우 .
n = int(input())

data = []

for _ in range(n):
    data.append(input().split())

class Node(): 
    def __init__(self, item, left, right):
        self.item = item
        self.left = left
        self.right = right

def preorder(node): # 전위
    print(node.item, end ='')
    if node.left != '.':
        preorder(tree[node.left])
    if node.right != '.':
        preorder(tree[node.right])

def inorder(node): # 중위
    if node.left != '.':
        inorder(tree[node.left])
    print(node.item, end = '')
    if node.right != '.':
        inorder(tree[node.right])

def postorder(node): # 후위
    if node.left != '.':
        postorder(tree[node.left])
    if node.right != '.':
        postorder(tree[node.right])
    print(node.item, end='')

tree = {} # 딕셔너리

for item, left, right in data:
    tree[item] = Node(item, left, right) # Node클래스 인스턴스화

preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])
