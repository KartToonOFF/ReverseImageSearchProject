from customtkinter import *
from customtkinter import filedialog
from PIL import Image
import shutil

def import_file():
    # Crée une fenetre pour choisir un ou des fichiers images
    file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("JPEG files", ["*.jpeg", "*.jpg", "*.png", "*.gif"]), ("All files", "*.*")])
    if file_path:
        # Donne le chemin du fichiers
        print("Selected file:", file_path)
        copy_path = shutil.copy(src=file_path, dst="projet/appWindows/files")
        print(copy_path)
        image = CTkImage(light_image=Image.open(copy_path), dark_image=Image.open(copy_path), size=(100, 100))
        my_label.configure(image=image)
        
copy_path = ""
file_path = ""

window = CTk()
window.geometry("700x500")

frame = CTkFrame(window)
frame.pack()

importButton = CTkButton(frame, text="Import file", command=import_file)
importButton.pack()

my_label = CTkLabel(frame, text="", image="")
my_label.pack(pady=10)

window.mainloop()