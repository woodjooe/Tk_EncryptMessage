
crypt=""

class BinaryTreeNode:
    def __init__(self):
        self.data = None
        self.leftChild = None
        self.rightChild = None
        self.crypt=str()

    def __print__(self):
        return 0;

    def insert(node, newValue):
        print("TRying")
        if node.data is None:
            print("FAILing"+str(node.data))
            node.leftChild=BinaryTreeNode()
            node.rightChild=BinaryTreeNode()
            node.data=newValue
            print("FAILing"+str(node.data))
            return None
        else:
            if newValue < node.data:

                node.leftChild.insert(newValue)
            else:
                node.rightChild.insert(newValue)
                return None


    def fill_Tree(self, x, l):
        for i in range(x):
            print("inserted value:"+str(ord(l[i])))
            self.insert(ord(l[i]));
            #print("inserted value:"+str(i))
            #self.insert(i);


    def encrypt_Letter(self, value, crypt):

        if self.data is None:
            return crypt
        elif self.data == value:
            crypt+="2"
            return crypt
        elif self.data > value:
            crypt+="0";
            return self.leftChild.encrypt_Letter(value, crypt)
        else:
            crypt+="1";
            return self.rightChild.encrypt_Letter(value, crypt)


#    def Decrypt_Letter(self, value, crypt):
#        if self.data==0:
#            return letter
#        else :
#            if self.data
#        return 0;
