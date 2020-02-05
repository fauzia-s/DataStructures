
#Q1: Check if the passed characters in a string are unique or not
def checkUnique(str1):
	d1={}
#ALGO:Add an entry for each letter in dictionary and a counter for # of occurence in the string
	for i in str1:
		if d1.get(i,-1) == -1:
			d1[i]=1
		else:
			d1[i]=d1[i]+1
			return False
	return True

#Test using assertion:
 assert checkUnique("ab"),"Not Unique"
 assert checkUnique("aa"),"Not Unique"
 assert checkUnique("abcdefghijklmnopqrstuvwxyz"),"Not Unique"
#Big O:O{n) for worst case (if last two elements are repititive), else O(1) if first 2 elements are repititive


##Optimised version of #A1 for #Q1:
#Boolean array to store true or false for first occurence of a char in a string.

def uniqueChar(str1):
    arr = [False for i in range(128)] #boolean array for 128 ascii characters
    for i in range(len(str1)):
    	val=str1[i]
    	ascii_val=ord(val)
    	if (arr[ascii_val]):
    		return False
    	else:
    		arr[ascii_val]=True
    return True	

assert uniqueChar("ab"),"Not Unique"
assert uniqueChar("aa"),"Not Unique"
assert uniqueChar("abcdefghijklmnopqrstuvwxyz"),"Not Unique"

#Q2: Check if one string is permutation of another
def checkPermutation(str1,str2):
	d1={}
	d2={}
#First basic check of lenght: If lenght is different then no need of further checks	
	if len(str1) <> len(str2):
		return False
#ALGO:Add the elements and there counts for each string in two separate dictionaries, then compare the values for the same keys, if non-matching return False
#Add elements in dictionary
	for i in str1:
		if d1.get(i,-1)==-1:
			d1[i]=1
		else: 
			d1[i]=d1[i]+1
	for j in str2:
		if d2.get(j,-1)==-1:
			d2[j]=1
		else: 
			d2[j]=d2[j]+1
#Check if all the keys are same
	if sorted(d1.keys()) <> sorted(d2.keys()):
		return False
	else:
		print(sorted(d1.keys()))
		print(sorted(d2.keys()))	
#Compare values for the same keys 	    		
	for i in d1.keys():
		if d2[i]!=d1[i]:
			return False
		else:
			return True
#Tests:
assert checkPermutation("abc", "cba"), "Not permutation"
assert checkPermutation("abc", "xyz"), "Not permutation"
#Big O: O(n+m+n)=O(2n+m)=O(n) , Best case: O(1): when strings are of different length, Worst: If strings of different length, in that case, we have to insert all elements in the dicts and then compare.


#Q3:URLify
#A3.1:Join and Split using python in-built functions			
#A3.2:Create a new string by checking each word, if space then '%20' else same word

def urlify(str1,size):
	newstr=""
	for i in range(len(str1)):
		if len(newstr) == size:
			return newstr	
		elif str1[i] == " ":
			newstr=newstr+"%20"
			print(newstr)
		else:
			newstr=newstr+str1[i]
			print(newstr)
--Iterates for each character hence not efficient, how to iterate for each word?->Using Split?

def urlify(str1,size):
	str_arr=str1.split(" ")
	new_str=""
	for i in str_arr:
		if new_str=="":
			new_str=i
			print(new_str)
		else:
		    new_str=new_str+"%20"+i
		    print(new_str)
		if len(new_str) >= 16:
			return new_str

#Test:
assert urlify("My Home Page    ",16)=='My%20Home%20Page','Error' -->Passes
assert urlify("My Home Page    ",16)=='My%20Home%20Page$','Error' -->Fails due to '$'


#Q4:OneAway: Check if one str1 is one operation away from str2. Operations: Insert,Delete,Replace

def oneAway(str1,str2):
	counter=0
	j=0
	#Check if length difference is 0 or 1
	if abs(len(str1)-len(str2))>1:   #if diff>1: False
		return False
	elif abs(len(str1)-len(str2))==1: #Can be insert/delete
		if len(str1)>len(str2):    ###Modify this if..else set to one algorithm
			for i in range(len(str2)):
				if str2[i] == str1[j]:
					j+=1
				elif str2[i]!=str1[j] and str2[i]==str1[i+1]:
					counter+=1
					j=i+2
				else:
				    counter+=1	
				    j+=1
		else:                              		
		    for i in range(len(str1)):
				if str1[i] == str2[j]:
					j+=1
				elif str1[i]!=str2[j] and str1[i]==str2[i+1]:
					counter+=1
					j=i+2
				else:
					counter+=1
					j+=1
	else:
		for i in range(len(str1)):
			if str1[i] != str2[i]:
				counter+=1
			if counter>1:
				return False
    return True


