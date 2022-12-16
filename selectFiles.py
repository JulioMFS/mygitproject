import tkinter as tk
from tkinter import filedialog

def selectFiles():
    root = tk.Tk()
    root.withdraw()
    extensions = [("PDF files", "*.pdf"),("PDF/Jpeg files", "*.pdf; *.jpg"), ("Jpeg files", "*.jpg"), ("All files", "*.*")]
    file_path = filedialog.askopenfilenames(initialdir="D:/Agromais/", title="Open a File", filetypes=extensions)
    return file_path
