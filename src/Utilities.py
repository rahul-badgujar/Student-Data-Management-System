from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


class GUIPicker:
    def __init__(self, master):
        self.__master = master

    # Label
    def pickLabel(self,text):
        label=Label(self.__master,text=text,bg=self.__master['bg'])
        return label

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
                        cursor=cursorType, command=callback, bd=0)
        button.image = img
        return button

    # Entry
    def pickEntry(self, textvar=None):
        entry = Entry(self.__master,
                          textvariable=textvar)
        return entry

    # Spinbox
    def pickSpinbox(self, possible_values=None, textvar=None):
        spinbox = ttk.Spinbox(
            self.__master, values=possible_values, textvariable=textvar)
        return spinbox

    # Combobox
    def pickCombobox(self, possible_values=None, textvar=None):
        combobox = ttk.Combobox(
            self.__master, values=possible_values, textvariable=textvar)
        return combobox


if __name__ == "__main__":
    print('Performing Test in Utilities Module\n')
