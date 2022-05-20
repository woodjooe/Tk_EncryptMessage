from tkinter import *

l=list();
s=str();
d=str();
backgroundColor="#eeeeee"

bellButtonPosition=(500,100)
hammerButtonPosition=(500,200)
computerButtonPosition=(500,300)
giftButtonPosition=(500,450)



window=Tk();

frame=Frame(window)

window.title("Encrypted_Comm!")
window.geometry("1024x600+150+50")
window.resizable(width=False, height=False)

background=PhotoImage(file='images/background.png')

icon=PhotoImage(file='images/logo.png')

butt=PhotoImage(file='images/buttons.png')

Bell=PhotoImage(file='images/bellButton.png')

Gift=PhotoImage(file='images/giftButton.png')

Hammer=PhotoImage(file='images/hammerButton.png')

Computer=PhotoImage(file='images/pcButton.png')

frame.pack();
