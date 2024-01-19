from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
from rembg import remove
import shutil



form = Tk()
form.title('')
pathImage = ""
screen_width = form.winfo_screenwidth()
screen_height = form.winfo_screenheight()
form_width = 500
form_height = 300

x = (screen_width // 2) - (form_width // 2)
y = (screen_height // 2) - (form_height // 2)
form.geometry(f"{form_width}x{form_height}+{x}+{y}")
form.config(background='white')
form.maxsize(width=form_width, height=form_height)
form.minsize(width=form_width, height=form_height)

fr2 = Frame(form, background='white')
fr2.place(x=170, y=50, height=300-70, width=500-180)

labelDev = Label(form, text="Dev By D_Bakhti", font=('Arial',9,'bold'), fg='black', bg='white')
labelDev.place(x=400, y=300-19)

image_label = Label(fr2, background='white')
image_label.pack()

def uploadImageInLabel():
   file_path = filedialog.askopenfilename()
   global pathImage
   pathImage = file_path
   print("Selected file:", file_path)
   load = Image.open(file_path)
   load.thumbnail((500-180,300-60))
   #load.resize((500-180,300-60))

   image = ImageTk.PhotoImage(load)
   image_label.image = image
   image_label.config(image=image)
   #image_label.pack()
   form.update_idletasks()

def removeBg():
   input = Image.open(pathImage)
   output = remove(input)
   output.save('test.png')
   load = Image.open('test.png')
   load.thumbnail((500-180,300-60))
   #load.resize((500-180,300-60))

   image = ImageTk.PhotoImage(load)
   image_label.image = image
   image_label.config(image=image)
   

def saveImg():
   fileName = str(pathImage).split('/')[-1]
   path =""
   for i in range(len(pathImage.split('/'))-1):
      path += pathImage.split('/')[i] + '/'
   print(path)
   path = path + fileName.split('.')[0]+"_removebg.png"
   print(path)
   shutil.copy("test.png", path)

title = Label(
  form,
  text='Remove Background Images',
  background= 'black',
  foreground='white',
  font= ('Arial',20,'bold')
)
fr1 = Frame(form, background='white')
fr1.place(x=10, y=38, width=150, height=300-38)
title.pack(fill=X)

btn1 = Button(fr1, text='Upload Image\nتحميل الصور', width=20, command=uploadImageInLabel, height=3, background='green', foreground='white', font= ('Arial',9,'bold'))
btn1.grid(row=1, column=1, pady=15)
btn2 = Button(fr1, text='Remove Background\nإزالة الخلفية', width=20, height=3, background='grey', foreground='white', font= ('Arial',9,'bold'), command=removeBg)
btn2.grid(row=2, column=1, pady=15)
btn3 = Button(fr1, text='Save Image\nاحفظ الصورة', width=20, height=3, background='black', foreground='white', font= ('Arial',9,'bold'), command=saveImg)
btn3.grid(row=3, column=1, pady=15)





form.mainloop()
