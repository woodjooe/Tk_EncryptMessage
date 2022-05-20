from setUp import *
from TreeClass import *
from key import *

def homeScreen(): pass
def settingsScreen():pass

def settingsScreen(): print("WAT")

def changeSize0(x,y,a,b):

    s=str(x)+"x"+str(y)+"+"+str(a)+"+"+str(b);
    window.geometry(s)

    window.resizable(width=False, height=False)



def helloCallBack():
   messagebox.showinfo( "Hello Python", "Hello World")

def clear_frame():
    if(frame.winfo_children()):
        for widgets in frame.winfo_children():
            widgets.destroy()

def Donate():
    print("thanks");


def sendFeed_Back():
    print("thanks")

def Exit():
   window.destroy();





def IdleAnimation():
   window.destroy();

def make_Key(x):
    K=Key(x);
    K.generateKey();
    return K

def make_Tree(K):
    x=K.length;
    l=K.l;
    T=BinaryTreeNode();
    T.fill_Tree(x,l);
    print("T has !!! "+str(T.data)+" and "+str(T.rightChild.data))
    return T

def EncryptMessage(T, message, K):
    new_M=""
    crypt=""
    j=0
    a=K.length
    print(message)
    print(a)
    print(K.l)
    for i in message :
        j=0
        C=True
        print(i)
        while(C and j<a):
            if (i==K.l[j]):
                C=False
                j=ord(K.l[j])
            j+=1
        j-=1
        print(j)
        if(C==False):
            new_M+=T.encrypt_Letter(j,crypt)
            print(new_M)
    return new_M;
