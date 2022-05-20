from dependencies import *
from TreeClass import *
from key import *

def Donate(C):
    global d
    d="Thank you for !!!!... 0 DT!"
    homeScreen();


def generateKey():
    global K
    K=Key(len(l),l);




def addToKey(entryAdd):
    global l
    ch=str(entryAdd.get())

    C=True
    j=0
    while(C and j<len(l)):
        if(l[j]==ch):
            C=False
        j+=1


    if(ch!="" and C):
        x=ch
        l.append(x);
        entryAdd.delete(0, END)


def rmFromKey(entryRm):
    global l
    ch=str(entryRm.get())

    C=True
    j=0
    while(C and j<len(l)):
        if(l[j]==ch):
            C=False
        j+=1


    if(ch!="" and not(C)):
        i=ch
        l.remove(i);
        entryRm.delete(0, END)




def seeKey():
    global l
    global s
    s="["
    if(not(len(l)==0)):
        for x in l:
            s+=(str(x)+",");
        s=s[:-1]
    s+="]"
    Encrypt_Decrypt_M();

def Encrypt_M(message, ShowMessageE):
    global en_M
    x=K.length
    l=K.l
    T=make_Tree(K);
    en_M=EncryptMessage(T, message, K)
    print(en_M)
    ShowMessageE.insert(0,en_M)



def Decrypt_M(message, ShowMessageD):
    global de_M

    return 0;


def addMessageE(entryMessageE):
    global sE
    sE=str(entryMessageE.get())
    entryMessageE.delete(0, END)
    seeKey()


def addMessageD(entryMessageD):
    global sD
    sD=str(entryMessageD.get())
    entryMessageD.delete(0, END)
    seeKey()


def show_Decrypted_M():
    seeKey();


def show_Encrypted_M():
    seeKey();


def homeScreen():

    clear_frame()



    window.update_idletasks()
    posB=(bellButtonPosition[0]*((window.winfo_width())/1024),
    bellButtonPosition[1]*(window.winfo_height()/600))

    posC=(computerButtonPosition[0]*(window.winfo_width()/1024),
    computerButtonPosition[1]*(window.winfo_height()/600))

    posH=(hammerButtonPosition[0]*(window.winfo_width()/1024),
    hammerButtonPosition[1]*(window.winfo_height()/600))

    posG=(giftButtonPosition[0]*(window.winfo_width()/1024),
    giftButtonPosition[1]*(window.winfo_height()/600))

    C = Canvas(frame,bd=2,confine=True,width=window.winfo_width(),height=window.winfo_height())

    coord=(200,100,100,200)

    window.iconphoto(True,icon);
    C.create_image(window.winfo_width()/2,window.winfo_height()/2,image=background)
    C.create_image(posB[0],posB[1],image=Bell)
    C.create_image(posC[0],posC[1],image=Computer)
    C.create_image(posH[0],posH[1],image=Hammer)
    C.create_image(posG[0],posG[1],image=Gift)
    C.create_text(300, 50, text=d, fill="purple", font=('Helvetica 15 bold'))

    #BUTTONS AND CONFIGS
    bellButton=Button(frame, text="Exit", command=Exit,
     width=190, height=15,
      image=butt,
     fg='purple',
     compound='center',
     )

    giftButton=Button(frame, text="Donate", command=lambda:Donate(C),
     width=190, height=15,
     image=butt,
      fg='purple',
      compound='center',
     )

    hammerButton=Button(frame, text="Encrypt/Decrypt", command=Encrypt_Decrypt_M,
     width=190, height=15,
      image=butt,
       fg='purple',
       compound='center',
     )
    computerButton=Button(frame, text="Settings", command=settingsScreen,
     width=190, height=15,
      image=butt,
       fg='purple',
       compound='center',
     )

    bellButton.place(x=posB[0]-30,y=posB[1]-15)

    hammerButton.place(x=posH[0]-30,y=posH[1]-15)

    computerButton.place(x=posC[0]-30,y=posC[1]-15)

    giftButton.place(x=posG[0]-30,y=posG[1]-15)
    C.pack()

    frame.pack()



def changeSize(x,y,a,b):
    changeSize0(x,y,a,b)
    settingsScreen()


def settingsScreen():

    window.update_idletasks()
    clear_frame()
    C = Canvas(frame,bd=2,confine=True,width=window.winfo_width(),height=window.winfo_height())

    C.create_image(window.winfo_width()/2,window.winfo_height()/2,image=background)

    posB=(bellButtonPosition[0]*((window.winfo_width())/1024),
    bellButtonPosition[1]*(window.winfo_height()/600))

    posC=(computerButtonPosition[0]*(window.winfo_width()/1024),
    computerButtonPosition[1]*(window.winfo_height()/600))

    posH=(hammerButtonPosition[0]*(window.winfo_width()/1024),
    hammerButtonPosition[1]*(window.winfo_height()/600))

    posG=(giftButtonPosition[0]*(window.winfo_width()/1024),
    giftButtonPosition[1]*(window.winfo_height()/600))

    level_1_Resolution=Button(frame,text="720 × 480",image=butt, command=lambda: changeSize(720,480,300,100))
    level_2_Resolution=Button(frame,text="1024 × 600",image=butt, command=lambda: changeSize(1024,600,150,50))
    level_3_Resolution=Button(frame,text="1280 × 720",image=butt, command=lambda: changeSize(1200,720,150,50))

    back=Button(frame,text="Back to Menu",image=butt,command=homeScreen);

    print(posB[0]-30)
    print(posB[1]-15)

    C.pack()

    level_1_Resolution.place(x=posB[0]-30,y=posB[1]-15)
    level_2_Resolution.place(x=posH[0]-30,y=posH[1]-15)
    level_3_Resolution.place(x=posC[0]-30,y=posC[1]-15)
    back.place(x=posG[0]-40,y=posG[1]+30)