pals
palsy

als
pals    

if str1[i]==str2[j]:
	i+=1
	j+=1
elif str1[i]=str2[j+1] or str1[i+1]==str2[j]:
    counter+=1

if counter>1:
	return False
else:
	return True



def oneAway(str1,str2):
	counter=0
	i=0
	j=0
	#Check if length difference is 0 or 1
	if abs(len(str1)-len(str2))>1:   #if diff>1: False
		return False
	elif abs(len(str1)-len(str2))==1: #Can be insert/delete
	    print(len(str1),len(str2)) #for i,j in zip(range(len(str1)),range(len(str2))):
	    while i<len(str1) and j<len(str2):
	    	print(i,j)
	    	if str1[i]!=str2[j]:
	    		counter+=1
	    	elif str1[i]==str2[j+1]:
	    		counter+=1
	    		j+=1
	    	elif str1[i+1]==str2[j]:
				i+=1
	    	i+=1
	    	j+=1					
	else:
		for i in range(len(str1)):
			if str1[i] != str2[i]:
				counter+=1
			if counter>1:
				return False
	if counter>1:
		return False
	elif (i==len(str1)-2 or j==len(str2)-2) and counter ==1 :
	    return False
	else:
		return True

assert oneAway("patsy", "pals"),'Error'
assert oneAway("pale", "ple")==False,'Error'
assert oneAway("pales", "pale")==False,'Error'
assert oneAway("pales", "bale")==False,'Error'
assert oneAway("pales", "bae")==False,'Error'

##Issue: If we compare indexes, smaller string might not match the longer string at all,
#Index out of bound error

#Given Solution: Use functions to check for insert/replace as the code gets repeated. 
#Also interchange the order of strings passed to the function based on the length to avoid index out of bound errors.
REDO:



#Q5:Compressor:Compresses the occurence of the characters followed by there occurence count in the string passed

#Ways to do:
	-dictionary
	-For counter
#A5.1:	
def compressor(str1):
	d1={}
	newstr=""
	for i in str1:
		d1[i]=d1.get(i,0)+1
		#print('d1',d1)
	for i in sorted(d1.keys()):
		newstr=newstr+i+str(d1[i])
	if len(newstr)>len(str1):
		return str1
	else:
		return newstr
#Test:
assert compressor('aaabb')=='a3b2','Error' -Pass
assert compressor('aab')=='aab','Error' -Pass
assert compressor('aab')=='a2b1','Error' -Fails (as expected)

#A5.2:	
def compressor(str1):
	newstr=""
	curr_letter=''
	counter=0
	for i in sorted(str1):
		if curr_letter=='':	
			curr_letter=i
			counter=1
		elif curr_letter!=i:
			newstr=newstr+curr_letter+str(counter)
			curr_letter=i	
			counter=1
		else:
			counter+=1
	newstr=newstr+curr_letter+str(counter)			
	return newstr if len(newstr)<len(str1) else str1
##Above line is the alternative to below conditional set
	if len(newstr)>len(str1):
		return str1
	else:
		return newstr	


#Q6:Remove Duplicates:Algorithm to remove duplicates from a linkedlist.
First implement a Linkedlist in python


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

#Write to remove all duplicates
def remove_alldup(self):
		curr=self.head
		item_dict={}
		if curr is None:
			print('The linkedlist is empty!')
			return
		else:
			while curr is not None:
				item_dict[curr.data]=item_dict.get(curr.data,0)+1
				print(item_dict)
				if item_dict[curr.data]>1:
					prev.next=curr.next
					curr=prev.next
				else:	
					prev=curr
					curr=curr.next
			
#Q6:SumLists
		//Challenge: You have two numbers represented by a linked list.
        // Each node represents a single digit, in reverse order, such that the
        // 1's digit is at the head. Write a function that adds the two numbers
        // and returns the sum as a linked list.

        // Example
        // Input:  (8 -> 2 -> 5) + (4 -> 9 -> 2). That is 528 + 294.
        // Output: (2 -> 2 -> 8). That is 822.

#Option1:Add the numbers one each position while traversing and store in a var, which is then copied to LL
#Option2:Traverse the 2 ll, get the numbers,add them,copy to ll: 
	#Little difficuilt in case the number of digits are different in the two linkedlists. But still possible
