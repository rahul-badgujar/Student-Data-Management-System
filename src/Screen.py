from tkinter import *
from tkinter import ttk


class Screen(ttk.Frame):
    def __init__(self, root):
        # Configure the Parent Window
        self._master = root
        super().__init__(self._master)

    def draw(self):
        # Draws the widgets
        self.grid(row=0, column=0)
        self._master.rowconfigure(0, weight=1)
        self._master.columnconfigure(0, weight=1)


class MainmenuScreen(Screen):
    def __init__(self, root):
        super().__init__(root)

        self.__intro_label = ttk.Label(
            self, text='This is gonna be our Mainmenu Screen')

    def draw(self):
        self.__intro_label.grid(row=0, column=0)

        super().draw()


if __name__ == "__main__":
    temp_window = Tk()
    temp_window.geometry('800x600')
    test_screen = MainmenuScreen(temp_window)
    test_screen.draw()
    temp_window.mainloop()
