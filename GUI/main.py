import tkinter as tk

window = tk.Tk()
window.title('My first GUI App')
window.geometry('1000x600')

# mylabel = tk.Label(text = "Hello World!")
# mylabel.grid(column=0,row=0)

# mylabel1 = tk.Label(text = "Hello World!")
# mylabel1.grid(column=1,row=1)

mylabel = tk.Label(text="Hello World!")
mylabel.pack(side=tk.TOP)

window.mainloop()