#Option3:LinkedList can also be implemented using a Stack


num1_ll=LinkedList()
num2_ll=LinkedList()
num1_ll.insert_at_back(8)
num1_ll.insert_at_back(2)
num1_ll.insert_at_back(5)
num2_ll.insert_at_back(4)
num2_ll.insert_at_back(9)
num2_ll.insert_at_back(2)


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
		num1=num1+curr_n1.data
		curr_n1=curr_n1.next
	print(num1)
	while curr_n2 is not None:
		num2=num2+curr_n2.data
		curr_n2=curr_n2.next
	print(num2)
	num3=int(num1)+int(num2)
	for i in str(num3):
		n3.insert_at_start(i)
	return(n3)
		


#Q7: Loop detection: Given a linked list, detect if it is circular.
        // Challenge: Given a circular linked list, implement an algorithm determines
        // whether the linked list has a circular loop
        //
        // Definition: A circular linked list (corrupt) is one where a node's next pointer
        // points to an earlier node.

        // Example
        // Input: 1 -> 2 -> 3 -> 4 -> 5 -> 3 (same as earlier)


#Create a new function to insert node at back, as the previous insert_at_back function adds None in the last node's .next value
def insert_node_at_back(self,new_node):
		curr=self.head
		if curr is None:
			new_node.next=None
			self.head=new_node
		else:	
			while curr.next is not None:
				curr=curr.next
			curr.next=new_node

#Create a dictionary to store the addresses, and quit when the same address is hit more than once, as it implies circular linkedlist

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


node1=Node(1)
node2=Node(12)
node3=Node(3)
node4=Node(5)
node6=Node(9)





 #Q7:Stack of plates
 Option1:Stack of stacks(Lists)
 Option2:linkedlist of linkedlists

 Option2: LinkedList of Linkedlist

class Node:
	def __init__(self,data):
		self.data=data
		self.next=None

class Stack: 	
	def __init__(self,thresh_val):
		self.head=None
		self.thresh_val=thresh_val 		
		self.counter=1
	def push(self,data):
		# print(self.thresh_val)
		new_node=Node(data)
		curr=self.head
		if self.counter<=self.thresh_val:
			new_node.next=curr
			self.head=new_node
			self.counter+=1
			# print("Counter: ",self.counter)
		else:
			main_head=self.head
			self.createLL(data,main_head)
	def createLL(self,data,main_head):
		self.data=data
		self.main_head=main_head
		new_node=Node(data)
		new_node.next=main_head
		self.head=new_node
		main_head=self.head
		stack=Stack(self.thresh_val)
		print("*****New Stack for %dth element with value=%d*******"%(self.counter,self.data))
		print(new_node)
		print("***************")
		self.counter=2 #As first node in the new LL has already been added
		stack.push(new_node)
	def traverse(self):
		curr=self.head
		while curr is not None:
			print("Node addres:%s, Node value:%d"%(curr,curr.data))
			curr=curr.next
	def pop(self):
		curr=self.head
		if curr is not None:
			print("Popped node:%s with value:%d"%(curr,curr.data))
			self.head=curr.next
		else:
			print("Stack is empty")	

stack=Stack(3)
stack.push(5)
stack.push(3)
stack.push(7)
stack.push(9)
stack.push(1)
stack.push(6)
stack.push(12)
stack.traverse()
stack.pop()


Q8: Palindromes:

Option1:My way: Traverse the string from behind and create a new string, if the new string matches the existing one, its a Palindrome
Option2: Walk only halfway in the string, and compare it with the first half, no need to traverse the entire string.

Option1:
def palindrome(str1):
	i=len(str1)-1
	str2=''
	while i>=0:
		str2+=str1[i]
		i-=1
	if str2==str1:
		return True
	else:
		return False

Tests:
assert palindrome('abba'),'Not Palindrome'
assert palindrome('mom'),'Not Palindrome'
assert palindrome('yes'),'Not Palindrome'
assert palindrome('rush'),'Not Palindrome'
		
Option2:
def palindrome(str1):
	i=0
	while i<=len(str1)/2:
		if str1[i]!=str1[len(str1)-i-1]:
			return False
		i+=1
	return True

Tests:
assert palindrome('abba'),'Not Palindrome'
assert palindrome('mom'),'Not Palindrome'
assert palindrome('yes'),'Not Palindrome'
assert palindrome('rush'),'Not Palindrome'	

