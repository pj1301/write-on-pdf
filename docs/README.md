# PDF Conversion Tool

_Created with Python3, tkinter and pikepdf._

## Files

### UI
The UI is provided by tkinter, a package which is actually included in the basic Python program download.

**Code:**
```python
from tkinter import *

# create window
window = Tk()
# add a title to the window
window.title("PDF Decrypter")
# create a label
labelOne = Label(window, text="!Holá, buenos días! Esto es una herramienta para convertir archivos PDF. Por favor, elige un archivo para convertir:")
# add the label to the window
labelOne.pack()
# add a photo


# run as a program rather than a run once file
window.mainloop()
```

### Decrypter
The decryption process utilises pikepdf, which is built off of qpdf. 

**Code:**
```python
import pikepdf as pikepdf

with pikepdf.open('file.pdf') as pdf:
  pdf.save('non-encrypted-file.pdf')
  print('Operation completed')
```

*******************

Author: **pj1301** 