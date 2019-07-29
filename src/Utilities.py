from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


class GUIPicker:
    def __init__(self, master):
        self.__master = master

    # Image Label
    def pickImageLabel(self, img):
        label = ttk.Label(self.__master, image=img)
        label.image = img
        return label

    def pickImage(self, path):
        img = ImageTk.PhotoImage(Image.open(path))
        return img

    # Image Button
    def pickImageButton(self, img, callback=None, cursorType='hand2'):
        button = Button(self.__master, image=img,
                            cursor=cursorType, command=callback,bd=0)
        button.image = img
        return button

    # Entry
    def pickEntry(self,textvar=None):
        entry = ttk.Entry(self.__master,foreground='grey',textvariable=textvar)
        return entry

    # Spinbox
    def pickSpinbox(self,possible_values=None,textvar=None):
        spinbox=ttk.Spinbox(self.__master,values=possible_values,textvariable=textvar)
        return spinbox
        


if __name__ == "__main__":
    print('Performing Test in Utilities Module\n')
