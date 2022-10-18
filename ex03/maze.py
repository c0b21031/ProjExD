import tkinter as tk


if __name__=="__name__":
    root=tk.Tk()
    root.title("迷えるこうかトン")

    canv=tk.Canvas(root,width=1500,height=900,bg="black")
    canv.pack()

    tori = tk.PhotoImage(file="fig/5.png") 
    cx, cy = 300, 400
    canv.create_image(cx, cy, image=tori, tag="tori")

    key=""

    root.mainloop()