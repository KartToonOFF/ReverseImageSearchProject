from tkinter import *
from tkinter import filedialog
import shutil

def import_file():
    # Crée une fenetre pour choisir un ou des fichiers images
    file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("JPEG files", ["*.jpeg", "*.jpg", "*.png", "*.gif"]), ("All files", "*.*")])
    if file_path:
        # Donne le chemin du fichiers
        print("Selected file:", file_path)
        print(shutil.copy(src=file_path, dst="projet/appWindows/files"))
        canvas.create_image(20,20, anchor=NW, image=f"projet/appWindows/files/")

file_path = ""

window = Tk()
window.geometry("700x500")

frame = Frame(window, height=500, width=700)
frame.pack()

importButton = Button(frame, text="Import file", command=import_file)
importButton.pack()

canvas = Canvas(frame, width = 300, height = 300)
canvas.pack()

window.mainloop()