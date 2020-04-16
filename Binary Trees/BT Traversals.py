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

5)Vertical Order Traversal:



6)Checking if a BT is balanced:


7)Constructing a BST from two traversals (one of which is Inorder):

A)In and Pre:https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/submissions/
Approach:
1)Recursion:Self discovered
	-Hashmap: to store the indexes for the inorder traversal (determines which node is left/right of parent)
	-Traverse through the preorder/post order to go through each node		
	-Subtree function:helper function for each node encountered in traversal
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return
        root=TreeNode(preorder[0])
        finalRoot=root
        l=0
        h={}

        while l<len(inorder):
            h[inorder[l]]=l
            l+=1
        for i in preorder[1:]:
            curr=TreeNode(i)
            while 1:
                if h[i]<h[root.val]:
                    if root.left is None:
                        root.left=curr
                        break
                    else:
                        root=root.left
                else:
                    if root.right is None:
                        root.right=curr
                        break
                    else:
                        root=root.right
        return(finalRoot)
        
2)Recursion:https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/discuss/401124/Python-easy-solution-with-comments
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        
        # Recursive solution
        if inorder:   
            # Find index of root node within in-order traversal
            index = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[index])
            
            # Recursively generate left subtree starting from 
            # 0th index to root index within in-order traversal
            root.left = self.buildTree(preorder, inorder[:index])
            
            # Recursively generate right subtree starting from 
            # next of root index till last index
            root.right = self.buildTree(preorder, inorder[index+1:])
            return root

B)In and Post:https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/discuss/481414/106-Construct-Binary-Tree-from-Inorder-and-Postorder-Traversal-Py-All-in-One-By-Talse
1)Recursion: root then right then left->if we traverse from the end for post order
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if inorder:
            root_val=postorder.pop()
            #print(root_val)
            root=TreeNode(root_val)
            root_idx=inorder.index(root.val)
            root.right=self.buildTree(inorder[root_idx+1:],postorder)
            root.left=self.buildTree(inorder[:root_idx],postorder)    
            return root
2)Iteration:Self discovery
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not postorder:
            return
        root=TreeNode(postorder[-1])
        finalroot=root
        h={inorder[i]:i for i in range(len(inorder))}
        i=len(postorder)-2 #As we have to start from 2nd last element in the array
        print(h)
        while i>=0:
            curr=postorder[i]
            root=finalroot
            #print(curr)
            # idx=inorder.index(curr)
            while 1:                
                if h[curr]<h[root.val]:
                    if not root.left:
                        root.left=TreeNode(curr)
                        break
                    else:
                        root=root.left
                else:
                    if not root.right:
                        root.right=TreeNode(curr)
                        break
                    else:
                        root=root.right
            i-=1
        return(finalroot)
3)
  def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not postorder: return
        #ind is the index of inorder
        stack, root = [], TreeNode(postorder[-1]), 
        stack.append(root)
        i, j = len(inorder)-1, len(postorder)-2
        while j >= 0:
        	#establish right sub tree before hitting the common root
            if stack[-1].val != inorder[i]:
                stack[-1].right = TreeNode(postorder[j])
                stack.append(stack[-1].right)
            else: 
            #right subtree is established, pop all right subtree node out but keep the last one as the root of the comming left node.
                while stack and stack[-1].val == inorder[i]:
                    node = stack.pop(); i -= 1
                node.left = TreeNode(postorder[j])
                stack.append(node.left)
            j-= 1
        return root

8)Bottom Up approach:
Ref LC-Ques:Find leaves of a binary tree:https://leetcode.com/problems/find-leaves-of-binary-tree/
class Solution:
    def findLeaves(self, root: TreeNode):
        depth_dict={}
        def bottomup_Depth(node):
            if not node:
                return 0
            depth=max(bottomup_Depth(node.left),bottomup_Depth(node.right))+1
            depth_dict.setdefault(depth,[]).append(node.val)
            return depth
        bottomup_Depth(root)
        return(depth_dict.values())