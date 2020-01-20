
#Q: Subtree checker:
Given two binary search trees, check if the 2nd BT is a subtree of the first one.
        // Challenge: T1 is a large binary tree and T2 is a smaller one. Write an
        // algorithm to determine if T2 is a subtree of T1.

#Need 2 functions for :Find and Insert as initial start is from root, then its recursive.
#If we use the same function, recursion would start from the root

#Implement Binary tree in Python.
def class BinarySearchTree:
	def class Node:
	#int key   #No need to declare as we don't specify data types
	#String value
	#Node left,right
		def __init__(self,key,value):
			this.key=key
			this.value=value
	root=Node()
	def Node find(self,key):
		curr=Node()
		curr=root
		if curr.key==key:
			return curr
		elif curr.key<key:
			findNode(curr.left,key)
		elif curr.key>key:
			findNode(curr.right,key)
		else:
		    print("Key not present in the tree!")
		    return	
	def Node findNode(n1,key):
		curr=Node()
		curr=n1
		if curr.key==key:
			return curr
		elif curr.key<key:
			findNode(curr.left,key)
		elif curr.key>key:
			findNode(curr.right,key)
		else:
		    print("Key not present in the tree!")
		    return	
	def insert(self,key,value):
		new_node=Node(key,value) #How would this be treated in recursion
		curr=Node() #It would assign the curr node to root in every recursion, hence we need a sub function to insert the key and value		
		#Same goes for find
		curr=root		
		if curr.key > new_node.key:
			insertNode(curr.left,new_node)
		else:
			insertNode(curr.right,new_node)

	def insertNode(self,n1,n2):
		n1=Node()
		n2=Node()
		this.n1=n1
		this.n2=n2
		if n1 is not Node:
			if n1.key>n2.key:
				insertNode(n1.left,n2)
			else:
			    insertNode(n1.right,n2)
		else:
			n1=n2


Q:Writeout the node of a Binary tree
Q:Write a code to copy a Node		
class Node:
	def __init__(self,key):
		self.key=key
		self.right=None
		self.left=None
	def inOrder(self): #Not working
		if self:
			inOrder(self.left)
			print(self.key)
			inOrder(self.right)

	def copy(n):
		newNode=Node(n.key)
		if n.left is not None:
			newNode.left=n.left.copy()
		if n.right is not None:
			newNode.right=n.right.copy()
		return newNode
def inOrder(x): #works
	if x:
		inOrder(x.left)
		print(x.key)
		inOrder(x.right)

n1=Node(123)
n1.left=Node(567)
n1.right=Node(99)
n1.left.left=Node(10)
n1.left.right=Node(345)
n1.right.left=Node(56)
n1.right.right=Node(34)
n1.inOrder() #If part of the class
inOrder(n1) if outside the class


Q:Inorder traversal for a Binary Tree:
#This function can be a part of the class or outside it like this
	#https://www.learnsteps.com/binary-tree-traversal-using-python/


Q:Level order traversal of binary tree:https://www.hackerrank.com/challenges/tree-level-order-traversal/problem

def levelOrder(root):
	if root is None:
		return
	q=[] #List to store the children of each node, prefer to use deque as it has O(1) time compl as opposed to O(n) for append 
	q.append(root)
	while q:
		parent=q.pop(0)
		if root.left:
			q.append(parent.left)
		if root.right:
			q.append(parent.right)
		print(parent.info,end=' ')


Q:Vertical order traversal of binary tree


Q:Insert a node in BT in level order:
Ref:https://www.geeksforgeeks.org/insertion-in-a-binary-tree-in-level-order/
def insertInBT(root,value):
	newNode=BinaryNode(value)
	if root is None:
		return
	q=[root]
	while q:
		parent=q.pop(0)
		if parent.left is None:
			parent.left=newNode
			return
		else:
			q.append(parent.left)
		if parent.right is None:
			parent.right=newNode
			return
		else:
			q.append(parent.right)
Q:Deletion in a binary tree:
Two steps:
1)Find the deepest right most node
2)Copy the node value with the node to delete
3)Delete the the deepest node
Q:Insert in a BST






	    	

Other BT functions: Min,Find,Add,Delete,In/Pre/Post traversal,Copy	











