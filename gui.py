from turtle import left
from pynput.keyboard import Key, Controller
import time
import tkinter as tk
Height = 300
Width = 400
root = tk.Tk()
root.title('Auto Typer by @ishubhamrathi')

root.resizable(False, False)


def autotype(entry):
    keyboard  = Controller()
    time.sleep(5)
    for x in range(len(entry)):
        for y in entry[x]:
            keyboard.press(y)
            keyboard.release(y)
            time.sleep(0.02)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
   
canvas = tk.Canvas(root, height=Height, width=Width , bg='#80c1ff')
canvas.pack()


frame = tk.Frame(root , bg ='#80c1ff' )
frame.place(relwidth=0.8, relheight=0.8 ,relx=0.1, rely=0.1)



label = tk.Label(frame, text = "Enter your text here, click where u want to type(it will take 5 sec to start)", wraplength='250', bg = '#FFF44F')
label.place(relx = 0.1, rely=0.1, relheight=0.2, relwidth=0.8)

entry = tk.Entry(frame, bg ='#FFFFE0' )
entry.place(relx = 0.1, rely=0.4, relheight=0.2, relwidth=0.8)

button = tk.Button(frame, text="Sumit", bg='black' , fg='white' , command=lambda: autotype(entry.get()))
button.place(relx = 0.1, rely=0.65, relheight=0.2, relwidth=0.8)

root.mainloop()
