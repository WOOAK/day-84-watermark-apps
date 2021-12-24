from PIL import Image as Ima
from PIL import ImageTk
from tkinter import *
from tkinter import filedialog as fd
import os
from tkinter import messagebox

from PIL.ImageTk import PhotoImage
global resized_image2, resized_image, filename1, filename2

def browseFile():
    global resized_image,filename1
    filename1 = fd.askopenfilename(initialdir="/",
                                  title="Select a File",
                                  filetypes=(("Image files",
                                              ".jpeg .jpg .png"),
                                             ("all files",
                                             "*.*")))
    if filename1:
        uploaded_image = Ima.open(filename1)
        old_size = uploaded_image.size
        maxwidth = 1000
        maxheight = 1000
        ratio = min(maxwidth/old_size[0],maxheight/old_size[1])

        resized_image = uploaded_image.resize((int(old_size[0]*ratio),int(old_size[1]*ratio)), Ima.ANTIALIAS)
        img = ImageTk.PhotoImage(resized_image)
        canvas = Canvas(window, width=1000, height=1000)
        canvas.create_image(0, 0, image=img, anchor="nw")
        canvas.image = img
        canvas.grid(row=2,column=2)
    checkUpload()

def browseWatermark():
    global resized_image2, filename2
    filename2 = fd.askopenfilename(initialdir="/",
                                  title="Select a File",
                                  filetypes=(("Image files",
                                              ".jpeg .jpg .png"),
                                             ("all files",
                                              "*.*")))
    if filename2:
        uploaded_image = Ima.open(filename2)
        print(filename2)
        old_size = uploaded_image.size
        maxwidth = 200
        maxheight =200
        ratio = min(maxwidth/old_size[0],maxheight/old_size[1])
        print(old_size[0])
        resized_image2 = uploaded_image.resize((int(old_size[0]*ratio),int(old_size[1]*ratio)), Ima.ANTIALIAS)
    ## Dont know why display transparent photo in window, remark this part
    # img = ImageTk.PhotoImage(resized_image2)
    # canvas2 = Canvas(window, width=200, height=200)
    # canvas2.create_image(500, 500, image=img, anchor="nw")
    # canvas2.image = img
    # canvas2.grid(row=2,column=3)
        resized_image2.show()
    checkUpload()
def Process():
    resized_image.paste(resized_image2, (0,0),resized_image2)
    img = ImageTk.PhotoImage(resized_image)
    # resized_image.show()
    img = ImageTk.PhotoImage(resized_image)
    canvas = Canvas(window, width=1000, height=1000)
    canvas.create_image(0, 0, image=img, anchor="nw")
    canvas.image = img
    canvas.grid(row=2, column=2)
    save_button["state"]="active"
def Save():
    filename, file_extension = os.path.splitext(filename1)
    dir_name = fd.askdirectory()
    if dir_name:
        os.chdir(dir_name)
        filename_without_directory = os.path.basename(filename)
        resized_image.save(f'{filename_without_directory}_watermarked{file_extension}')
        messagebox.showinfo(title='Saved',message=f'Photo saved successfully to {dir_name}!')

def checkUpload():
    if filename1 and filename2:
        process_button["state"] = "active"

window = Tk()
# Gets the requested values of the height and widht.
windowWidth = window.winfo_reqwidth()
windowHeight = window.winfo_reqheight()
print("Width", windowWidth, "Height", windowHeight)

# Gets both half the screen width/height and window width/height
positionRight = int(window.winfo_screenwidth() / 2 - windowWidth / 2)
positionDown = int(window.winfo_screenheight() / 2 - windowHeight / 2)
print(positionRight)
print(positionDown)
print(window.winfo_screenwidth())
print(window.winfo_screenheight())

# Positions the window in the center of the page.
window.geometry("+{}+{}".format(positionRight, positionDown))

# window.eval('tk::PlaceWindow . center')
window.title("Watermark")
window.config(width=1000, height=1000)
upload_button = Button(text="Upload Photo", command=browseFile)
upload_button.grid(row=1, column=1)
watermark_button = Button(text="Upload Watermark", command=browseWatermark)
watermark_button.grid(row=1, column=2)
process_button = Button(text="Process", command=Process, state="disable")
process_button.grid(row=1, column=3)
save_button = Button(text="Save Photo", command=Save, state="disable")
save_button.grid(row=1, column=4)


window.mainloop()
