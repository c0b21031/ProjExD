import tkinter as tk
import tkinter.messagebox as tkm


def click_number(event): 
    btn = event.widget
    num = btn["text"]
    #tkm.showinfo(f"{num}", f"{num}のボタンが押されました")
    entry.insert(tk.END, num)

def click_equal(event):
    eqn = entry.get()
    res = eval(eqn)
    entry.delete(0, tk.END)
    entry.insert(tk.END, res) # 練習7

def click_delete(event):
    entry.delete(0,tk.END)

root=tk.Tk()
root.geometry("400x700")

entry=tk.Entry(root, width=10, font=(", 40"), justify="right") # 練習4
entry.grid(row=0, column=0, columnspan=3)

r,c=1,0
numbers=[7,8,9,4,5,6,1,2,3]
operators=["+","-","*","/"]
for i,num in enumerate(numbers+operators,1):
    btn=tk.Button(root,text=f"{num}",font=("",30), width=4,height=2)
    btn.bind("<1>", click_number)
    btn.grid(row=r,column=c)
    c+=1
    if i%3==0:
        r+=1
        c=0

btn = tk.Button(root, text=f"=", font=("", 30), width=4, height=2)
btn.bind("<1>", click_equal)
btn.grid(row=5, column=2)

btn=tk.Button(root,text=f"AC", font=("", 30), width=4, height=2)
btn.bind("<1>",click_delete)
btn.grid(row=r,column=c)

root.mainloop()