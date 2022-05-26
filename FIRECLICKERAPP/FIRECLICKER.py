from tkinter import messagebox
from tkinter import *
import keyboard

app = Tk()
app.config(bg="black")
app.geometry('800x500')
app.resizable(0,0)
app.iconbitmap('FIRECLICKERAPP/Images/logo.ico')
app.title("FIRECLICKER")





from PIL import Image, ImageTk
# start function

def click():
    messagebox.showinfo('Info-FIRECLICKER', 'Press Enter To Start action, After Pressing Enter Wait For 5ms and The action will start, For Now There is a standard values(You can not change the values) - If something Terrible Happens Click CTRL-Q and IF that does not work Shutdown your PC :)')
    m = k()
    def attack():            
        time.sleep(5)
        for i in range(5):
            time.sleep(0.1)
            m.click(Button.left)
            
    while True:        
        if keyboard.is_pressed("enter"):
            attack()
            break


            
        
            
            
    attack()

    
startbtn = Button(app, text="Start", background="orange", bd=0, font=("Showcard Gothic", 13), command=click)
startbtn.place(x=350, y=320)

from pynput.mouse import Button, Controller as k
import time







# IMAGE





# Create a photoimage object of the image in the path
image1 = Image.open("FIRECLICKERAPP/Images/logo.png")
test = ImageTk.PhotoImage(image1)

label1 = Label(app, image=test, bg="black")
label1.place(x=-10, y=1)

# Text

welcome = Label(app, text="FIRECLICKER", bg="black", fg="orange", font=("Fixedsys", 50))
welcome.place(x=260, y=120)


# clicker_function

speedtext = Label(app, text="Speed:", bg="black", fg="orange", font=("Arial", 12))
speedtext.place(x=100, y=250)
speedget = Entry(app, bg="wheat", width=5, font=("Arial", 10))
speedget.place(x=160, y=253)
speedget.insert(0, 0.1)
speedunit = Label(app, text="ms", bg="black", fg="orange", font=("Arial", 12))
speedunit.place(x=200, y=250)

clickstext = Label(app, text="Clicks:", bg="black", fg="orange", font=("Arial", 12))
clickstext.place(x=300, y=250)
clicksget = Entry(app, bg="wheat", width=5, font=("Arial", 10))
clicksget.place(x=360, y=253)
clicksget.insert(0, 5)
clicksunit = Label(app, text="/speed", bg="black", fg="orange", font=("Arial", 12))
clicksunit.place(x=400, y=250)

quittext = Label(app, text="Quit:", bg="black", fg="orange", font=("Arial", 12))
quittext.place(x=500, y=250)
quitkey = Label(app, text="Press CTRL-Q", bg="black", fg="yellow", font=("Arial", 12))
quitkey.place(x=540, y=250)



    


    

    









app.mainloop()