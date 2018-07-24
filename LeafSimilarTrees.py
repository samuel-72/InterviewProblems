class Solution(object):
    def __init__(self):
        self.leaf_val = [[],[]]
        
    def inorder(self,root,no):
        if root is None:
            return
        self.inorder(root.left,no)
        if root.left is None and root.right is None:
            self.leaf_val[no].append(root.val) 
        self.inorder(root.right,no)
        
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        self.inorder(root1,0)
        self.inorder(root2,1)
        #print self.leaf_val
        if self.leaf_val[0] == self.leaf_val[1]:
            return True
        else:
            return False
            
#There is a better solution which uses only generators and which is cooler than this
