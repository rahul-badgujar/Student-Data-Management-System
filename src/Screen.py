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
    search_icon_normal_path = 'assets\images\search_icon_normal.png'
    search_icon_mouseover_path = 'assets\images\search_icon_mouseover.png'

    # Useful Values Tuples
    search_type_spinbox_values = (
        'Search by Roll Number', 'Search by Name', 'Search by Year of Joining')

    def __init__(self, root):
        super().__init__(root)

        # Main Logo
        self.__main_logo_image = self._gui_picker.pickImage(
            MainmenuScreen.main_logo_path)
        self.__main_logo_label = self._gui_picker.pickImageLabel(
            self.__main_logo_image)

        # Search Type Spinbox
        self.__search_type_textvar = StringVar(
            None, MainmenuScreen.search_type_spinbox_values[0])
        self.__search_type_spinbox = self._gui_picker.pickSpinbox(
            MainmenuScreen.search_type_spinbox_values, self.__search_type_textvar)
        self.__search_type_spinbox.configure(width=25)

        # Search Entry
        self.__search_entry_textvar = StringVar(None, 'Enter here')
        self.__search_entry = self._gui_picker.pickEntry(
            self.__search_entry_textvar)

        # Search Button
        self.__search_button_image_normal = self._gui_picker.pickImage(
            MainmenuScreen.search_icon_normal_path)
        self.__search_button_image_mouseover = self._gui_picker.pickImage(
            MainmenuScreen.search_icon_mouseover_path)
        self.__search_button = self._gui_picker.pickImageButton(
            self.__search_button_image_normal)
        self.__search_button.bind('<Enter>', lambda e: self.__search_button.configure(
            image=self.__search_button_image_mouseover))
        self.__search_button.bind('<Leave>', lambda e: self.__search_button.configure(
            image=self.__search_button_image_normal))

    def draw(self):
        # Main Logo
        self.__main_logo_label.grid(
            row=0, column=0, columnspan=4, pady=40)

        # Search Type Spinbox
        self.__search_type_spinbox.grid(row=2, column=0)

        # Search Entry
        self.__search_entry.grid(row=2, column=1, columnspan=2)

        # Search Button
        self.__search_button.grid(row=2, column=3)

        super().draw()


if __name__ == "__main__":
    print('Performing Test in Screen Module\n')

    temp_window = Tk()
    temp_window.geometry('800x600')
    test_screen = MainmenuScreen(temp_window)
    test_screen.draw()
    temp_window.mainloop()
