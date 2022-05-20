class Key:
    def __init__(self, x,l):
        self.length=x
        self.l=l

    def generateKey(self):

        for i in range(self.length):

            a=input("insert new letter")
            C=True
            j=0
            while(C and j<len(self.key)):
                if(self.key[j]==a):
                    C=False
                j+=1

            if(C):
                self.key.append(a)