Q9:FizzBuzz: Print numbers 1 to 100. For multiple of 3->Fizz, Multiple of 5->Buzz, Multiple of both->FizzBuzz
Option1:My way: check if the number is multiple of 15, then return FizzBuzz,else return the other values

def fizzbuzz():
	num1=0
	while num1<=100:
		if num1%15==0:
			print('FizzBuzz')
		elif num1%5==0:
			print('Buzz')
		elif num1%3==0:
			print('Fizz')
		else:
		    print(num1)
		num1+=1

Q10:Ransom note-> Can the words passed be made with the magazin letters available?
Option1:My way: Add the letters in a dictionary, traverse through the note and check if its available in the dictionary and deduct the value(count) once a letter is used

def ransomNote(note,letters):
	d={}
	letters=letters.replace(' ','')
	for i in letters:
		d[i]=d.get(i,0)+1
	for i in note:
		if d.get(i,0)==0:
			return False
		else:
			d[i]=d.get(i)-1
	return True		

assert ransomNote("Pay","yaP"),"Note not possible"      
assert ransomNote("Pay", "yaP a"),"Note not possible"      
assert ransomNote("Pay me $1000", "ayPem001$"),"Note not possible" 

Q11:Caesar Cipher
-Replace alphabets in the message based on the offset provided, by shifting the order.

Option1:Store the letters and their order in a list, but difficuilt to retrieve
Option2:Store the letters and there order in dictionary

import string
def caesarCipher(message,offset):
	letters=string.ascii_uppercase
	d={}
	new_mesg=''
	i=0
	while i<len(letters):
		d[letters[i]]=i
		i+=1
	for i in message:
		if i==' ':
			new_mesg=new_mesg+' '
		elif d[i]>22:
			index=(d[i]-26)+offset
			new_mesg=new_mesg+letters[index]
		else:
			index=d[i]+offset
			new_mesg=new_mesg+letters[index]
	return new_mesg	

Tests:
assert caesarCipher("XYZ",3)=="ABC","Not encrypted properly"
assert caesarCipher("X Y Z",3)=="A B C","Not encrypted properly"
assert caesarCipher("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG",3)=="WKH TXLFN EURZQ IRA MXPSV RYHU WKH ODCB GRJ","Not encrypted properly"
assert caesarCipher("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG",-3)=="QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD","Not encrypted properly"



Q12: Sieve of Eratosthenes: Given a prime number 'n', calculate all the prime numbers smaller than or equal to 'n'
Option1:Start with 2 and iterate till 'n', adding the primes and skipping the multiples of prime added so far
Option2:Start with 2 and go till the prime number 'n' as upper bound to generate composite numbers 
and store the values for these numbers as indexes Eg: isComposite[2]=false,isComposite[3]=false, isComposite[4]=true
,,,,m

#Iterate all the elements in the numList first by 2, and delete everything that is divisible by 2, then
check the next number after 2, which is not divisible by 2, now delete all the numbers in the list 
now check the next number after 3,which is not divisible by 3

def sievePrime(num):
	numList=[i for i in range(num+1) if i>2]
	#print("NumList: "+str(numList))
	primeList=[2] #initialise the prime number list
	for p in primeList:
		for i in numList:
			if i<=p or i%p == 0:
				numList.remove(i)
		if len(numList)>=1:		
			primeList.append(numList[0])
			numList.remove(numList[0])
			#print("PrimeList: "+str(primeList))
	print("Final PrimeList:"+str(primeList))
	return(primeList)

BigO: O(m*n2)-for,for,remove=O(n^3)
Optimize?
Create a list of all numbers same numlist but the of characters where position says if the NUMBER IS prime or composite
def sievePrime(n):
	#nums can be a list or a dictionary:List is more efficient
	nums=['T' for i in range(n+1) if i>=2]
	print(nums)
	p=2
	i=0
	while i<=n:
		print("In first while loop!")
		if i<p:
			i+=1
			continue
		elif i==p or i%p==0 :
			nums[i]='F'
		elif i==n and p<=n:
			p+=1
			i=0
		elif i==n and p>n:
			break
		i+=1
	j=0
	while j < len(nums):
		print("In second while loop!")
		if nums[j]=='T':
			print(j)
		j+=1



Q13:String reversal:
Option1: iterate through the string elements from behind
Option2:string[::-1]
Option3: reversed(string)

