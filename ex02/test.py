print("hello world")

import tkinter as tk
import tkinter.messagebox as tkm

root=tk.Tk()
root.title("otamesi")
root.geometry("500x200")

label=tk.Label(root,
            text="ラベルを書いてみた件",
            font=("Ricty Diminished",20))
label.pack()

def button_click(event):
    btn=event.widget
    txt=btn["text"]
    tkm.showinfo(txt,f"[{txt}]ボタンを押した")

button=tk.Button(root,text="押すな")
button.bind("<1>",button_click)
button.pack()

entry=tk.Entry(width=30)
entry.insert(tk.END,"fugipiyo")
entry.pack()

root.mainloop()