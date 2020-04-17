#====================================
#IMPORTS
#====================================

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import os

from PIL import ImageTk,Image

#====================================
#ROOT
#====================================

root = Tk()
root.title("Image Viewer")
root.iconbitmap('icon.ico')

#====================================
#VARIABLES
#====================================
#A main list with all the images. You need to add them before of course.
imageList = []

#There will be always an image on start. Don't delete it or it may cause some glitches.
path = os.getcwd()
img = Image.open(path+"/test.jpg")
ph = ImageTk.PhotoImage(img)

#Add that image to the main list for images.
imageList.append(ph)

#Some variables..
currentImage = IntVar()
currentImage.set(0)

prevActive = StringVar()
prevActive.set('normal')

nextActive = StringVar()
nextActive.set('normal')

#====================================
#FUNCTIONS
#====================================
#Get the current image that should be displayed.
c = currentImage.get()

#Draw the image.
labelImage = Label(root,image=imageList[c])
labelImage.grid(column=1,row=0)

def prevImage():
    global labelImage

    #Get the old, update it and get the updated variable
    c = currentImage.get()
    currentImage.set(c - 1)
    c = currentImage.get() 

    #The same checks as in the GUI function
    if c == 0:
        prevActive.set('disabled')
    else:
        prevActive.set('normal')

    #Draw the new image to the screen.
    labelImage.grid_forget()
    labelImage = Label(root,image=imageList[c])
    labelImage.grid(column=1,row=0)

    GUI()

def nextImage():
    global labelImage

    #Get the old, update it and get the updated variable
    c = currentImage.get()
    currentImage.set(c + 1)
    c = currentImage.get()

    #The same checks as in the GUI function
    if c == len(imageList):
        nextActive.set('disabled')
    else:
        nextActive.set('normal')

    #Draw the new image to the screen.
    labelImage.grid_forget()
    labelImage = Label(root,image=imageList[c])
    labelImage.grid(column=1,row=0)

    GUI()

def addImage():
    global labelImage

    #Get the path of the program
    cur = os.getcwd()

    #Open the images
    root.filename = filedialog.askopenfilenames(initialdir=cur,title="Choose a file to open",filetypes=(("JPG files","*.jpg"),("PNG files","*.png"),("BMP files","*.bmp"),("All files","*.*")))
   
    #Add each image to the list
    for item in root.filename:

        #Open the image
        img = Image.open(item)
        ph = ImageTk.PhotoImage(img)

        #Add it to the list
        imageList.append(ph)
        print(len(imageList))
        print(imageList)

        #Draw it to the screen.
        labelImage.grid_forget()
        labelImage = Label(root,image=ph)
        labelImage.grid(column=1,row=0)

    GUI()

def delImage():
    global labelImage
    
    #Get the current image
    c = currentImage.get()

    #Remove it.
    imageList.pop(c)

    #Do some checks for the variable so it won't cause any glitches.
    if c != 0:
        currentImage.set(c - 1)
    else:
        currentImage.set(0)

    #Get the updated variable.
    c = currentImage.get()

    #Delete the image and draw the other one.
    labelImage.grid_forget()
    labelImage = Label(root,image=imageList[c])
    labelImage.grid(column=1,row=0)

    GUI()

#These two don't need any comment as I think everyone understands what they are doing.
def helpMenu():
    messagebox.showerror("Help",'''To add a picture(s), click the 'Add' button. 
Similarly, if you want to remove an image from the list, click the 'Del' button.
Sometimes a program may glitch if you select multiple images and move forward, but just try to go backwards.
Please note that some pictures may be very big and you will not be able to display them fully on your monitor.
The fix for that is to simply resize them in editing images applications such as Paint.''')

def aboutMenu():
    messagebox.showinfo("About","Image Viewer app, version 1.0. Created by xXx_Bain_xXx#1237 in February 2020.")


def GUI():
    #Get the variable..
    c = currentImage.get()

    #Do a few checks whether arrow buttons should be functioning or not.
    if c == 0:
        prevActive.set('disabled')
    else:
        prevActive.set('normal')

    if c == len(imageList) - 1:
        nextActive.set('disabled')
    else:
        nextActive.set('normal')

    #Get the variables for the arrow buttons
    p = prevActive.get()
    n = nextActive.get()

    #Draw the GUI.
    prevButton = Button(root,text="<",command=prevImage,state=p).grid(column=0,row=1)
    nextButton = Button(root,text=">",command=nextImage,state=n).grid(column=2,row=1)

    addButton = Button(root,text="Add",command=addImage).grid(column=1,row=1,sticky='n')
    remButton = Button(root,text="Del",command=delImage).grid(column=1,row=2,sticky='s')

    ivMenu = Menu(root)

    ivMenuInfo = Menu(ivMenu,tearoff=0)

    ivMenu.add_cascade(label="Info",menu=ivMenuInfo)

    ivMenuInfo.add_command(label="Help",command=helpMenu)
    ivMenuInfo.add_command(label="About",command=aboutMenu)

    root.config(menu=ivMenu)

GUI()
root.mainloop()
