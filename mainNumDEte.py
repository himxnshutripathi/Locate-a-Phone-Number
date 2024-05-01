import tkinter
from tkinter import *
import phonenumbers
from phonenumbers import timezone, geocoder, carrier

root = Tk()
canvas = Canvas(root)
root.title("Locate Phone")
root.geometry("300x400")
root.resizable(False, False)

title = Label(root, fg="blue", text="Number Fetcher", font="50px").pack()
num = Label(root, text="Enter the Number (+)").place(x=20,y=50)

data = StringVar()

e1 = Entry(root, textvariable=data).place(x = 150, y = 50)

def func():
    num = data.get()

    phone = phonenumbers.parse(num)

    val = phonenumbers.is_valid_number(phone)
    time = timezone.time_zones_for_number(phone)
    carr = carrier.name_for_number(phone,"en")
    reg = geocoder.description_for_number(phone,"en")

    v = ""

    if val==True: v = "Number is Valid."
    else: v = "Number is not Valid."

    emptyl1.config(text="Validity: "+v)
    emptyl2.config(text="Timezone: "+str(time))
    emptyl3.config(text="Service Provider: "+str(carr))
    emptyl4.config(text="Region: "+str(reg))

b1 = Button(root,fg="red",command=func ,text="Get Details").place(x=20,y=90)

canvas.create_line(15, 25, 270, 25, width=1, dash=(10))
canvas.place( x = 10, y= 110)

emptyl1 = Label(root)
emptyl1.place(x=20, y=150)
emptyl2 = Label(root)
emptyl2.place(x=20, y=170)
emptyl3 = Label(root)
emptyl3.place(x=20, y=190)
emptyl4 = Label(root, fg="red")
emptyl4.place(x=20, y=210)

root.mainloop()
