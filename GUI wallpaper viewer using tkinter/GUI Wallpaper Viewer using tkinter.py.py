from tkinter import *
from PIL import ImageTk,Image
import os   #by using os module you can navigate 
            #inside files and folders
def next_image():
    global counter
    img_label.config(image=img_array[counter%len(img_array)])
    counter+=1
counter=1
root=Tk()
root.title("Wallpaper Viewer")
root.minsize(600,600)     #priority will be given to this
#if geometry(lxb) is less than minsize(lxb)
#in other words this is a minimum size constraint
root.geometry('800x600')  #priority will be given to this
#if minsize(lxb) is less than geometry(lxb)
root.configure(background='black')
root.iconbitmap("wall.ico")
wall_label=Label(root,text='Wallpaper Viewer',fg='white',bg='black')
wall_label.pack(pady=(10,5))
wall_label.config(font=('verdana',14))
files=os.listdir('wallpaper') #This will give the name of 
#all files present inside the 'wallpaper' folder

#print(files)  #['everest.png', 'maldives.png.png', 'temple.png']

img_array=[] #contains image object
for file in files:
    #file_path=os.path.join('wallpaper',file)
    #print(file_path)
    img=Image.open(os.path.join('wallpaper',file))
    resized_img=img.resize((700,400))
    img_array.append(ImageTk.PhotoImage(resized_img))
#print(img_array)

img_label=Label(root,image=img_array[0])
img_label.pack(pady=(15,10),ipady=0)

next_btn=Button(root,text='Next',bg='white',fg='black',width=25,height=2,command=next_image)
next_btn.pack(pady=(20,5))

root.mainloop()

