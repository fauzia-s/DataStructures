#Traversals-Recursive and Iterative

1)InOrder:
#Recursvie
def inOrder(self,root):
	op=[]
	if root is None:
		return []
	op+=self.inOrder(root.left)
	op+=[root.val]
	op+=self.inOrder(root.right)
	return op #Returns the traversed nodes in an array


#Iterative:Most of the time involves two stacks
#Algorithm:(Long Story Short: Traverse through the left nodes first then print the root and then the right ones.)
1) Create an empty stack S.
2) Initialize current node as root
3) Push the current node to S and set current = current->left until current is NULL
4) If current is NULL and stack is not empty then 
     a) Pop the top item from stack.
     b) Print the popped item, set current = popped_item->right 
     c) Go to step 3.
5) If current is NULL and stack is empty then we are done.
-Ref:https://www.geeksforgeeks.org/inorder-tree-traversal-without-recursion/

def inOrder(self,root):
	if not root:
		return
	st=[]
	op=[]
	while True:
		if root:
			st.append(root)
			root=root.left
		elif (st):
			curr=st.pop()
			op.append(curr.val)
			if curr.right:
				root=curr.right
		else:
			break
	return(op)

2)PreOrder:
#Recursive
def PreOrder(self,root):
	op=[]
	if not root:
		return []
	return([root.val]+self.PreOrder(root.left)+self.PreOrder(root.right))

#Iterative: Most of the time involves two stacks
#ALgortihm:
#Add first node i.e root in the stack
#Pop it
#Append right
#Append left
#Pop: Left will be out first then right->DLR(DataLeftRight)->PreOrder
https://www.geeksforgeeks.org/iterative-preorder-traversal/
def PreOrder(self,root):
    if not root:
        return
    st=[root]
    op=[]
    while st:
        curr=st.pop()
        op.append(curr.val)
        if curr.right:
            st.append(curr.right)
        if curr.left:
            st.append(curr.left)
    return(op)

3)PostOrder:
#Recursive:
def PostOrder(self,root):
	op=[]
	if not root:
		return []
	return(self.PostOrder(root.left)+self.PostOrder(root.right)+[root.val])

#Iterative:
Ref:https://www.geeksforgeeks.org/iterative-postorder-traversal/
#Algorithm: Two stacks
-add the first node i.e root to the stack
-pop it and add it to another stack say 'op'
-append left
-append right
-Redo step 2
-return the reversed 'op' stack

def PostOrder(self,root):
	if not root:
		return
	st=[root]
	op=[]
	while st:
		curr=st.pop()
		op.append(curr.val)
		if curr.left:
			st.append(curr.left)
		if curr.right:
			st.append(curr.right)
	return(op[::-1])
