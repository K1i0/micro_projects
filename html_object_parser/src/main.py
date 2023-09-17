#! /usr/bin/env python
# -*- coding: utf-8 -*-
import transform as tsf
import tkinter as tk
from tkinter import scrolledtext
from tkinter import filedialog
from tkinter import ttk

def openFile():
    tf = filedialog.askopenfilename(
        initialdir="C:/Users/MainFrame/Desktop/", 
        title="Open Text file", 
        filetypes=(("Text Files", "*.txt"),), 
        )
    tf = open(tf, 'r', encoding="utf-8")  # or tf = open(tf, 'r')
    tsf.prepare_data(txt, tf)
    tf.close()

def clearTextWindow():
    txt.delete("1.0", tk.END)

root = tk.Tk()
root.title("Парсер HTML")
root.geometry("700x600")
root.resizable(False, False)

txt = tk.scrolledtext.ScrolledText(root, width=80, height=34)
txt.pack()

importFileButton = ttk.Button(text="Set Import File", width=110, command=openFile)
importFileButton.pack()
exportFileButton = ttk.Button(text="Clear Text Window", width=110, command=clearTextWindow)
exportFileButton.pack()

root.mainloop()