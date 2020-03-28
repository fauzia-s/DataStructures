#Traversals-Recursive and Iterative

1)InOrder:
class Solution:
    #Option1:Recursion:Local variable
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        l=[] #Local variable, but append the value for each recursion, to being being reset
        if not root:
            return
        if root.left:
            l+=self.inorderTraversal(root.left)
        l.append(root.val)
        if root.right:
            l+=self.inorderTraversal(root.right)
        return(l)
    
    #Option2:Recursion:Global variable
    def __init__(self):
        self.l=[]
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return
        if root.left:
            self.inorderTraversal(root.left)
        self.l.append(root.val)
        if root.right:
            self.inorderTraversal(root.right)
        return(self.l)
    #   Option3:Recursive: One liner return
    def inorderTraversal(self,root:TreeNode)->List[int]:
        if not root:
            return []
        return(self.inorderTraversal(root.left)+[root.val]+self.inorderTraversal(root.right))
    
    #Option4:Iterative
    def inorderTraversal(self,root:TreeNode)->List[int]:
        if not root:
            return
        st=[]
        op=[]
        while st or root:
            if root:
                st.append(root)
                root=root.left
            else:
                curr=st.pop()
                op.append(curr.val)
                root=curr.right
        return(op)


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
	while st or root:
		if root:
			st.append(root)
			root=root.left
		else: #if st is nonempty
			curr=st.pop()
			op.append(curr.val)
			if curr.right:
				root=curr.right
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


4)Level Order Traversal:

#Opt1:Iterative:
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return
        q=collections.deque()
        q.append(root)
        res=[]
        count=0
        while q:
            l=len(q)
            temp=[]
            while l>0:                
                curr=q.popleft()
                temp.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                l-=1
            res.append(temp)
        return(res)

#Opt2:Recursion:List
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res=[]
        self.dfs(root,0,res)
        return(res)
    
    def dfs(self,root,level,res):
        if not root:
            return
        if len(res)<=level:
            res.append([])
        res[level].append(root.val)
        self.dfs(root.left,level+1,res)
        self.dfs(root.right,level+1,res)

 #Opt3:Recursion:Dictionary:Best Solution
 class Solution:

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        hmap={}
        if not root:
            return
        self.dfs(root, 0,hmap)
        return (list(hmap.values()))
    def dfs(self,node, level,hmap):
        if not node:
            return
        hmap.setdefault(level, []).append(node.val)
        self.dfs(node.left, level+1,hmap)
        self.dfs(node.right, level+1,hmap)
