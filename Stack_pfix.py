class stacknode:
    def __init__(self, data):
        self.data=data
        self.previous=None

class stack:
    def __init__(self):
        self.top=None

    def push(self, data):
        new_node=stacknode(data)
        
        if self.top==None:
            self.top=new_node
            
        else:    
            new_node.previous=self.top
            self.top=new_node

    def GetSize(self):
        count=0
        node_count=self.top
        while True:
            count+=1
            if (node_count.previous==None):
                break
            node_count=node_count.previous
        return count

    def pop(self):
        new_node=self.top
        if self.GetSize()>0:
            self.top=new_node.previous
        return new_node.data

    def PrintStack(self):
        new_node=self.top
        while True:
            print(new_node.data)
            if (new_node.previous==None):
                break
            new_node=new_node.previous
        
            
    

            
        

    

        
            
            
                
            
