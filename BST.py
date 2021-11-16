class Node:
	def __init__(self, data):
		self.left = self.right = None
		self.data = data


class BST:
	def insert(self, root, data):
		if root == None:
			return Node(data)
		elif data <= root.data:
			cur = self.insert(root.left, data)
			root.left = cur
		else:
			cur = self.insert(root.right, data)
			root.right = cur
		return root


	def minNode(self, root):
		if root.left == None:
			return root
		else:
			return self.minNode(root.left)


	def deleteNode(self, root, data):
		if root == None:
			return root
		if root.data < data:
			root.right = self.deleteNode(root.right, data)
		elif root.data > data:
			root.left = self.deleteNode(root.left, data)
		else:
			if root.left == None:
				tempNode = root.right
				root = None
				return tempNode
			elif root.right == None:
				tempNode = root.left
				root = None
				return tempNode
			else:
				node = self.minNode(root.right)
				root.data = node.data
				root.right = self.deleteNode(root.right, node.data)
				return root
		return root


	def printTree(self, root):
		if root != None:
			self.printTree(root.left)
			print(root.data, end=" ")
			self.printTree(root.right)


	def getHeight(self, root):
		if root == None:
			return 0
		if root.left == None and root.right == None:
			return 0
		leftHeight 	= self.getHeight(root.left)
		rightHeight = self.getHeight(root.right)
		return max(leftHeight, rightHeight) + 1


	#BFS Traversal
	def bfsTraversal(self, root):
		if root == None:
			return 
		queue = []
		queue.append(root)
		while len(queue):
			node = queue.pop(0)
			print(node.data, end=" ")
			if node.left != None:
				queue.append(node.left)
			if node.right != None:
				queue.append(node.right)




#main programm
myTree = BST()
n = int(input())
root = None

for _ in range(n):
	d = int(input())
	root = myTree.insert(root, d)

myTree.printTree(root)
print(f"\nthe BFS Traversal : ")
myTree.bfsTraversal(root)
print(f"\nthe Height of the tree is : {myTree.getHeight(root)}")
deletNod = int(input('enter node for delete : '))
root = myTree.deleteNode(root, deletNod)
print('\nafter delet : ')
myTree.printTree(root)
print(f"\nthe Height of the tree after delet node is : {myTree.getHeight(root)}")





















