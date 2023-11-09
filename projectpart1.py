from tkinter import *
# part2
from tkinter.messagebox import showinfo
#part2 for open and save menu
from tkinter.filedialog import askopenfilename,asksaveasfilename

import os

def newFile():
    global file #it can be accessed from bottom
    root.title("Untitle-Notepad")
    file=None #resetting
    textArea.delete(1.0,END) #From first line zerothe character to end

def openFile():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.*")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file)+"- Notepad")
        textArea.delete(1.0,END)
        f=open (file,"r")
        textArea.insert(1.0,f.read())
        f.close()

def saveFile():
    global file
    if file==None:
        file=asksaveasfilename(initialfile="untitled.txt",filetypes=[("All Files","*.*"),("Text Document","*.*")])
        if file=="":
            file=None
        else:
            f=open(file,"w")
            f.write(textArea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file)+"- Notepad")
            print("File Saved")
    else:
        f=open(file,"w")
        f.write(textArea.get(1.0,END))
        f.close()
        

def quitApp():
    #  part2
    root.destroy()

def cut():
    #part2 event generation and handling of cut
    textArea.event_generate(("<<Cut>>"))

def copy():
    #part2 event generation and handling of copy
    textArea.event_generate(("<<Copy>>"))

def paste():
    #part2 event heneration and handling of paste
    textArea.event_generate(("<<Paste>>"))

def about():
    showinfo("Notepad","Notepad by Akanksha Dubey")


if __name__=='__main__':
    #Basic tkinter setup
    root=Tk()
    root.title("untitle -Notepad")
    #root.wm_iconbitmap("1.ico")
    root.geometry("644x788")

    #Adding TextArea in root
    textArea=Text(root,font="lucida 13")
    file=None    #file will point to the file which is going to open

    # part2
    # packing of textArea fill=BOTH to resize in x and y expand=to area of parent
    textArea.pack(expand=True,fill=BOTH)
    
    #creating menubar in root
    menuBar=Menu(root)#horizontal
    ##################################################
    #creating fiilmenu in Menubar
    fileMenu=Menu(menuBar,tearoff=0)#tearoff
    #to open new file
    fileMenu.add_command(label="New",command=newFile)#newFile is command
    #To open already existing file
    fileMenu.add_command(label="Open",command=openFile)
    #to save a current file
    fileMenu.add_command(label="Save",command=saveFile)
    ##seperator
    fileMenu.add_separator()
    ##to exit
    fileMenu.add_command(label="Exit",command=quitApp)
    ## to stick to menu in the file
    menuBar.add_cascade(label="File",menu=fileMenu)
   #######################################################


   ########################################################
    ##creating editMenu in menubar
    editMenu=Menu(menuBar,tearoff=0)
   ## to give feature of cut,copy,past
    editMenu.add_command(label="Cut",command=cut)
    editMenu.add_command(label="Copy",command=copy)
    editMenu.add_command(label="Paste",command=paste)

   ##to stick the editMenu in file
    menuBar.add_cascade(label="Edit",menu=editMenu)

   ##################################################



   #################################################
   #creating help menu in menubar
    helpMenu=Menu(menuBar,tearoff=0)

   ##creating about
    helpMenu.add_command(label="About Notepad",command=about)

   ##to stick the helpMenu
    menuBar.add_cascade(label="Help",menu=helpMenu)

   
   




    root.config(menu=menuBar)
    # project part 2adding Scrollbar
    scBar=Scrollbar(textArea)
    scBar.pack(side=RIGHT,fill=Y)
    # Rule to remember
    scBar.config(command=textArea.yview)
    textArea.config(yscrollcommand=scBar.set)
    
    
    root.mainloop()
    




    
