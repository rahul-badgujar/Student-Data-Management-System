from tkinter import *
from tkinter import ttk

class Screen(Frame):
    def __init__(self,root):
        self._master=root
        super().__init__(self._master)

    def draw(self):
        self.grid(row=0,column=0)
        self._master.rowconfigure(0,weight=1)
        self._master.columnconfigure(0,weight=1)


if __name__ == "__main__":
    temp_window=Tk()
    temp_window.geometry('800x600')
    test_screen=Screen(temp_window)
    test_screen.draw()
    temp_window.mainloop()