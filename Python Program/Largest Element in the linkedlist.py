# define the class
class Node:
	def __init__(self):
		self.data = None
		self.next = None
head = None
# function to find the smallest element
def maximumElement(head):
	max = -32767
	while (head != None):
		if (max < head.data) :
			max = head.data
		head = head.next
	return max
# function to push data into linkedlist
def push( data) :
	global head
	nextNode = Node()
	nextNode.data = data
	nextNode.next = (head)
	(head) = nextNode
# printing the linkedlist
def printList( head) :
	while (head != None) :
		print(head.data ,end= " -> ")
		head = head.next
	print("None")
# adding values to the linkedlist
push( 1)
push( 3)
push( 5)
push( 2)
push( 7)
print("Linked list is : ")
printList(head)
print("Maximum element in linked list: ",end="")
print(maximumElement(head))
