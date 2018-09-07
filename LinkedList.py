class DoublyLinkedNode:
    def __init__(self,data):
        self.data=data   ##Data to be stored
        self.previous=None   ##Pointer to the previous element
        self.next=None   ##Pointer to the next element

class DoublyLinkedList:
    def __init__(self):
        self.head=None  ##Define Head of the List
        self.tail=None  ##Define End/Tail of the list

    def AddElement(self, data):
        new_node=DoublyLinkedNode(data) ##Create a node with Val=Data, prev=None and next=None

        if self.head==None:      ##If it is the start of the list
            self.head=new_node       ##Point the Head of the list to this node
            
        elif self.head!=None:    ##If not the start of the list
            self.tail.next=new_node   ##Point the next of the previous element to the new node created 
            new_node.previous=self.tail   ##Point the previous of the current element to the temporary Variable (Contains the previous node)
        self.tail=new_node  ##Move the tail to the current element

    def GetSize(self):
        count=0
        node_count=self.head
        while self.head!=None:
            count=count+1
            if (node_count.next==None):
                break
            node_count=node_count.next
        return count

    def InsertElementAt(self, data, index):
        r=self.GetSize()

        if index<=r and index>1: ##Position being entered at is appropriate
            new_node=DoublyLinkedNode(data)  ##New Node with data to be inserted

            node_insert=self.head ##Begin selection from start of the list
            while index!=1:     ##Traverse the list to find the position
                node_insert=node_insert.next
                index-=1

            new_node.previous=node_insert.previous ##Point the previous of the new data node to place that previous of the old data_node points to
            tmp=new_node.previous
            new_node.next=node_insert  ##point the next of new data node to old data node
            node_insert.previous=new_node ##point previous of old data node to new data node
            tmp.next=new_node

        elif index==1:
            new_node=DoublyLinkedNode(data)
            node_insert=self.head
            self.head=new_node
            self.head.next=node_insert
            node_insert.previous=new_node
             
        else:
            print('Sorry, The position you are trying to insert at is not valid')
       
    def PrintList(self):
        node_print=self.head
        while True:
            print(node_print.data)
            if (node_print.next==None):
                break
            node_print=node_print.next

    def RemoveElement(self,data):
        node_remove=self.head
        while node_remove.next!=None:
            if node_remove.data==data:
                break
            node_remove=node_remove.next

        if node_remove.data==data:
            ref=node_remove.previous
            tmp=node_remove.next
            tmp.previous=ref
            ref.next=tmp
            
        else:
            print('Sorry, the Data you are trying to remove cannot be found')


        
                

            
            
        
            
            
            
            
    
            
            

        
