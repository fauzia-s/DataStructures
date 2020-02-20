#LinkedList
class Node:
	def __init__(self,data):
		self.data=data
		self.next=None


class LinkedList:
	def __init__(self):
		self.head=None
	def traverse(self):
		if self.head is None:
			print("List has no items.")
			return
		else:
			curr=self.head
			while curr is not None:
				print(curr.next," ")
				curr=curr.next
	def insert_at_start(self,data):
		new_node=Node(data)
		new_node.next=self.head  #Will set to None if self.head is none currently
		self.head=new_node
	def insert_at_back(self,data):
		new_node=Node(data)
		curr=self.head
		if curr is None:
			new_node.next=None
			self.head=new_node
		else:	
			while curr.next is not None:
				curr=curr.next
			curr.next=new_node
			new_node.next=None	
	def insert_node_at_back(self,new_node):
		curr=self.head
		if curr is None:
			new_node.next=None
			self.head=new_node
		else:	
			while curr.next is not None:
				curr=curr.next
			curr.next=new_node
	def remove_dup(self,item):
		curr=self.head
		counter=0
		if curr is None:
			print("The item is not present in the LinkedList")
			return
		else:
			while curr is not None:
				print("Comparing item ",curr.data)
				if curr.data == item: #Increment the counter for the node
					counter+=1
					print("counter for %d is %d "%(curr.data,counter))
				if counter>1:
					prev.next = curr.next
				prev=curr
				curr=curr.next
	def sumList(self,num1_ll,num2_ll):
		n1=LinkedList()
		n2=LinkedList()
		n3=LinkedList()
		n1=num1_ll
		n2=num2_ll
		curr_n1=num1_ll.head
		curr_n2=num2_ll.head
		num1=''
		num2=''
		num3=''
		#Option2:
		while curr_n1 is not None:
			num1=str(curr_n1.data)+num1
			curr_n1=curr_n1.next
		print(num1)
		while curr_n2 is not None:
			num2=str(curr_n2.data)+num2
			curr_n2=curr_n2.next
		print(num2)
		num3=int(num1)+int(num2)
		for i in str(num3):
			n3.insert_at_start(i)
		return(n3)
	def detectLoop(self):
		curr=self.head
		d_nodes={}
		#dictionary of Nodes
		while curr.next is not None:
			if d_nodes.get(curr.next,-1)>-1:
				print('Linkedlist is circular!')
				return
			else:
				d_nodes[curr.next]=d_nodes.get(curr.next,0)+1
				print(curr.next)
				print(d_nodes)
				curr=curr.next
		print('Linked list is not circular!')



	

#Create an object of the linkedlist class as follows
new_linked_list=LinkedList()
new_linked_list.insert_at_back(1)
new_linked_list.insert_at_back(3)
new_linked_list.insert_at_back(5)
new_linked_list.insert_at_back(1)
new_linked_list.insert_at_back(3)

new_linked_list.traverse()
new_linked_list.remove_alldup()
new_linked_list.remove_dup(3)
#Assert using linkedlist.size

node1=Node(1)
node2=Node(12)
node3=Node(3)
node4=Node(5)
node5=Node(9)

new_linked_list=LinkedList()
new_linked_list.insert_node_at_back(node1)
new_linked_list.insert_node_at_back(node2)
new_linked_list.insert_node_at_back(node3)
new_linked_list.insert_node_at_back(node4)
new_linked_list.insert_node_at_back(node5)
new_linked_list.insert_node_at_back(node1)
new_linked_list.detectLoop()

new2=LinkedList()
new2.insert_node_at_back(node1)
new2.insert_node_at_back(node2)
new2.insert_node_at_back(node3)
new2.insert_node_at_back(node4)
new2.insert_node_at_back(node5)
new2.detectLoop()



***Leetcode:
https://leetcode.com/problems/design-linked-list/
Other solutions:
https://leetcode.com/problems/design-linked-list/discuss/258792/Python-Singly-and-Doubly-LinkedList

#Edge cases for add_at_index function:
-1 element,add at 0th index
-n elements,add at nth index
-No elements add at 0th index

class ListNode:
    def __init__(self,val):
        self.val=val
        self.next=None
class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head=None
                    

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        cur=self.head
        if not self.head:
            return(-1)
        while cur:
            if index==0:
                return cur.val
            cur=cur.next
            index-=1
        return(-1)
            
        

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        if not self.head:
            self.head=ListNode(val)
            return
        saveHead=self.head
        newnode=ListNode(val)
        newnode.next=saveHead
        self.head=newnode
    

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        cur=self.head
        if not self.head:
            self.head=ListNode(val)
            return(self.head)
        while cur.next:
            cur=cur.next
        cur.next=ListNode(val)

        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if not self.head:
            if index==0:
                self.head=ListNode(val)
            else:
                return
        cur=self.head
        prev=None
        
        l=0 #Length of LL
        i=0 #iterator for index
        while cur:
            if i==index:
                if not prev:
                    newNode=ListNode(val)
                    newNode.next=cur
                    self.head=newNode
                    return
                prev.next=ListNode(val)
                prev.next.next=cur
                return
            else:
                prev=cur
                cur=cur.next
            i+=1
            l+=1
        if l==index:
            prev.next=ListNode(val)
        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if not self.head:
            return
        cur=self.head
        prev=None
        if index==0:
            self.head=self.head.next
            return
        while cur.next:
            if index==0:
                prev.next=cur.next
            else:
                prev=cur
            cur=cur.next
            index-=1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)



#Other optimal solutions (from discussions)
class Node(object):
    
    def __init__(self, x, nxt=None):
        """
        :type x: int
        :type nxt: Node | None
        """
        self.val = x
        self.next = nxt

class MyLinkedList(object):
    
    INVALID = -1
    
    def __init__(self):
        self.first = None
        self.size = 0
        
    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        node = self.getNode(index)
        return node.val if node else self.INVALID
    
    def getNode(self, index):
        """
        :type index: int
        :rtype: Node | None
        """
        if index >= self.size or index < 0:
            return None
        node = self.first
        while index > 0:
            node = node.next
            index -= 1
        return node

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.addAtIndex(0, val)

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index > self.size or index < 0:
            return
        prev = self.getNode(index-1)
        if prev:
            prev.next = Node(val, prev.next)
        else:
            self.first = Node(val, self.first)
        self.size += 1

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index >= self.size or index < 0:
            return
        prev = self.getNode(index-1)
        if prev:
            prev.next = prev.next.next if prev.next else None
        else:
            self.first = self.first.next
        self.size -= 1