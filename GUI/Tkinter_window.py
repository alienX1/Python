import tkinter as tk

window = tk.Tk()
# label = tk.Label(
#     text='Python tkinter!',
#     foreground='white',
#     background='#34A2FE'
# )

# short_hand for background bg and foregroung fg
# label = tk.Label(
#     text='Python tkinter!',
#     fg='white',
#     bg='#34A2FE'
# )

label = tk.Label(
    text='Python tkinter!',
    fg='white',
    bg='#242424',
    width=10,
    height=10
)
"""Above code don't give square box. One horizontal text unit is determined by the width of the character "0", 
or the number zero, in the default system font. Similarly, one vertical text unit is determined by the height of the 
character "0". """

label.pack()

window.mainloop()