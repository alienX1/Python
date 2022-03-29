import tkinter as tk

window = tk.Tk()
label = tk.Label(text='Name')
entry = tk.Entry()

# The data which we enter can be retrieved by .get()
name = entry.get()

# Data can be deleted using .delete()
name.delete(0, 4)
# It deletes character from 0 to fourth index

# .insert(0, 'python')
# it insert python at 0th index

label.pack()

entry.pack()

window.mainloop()
