import tkinter as tk
from tkinter import scrolledtext as tkst

root = tk.Tk()

txt = tkst.ScrolledText(root)
txt.insert(tk.END, "This is a test phrase")
txt.pack()

entry = tk.Entry(root)
entry.pack()

def select_event(event):
    try:
        entry.delete(0, tk.END)
        entry.insert(0, txt.get(tk.SEL_FIRST, tk.SEL_LAST))
    except tk.TclError:
        pass

txt.bind("<<Selection>>", select_event)

root.mainloop()