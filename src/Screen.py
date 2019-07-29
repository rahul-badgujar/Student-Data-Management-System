from tkinter import *
from tkinter import ttk
from Utilities import GUIPicker


class Screen(ttk.Frame):
    def __init__(self, root):
        # Configure the Parent Window
        self._master = root
        super().__init__(self._master)

        self._gui_picker = GUIPicker(self)

    def draw(self):
        # Draws the widgets
        self.grid(row=0, column=0)
        #self._master.rowconfigure(0, weight=1)
        #self._master.columnconfigure(0, weight=1)


class MainmenuScreen(Screen):
    # Path for Images
    main_logo_path = 'assets\images\main_icon.png'

    def __init__(self, root):
        super().__init__(root)

        self.__main_logo_label = self._gui_picker.pickImageLabel(
            MainmenuScreen.main_logo_path)

    def draw(self):
        self.__main_logo_label.grid(row=0, column=0)

        super().draw()


if __name__ == "__main__":
    print('Performing Test in Screen Module\n')

    temp_window = Tk()
    temp_window.geometry('800x600')
    test_screen = MainmenuScreen(temp_window)
    test_screen.draw()
    temp_window.mainloop()
