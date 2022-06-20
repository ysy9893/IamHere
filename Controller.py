from tkinter import * 
import tkinter.font as font
import serial 
from PIL import Image, ImageTk, ImageSequence 
import time 
from functools import partial 

arduino = serial.Serial('/dev/cu.usbserial-0001',9600) #Create Serial port object called arduinoSerialData
time.sleep(2) #wait for 2 secounds for the communication to get established

def serial_input(num):
    arduino.write(str(num).encode())
    time.sleep(0.1)
    if arduino.readable():
        response = arduino.readline()
        print(response[:len(response)-1].decode())


root = Tk()
root.geometry('500x400+1500+700')
root.configure(bg='#FFFFFF')
f_button = Frame(root, bg = 'white')
f_button.place(relx=0.5, rely=0.8, anchor = 'center')  


def play_gif():
    global imgs 
    imgs = Image.open("./design/real.gif")
    
    lbl = Label(root)#root에 포함되는 라벨이라는 의미인 것 같음 
    lbl.place(relx=0.5, rely=0.32, anchor = 'center')
    
    for img in ImageSequence.Iterator(imgs):
        time.sleep(0.005)
        img = img.resize((400,250))
        im = ImageTk.PhotoImage(img)
        lbl.config(image = im)
        
        lbl.location
        root.update()
         
    return play_gif()



soundBtn = Frame(f_button, background = '#FFFFFF')
soundBtn.grid(row = 0, column = 0)
soundBtnState = Button(soundBtn, 
                      text = "Sound Issue",
                      #command = connection, 
                      height = 4, 
                      fg = "black", 
                      font = ('Calibri',10, 'bold'),
                      bg= '#FF0000',
                      width = 8,
                      bd = 10, 
                      activebackground ='#FFFFFF',
                      command = partial(serial_input,1))
soundBtnState.pack(side = 'top', ipadx = 10, padx=10, pady=15)

questionBtn = Frame(f_button, background = '#FFFFFF')
questionBtn.grid(row = 0, column = 1)
questionBtnState = Button(questionBtn,
    text="Question",
    #command=set_button2_state,
    height = 4,
    fg = "black",
    font = ('Calibri',10, 'bold'),
    width = 8,
    bd = 10,
    bg = '#00FF33',
    activebackground ='#FFFFFF', 
    command = partial(serial_input, 2)
)
questionBtnState.pack(side='top', ipadx=10, padx=10, pady=15)

chatBtn = Frame(f_button, background = '#FFFFFF')
chatBtn.grid(row = 0, column = 2)
chatBtnState = Button(chatBtn,
    text="Chat",
    #command=set_button2_state,
    height = 4,
    fg = "black",
    font = ('Calibri',10, 'bold'),
    width = 8,
    bd = 10,
    bg = '#00A0FF',
    activebackground ='#FFFFFF', 
    command = partial(serial_input, 3)
)
chatBtnState.pack(side='top', ipadx=10, padx=10, pady=15)


play_gif()

root.mainloop()
        
    

