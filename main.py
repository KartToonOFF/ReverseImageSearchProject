from customtkinter import *
from customtkinter import filedialog
from PIL import Image
import shutil   

copy_path = ""
file_path = ""

# Main window
window = CTk()
window.title("ReverseImageSearch")
window.geometry("1920x1080")
window.grid_columnconfigure((0, 1), weight=1)
window.grid_rowconfigure(0, weight=1)


# Fonctions
def import_file():
    # Crée une fenetre pour choisir un ou des fichiers images
    file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("JPEG files", ["*.jpeg", "*.jpg", "*.png", "*.gif"]), ("All files", "*.*")])
    if file_path:
        # Donne le chemin du fichiers
        print("Selected file:", file_path)
        copy_path = shutil.copy(src=file_path, dst="projet/appWindows/files")
        print(copy_path)
        size = getSliderSize()
        image = CTkImage(light_image=Image.open(copy_path), dark_image=Image.open(copy_path), size=size)
        imageLabel.configure(text="", image=image)

sliderValue = IntVar()
def get_value(*args): 
    print(sliderValue.get())

def getSliderSize():
    sizes = {1: (100, 100), 2: (200, 200), 3: (300, 300), 4: (400, 400), 5: (500, 500)}
    return sizes[sliderValue.get()]


# Frame
imageFrame = CTkFrame(window)
imageFrame.grid(row=0, column=1, sticky=NSEW)
imageFrame.grid_columnconfigure(0, weight=1)
imageFrame.grid_rowconfigure(0, weight=1)

# Sliders
sizeSlider = CTkSlider(window, from_=1, to=5, number_of_steps=5, variable=sliderValue, command=get_value)
sizeSlider.grid(row=0, column=0, padx=2, pady=2)

# Buttons
importButton = CTkButton(window, text="Import file", command=import_file)
importButton.grid(row=0, column=0, padx=2, pady=2, sticky=EW)

# Labels
imageLabel = CTkLabel(imageFrame, text="Select your image", image="")
imageLabel.grid(row=0, column=0, sticky=NSEW)


window.mainloop()
