from tkinter import *
from tkinter.filedialog import askopenfile
from decrypter import decrypt_file

window = Tk()
window.geometry("600x550")
window.title("Beagle PDF Decrypter")
window.resizable(False, False)
labelOne = Label(window, text="¡Hola, buenos días! Esta es tu herramienta para convertir archivos PDF. Por favor, elige un archivo para convertir", wraplength=600)
labelOne.place(x=15, y=420)

img = PhotoImage(file="beagles.png")
background_label = Label(window, image=img)
background_label.place(x=0, y=0, relwidth=1)
background_label.lower()

def open_file():
  file = askopenfile()
  if file is not None:
    decrypt_file(file)


select = Button(window, width=7, height=2, text="Elegir", relief=GROOVE, command=lambda:open_file())
# file = askopenfile()
select.place(x= 255, y= 480)

# run as a program rather than a run once file
window.mainloop()
