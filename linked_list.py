class Node(object):
    #this class creates nodes to be added to the linked list
    def __init__(self, value, succeeding=None, previous=None):
        self.data = data
        self.next = None


class LinkedList:
    # create a linked list as the instance of the class
    def __init__(self):
        self.head = None
        self.last_node = None
        self.starting_node = None

    # insert a node at the list's end
    def push(self, data):
        # in the case of empty list
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head

        # adding the node
        else:    
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next
    
    # remove a node from the end of the list
    def pop(self):
        temp = self.head

        # if the list has only one node
        if temp.next == None:
            self.head = None
        
        #general case
        else: 
            #iterate over the list and stop at second last node   
            while(temp.next.next != None):
                temp = temp.next

        
            # second last node become the last node
            self.last_node = temp.next
            temp.next = None
            self.last_node = None

    # remove a node at the begin of the list
    def shift(self): 
        temp = self.head
        # Move the head pointer to the next node
        self.head = self.head.next
        # the remove the head
        temp = None       

    #add a node at the begin of the list
    def unshift(self, data):
        # for an empty list
        if self.head is None:
            # add the node at the end
            self.last_node = Node(data)
            # assign head to this last node
            self.head = self.last_node

        # general case
        else:  
            #create a node
            new_node = Node(data)
            # assign its pointer to the head
            new_node.next = self.head
            # put it as a new head
            self.head = new_node
                         
            
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end = ' ')
            current = current.next      
        
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None   

             