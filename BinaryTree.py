class BinaryTreeNode:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None

class BinaryTree:
    def __init__(self):
        self.root=None
        self.ref_node=None

    def AddElement (self,data):
        new_node=BinaryTreeNode(data)

        r=False
        if self.root==None:
            self.root=new_node
        else:
            ref_node=self.root    ##start from root
            par_node=ref_node   

            while ref_node!=None:

                if ref_node.data<=data:
                    par_node=ref_node
                    ref_node=ref_node.right
                    r=True

                else:
                    par_node=ref_node
                    ref_node=ref_node.left
                    r=False

            if r is True:
                par_node.right=new_node
            else:
                par_node.left=new_node

    def PrintElement (self, start):
        if (start==None):
            return
        print(start.data)
        self.PrintElement(start.left)
        self.PrintElement(start.right)
    
        
 

                    
                
            
       
            
    
        
                
                
            
            
                            
                                
                                