def newMessage():
    global l
    l=list();
    global s
    s=str();
    sortScreen();

def update(entryMessageE,entryMessageD,entryAdd,entryRm):
    #addMessageE(entryMessageE)
    #addMessageD(entryMessageD)
    addToKey(entryAdd)
    rmFromKey(entryRm)


def Encrypt_Decrypt_M():

    window.update_idletasks()
    clear_frame()
    C = Canvas(frame,bd=2,confine=True,width=window.winfo_width(),height=window.winfo_height())

    C.create_image(window.winfo_width()/2,window.winfo_height()/2,image=background)

    posB=(bellButtonPosition[0]*((window.winfo_width())/1024),
    bellButtonPosition[1]*(window.winfo_height()/600))

    posC=(computerButtonPosition[0]*(window.winfo_width()/1024),
    computerButtonPosition[1]*(window.winfo_height()/600))

    posH=(hammerButtonPosition[0]*(window.winfo_width()/1024),
    hammerButtonPosition[1]*(window.winfo_height()/600))

    posG=(giftButtonPosition[0]*(window.winfo_width()/1024),
    giftButtonPosition[1]*(window.winfo_height()/600))



    entryMessageE=Entry(frame,font=("Arial",10,"bold"))
    entryMessageD=Entry(frame,font=("Arial",10,"bold"))
    entryAdd=Entry(frame,font=("Arial",10,"bold"))
    entryRm=Entry(frame,font=("Arial",10,"bold"))

    ShowMessageE=Entry(frame,font=("Arial",10,"bold"))
    ShowMessageD=Entry(frame,font=("Arial",10,"bold"))

    window.bind('<Return>',(lambda event:update(entryMessageE,entryMessageD,entryAdd,entryRm)))
    #window.bind('<F5>',command=seeKey())

    E_Button=Button(frame, text="Encrypt", command=lambda:Encrypt_M(str(entryMessageE.get()),ShowMessageE),
    width=190, height=15,
    image=butt,
    fg='black',
    compound='center',
    )
    Show_E_Button=Button(frame, text="Show Encrypted Message:", command=show_Encrypted_M,
    width=190, height=15,
    image=butt,
    fg='green',
    compound='center',
    )
    D_Button=Button(frame, text="Decrypt ", command=Decrypt_M,
    width=190, height=15,
    image=butt,
    fg='green',
    compound='center',
    )
    Show_D_Button=Button(frame, text="Show Decrypted Message:", command=show_Decrypted_M,
    width=190, height=15,
    image=butt,
    fg='black',
    compound='center',
    )
    MakeKeyButton=Button(frame, text="Make Key", command=generateKey,
    width=190, height=15,
    image=butt,
    fg='purple',
    compound='center',
    )
    addToKeyButton=Button(frame, text="add letter:", command=lambda:addToKey(entryAdd),
    width=190, height=15,
    image=butt,
    fg='purple',
    compound='center',
    )
    rmFromKeyButton=Button(frame, text="remove letter:", command=lambda:rmFromKey(entryRm),
    width=190, height=15,
    image=butt,
    fg='purple',
    compound='center',
    )
    showKeyButton=Button(frame, text="Show Key", command=seeKey,
    width=190, height=15,
    image=butt,
    fg='purple',
    compound='center',
    )
    back=Button(frame,text="Back to Menu",command=homeScreen,
    width=190, height=15,
    image=butt,
    fg='#333333',
    compound='center',);

    #E_Button=Button(frame, text="add number:", command=lambda:addList(entryAdd),
    #width=190, height=15,
    #image=butt,
    #fg='purple',
    #compound='center',
    #)
    #D_Button=Button(frame, text="remove number of position:", command=lambda:rmList(entryRm),
    #width=190, height=15,
    #image=butt,
    #fg='purple',
    #compound='center',)
    #Show_D_Button=Button(frame,text="Back to Menu",command=homeScreen,
    #width=190, height=15,
    #image=butt,
    #fg='#333333',
    #compound='center',);//


    C.create_text(300, 500, text=s, fill="green", font=('Helvetica 15 bold'))
    C.pack()

    entryMessageE.place(x=posB[0]+300,y=posB[1]-15,width=100)
    entryMessageD.place(x=posH[0]+300,y=posH[1]-75,width=100)
    E_Button.place(x=posB[0]+30,y=posB[1]-15)
    D_Button.place(x=posH[0]+30,y=posH[1]-75)

    entryAdd.place(x=posG[0]+300,y=posG[1]-100,width=100)
    entryRm.place(x=posG[0]+300,y=posG[1]-70,width=100)
    addToKeyButton.place(x=posG[0]+30,y=posG[1]-100)
    rmFromKeyButton.place(x=posG[0]+30,y=posG[1]-70)

    ShowMessageE.place(x=posG[0]+300,y=posG[1]+15,width=200)
    ShowMessageD.place(x=posG[0]+300,y=posG[1]+45,width=200)
    Show_D_Button.place(x=posG[0]+30,y=posG[1]+15)
    Show_E_Button.place(x=posG[0]+30,y=posG[1]+45)

    showKeyButton.place(x=posG[0]-300,y=posG[1]-40)
    MakeKeyButton.place(x=posG[0]-300,y=posG[1]-85)
    #resetSortButton.place(x=posG[0]-310,y=posG[1]-15)
    back.place(x=posG[0]-300,y=posG[1]+120)