Option1:
def reverse(str1):
	i=len(str1)-1
	newstr=''
	while i>=0:
		newstr+=str1[i]
		i-=1
	print(newstr)

Option3:
>> print([i for i in reversed('hello')])
			
Q14:Integer reversal:
Option1:Convert to string,reverse,convert to int again
Option2:Mod 10 get remainders and append in the newstring
Option3:Mod 10 get remainders and add the numbers

Option1:
def intRev(num):
	numstr=str(num)
	i=len(numstr)-1
	numstr2=''
	while i>=0:
		numstr2+=numstr[i]
		i-=1
	print(int(numstr2))

def intRev1(num):
	newnum=''
	while num>10:
		rem=num%10
		num=num//10
		newnum+=str(rem)
		if num<10:
			newnum+=str(num)
	print(newnum)

def intRev2(num):
	newnum=0
	while num>0:
		rem=num%10
		num=num//10
		newnum=newnum*10+rem
	print(newnum)


Q15:Anagram:
def anagram(str1,str2):
	d1={}
	for i in str1:
		d1[i]=d1.get(i,0)+1
	for i in str2:
		d1[i]=d1.get(i,0)-1
	for i in d1.keys():
		if d1[i]==0:
			continue			
		else:
			return False
	return True


Q16:Array Intersection:
Option1:If there can be multiple elements in each array
Option2:If each array has unique elements only
Option3: Brute force
Option1:
def arrayInt(l1,l2):
	l3=[]
	i,j=0,0
	while i<len(l1) and j<len(l2):
		if l1[i]==l2[j]:
			l3.append(l1[i])
			i+=1
			j+=1
		elif l1[i]<l2[j]:
			i+=1
		else:
			j+=1
	return(l3)		

Option2:
def arrayInt(l1,l2):
	l3=[]
	l4=[]
	l3=l1+l2
	d={}
	for i in l3:
		d[i]=d.get(i,0)+1
	print(d)
	for i in d.keys():
		if d[i]>1:
			l4.append(i)
	return(l4)		


Option3:
def arrayInt(l1,l2):
	l3=[]
	for i in l1:
		for j in l2:
			if i==j:
				l3.append(i)
	return(l3)	


#Amazon Questions
Q19:Merge two lists
-Fit the function into an API.

l1=[2,4,5,6,7]
l2=[1,2,3,4,5,7]
l3=[1,2,2,3,4,4,5,5,6,7]

Questions to interviewer and assumptions.
-Are the lists sorted? Y
-Does the output need to be sorted? Y 


Note:Check if no overlapping, if yes then simply append the arrays
Option1: Bruteforcce
Option2: Simulataneous walk through each list and compare elements with each other

Option1:
def mergeListBF(l1,l2):
	i,j=0,0
	l3=[]
	if l1==[]:
		return(l2)
	elif l2==[]:
		return(l1)
	elif l1==[] and l2==[]:
		return([])	
	while i<len(l1):
		while j<len(l2):
			if l1[i]<l2[j]:
				l3.append(l1[i])
				i+=1
			elif l1[i]>l2[j]:
				l3.append(l2[j])
				j+=1
			else:
				l3.append(l1[i])
				l3.append(l2[j])
				i+=1
				j+=1
	return(l3)

Option2:
def mergeLists(l1,l2):
	l3=[]
	if l1==[]:
		return(l2)
	elif l2==[]:
		return(l1)
	elif l1==[] and l2==[]:
		return([])
	i,j,k=0,0,0
	while i < len(l1) and j <len(l2):
		#print("i=%d,j=%d"%(i,j))
		if l1[i]<l2[j]:
			l3.append(l1[i])
			i+=1
		elif l1[i]>l2[j]:
			l3.append(l2[j])
			j+=1
		else: 
			l3.append(l1[i])
			l3.append(l2[j])
			i+=1
			j+=1
	if i!=len(l1)-1:
		while i < len(l1):
			l3.append(l1[i])
			i+=1
	elif j!=len(l2)-1:
		while j < len(l2):
			l3.append(l2[j])
			j+=1
	return(l3)	

l1=[2,4,5,6,7]
l2=[1,2,3,4,5,7]
l3=[1, 2, 2, 3, 4, 4, 5, 5, 6, 7, 7] #Expected o/p

assert mergeLists(l1,l2)==[1, 2, 2, 3, 4, 4, 5, 5, 6, 7, 7],"Lists don't match"

API: Confirm if correct. Pending!
class MergeList:
	def mergeLists(l1,l2):





			





