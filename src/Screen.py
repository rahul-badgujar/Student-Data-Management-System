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
        self.place(relx=0, rely=0, relwidth=1, relheight=1)


class MainmenuScreen(Screen):
    # Path for Images
    main_logo_path = 'assets\images\main_icon.png'
    search_icon_path = 'assets\images\search_icon.png'
    add_icon_normal_path = 'assets\images\\add_icon_normal.png'
    add_icon_mouseover_path = 'assets\images\\add_icon_mouseover.png'
    modify_icon_normal_path = 'assets\images\modify_icon_normal.png'
    modify_icon_mouseover_path = 'assets\images\modify_icon_mouseover.png'
    delete_icon_normal_path = 'assets\images\delete_icon_normal.png'
    delete_icon_mouseover_path = 'assets\images\delete_icon_mouseover.png'
    exit_icon_normal_path = 'assets\images\exit_icon_normal.png'
    exit_icon_mouseover_path = 'assets\images\exit_icon_mouseover.png'

    # Useful Values Tuples
    search_type_spinbox_values = (
        'Roll Number', 'Name', 'Year of Joining')

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
        self.__search_type_spinbox.configure()

        # Search Entry
        self.__search_entry_textvar = StringVar(None, 'Enter here')
        self.__search_entry = self._gui_picker.pickEntry(
            self.__search_entry_textvar)

        # Search Button
        self.__search_button_image = self._gui_picker.pickImage(
            MainmenuScreen.search_icon_path)
        self.__search_button = self._gui_picker.pickImageButton(
            self.__search_button_image)

        # Add Button
        self.__add_button_image_normal = self._gui_picker.pickImage(
            MainmenuScreen.add_icon_normal_path)
        self.__add_button_image_mouseover = self._gui_picker.pickImage(
            MainmenuScreen.add_icon_mouseover_path)
        self.__add_button = self._gui_picker.pickImageButton(
            self.__add_button_image_normal)
        self.__add_button.bind('<Enter>', lambda e: self.__add_button.configure(
            image=self.__add_button_image_mouseover))
        self.__add_button.bind('<Leave>', lambda e: self.__add_button.configure(
            image=self.__add_button_image_normal))

        # Modify Button
        self.__modify_button_image_normal = self._gui_picker.pickImage(
            MainmenuScreen.modify_icon_normal_path)
        self.__modify_button_image_mouseover = self._gui_picker.pickImage(
            MainmenuScreen.modify_icon_mouseover_path)
        self.__modify_button = self._gui_picker.pickImageButton(
            self.__modify_button_image_normal)
        self.__modify_button.bind('<Enter>', lambda e: self.__modify_button.configure(
            image=self.__modify_button_image_mouseover))
        self.__modify_button.bind('<Leave>', lambda e: self.__modify_button.configure(
            image=self.__modify_button_image_normal))

        # Delete Button
        self.__delete_button_image_normal = self._gui_picker.pickImage(
            MainmenuScreen.delete_icon_normal_path)
        self.__delete_button_image_mouseover = self._gui_picker.pickImage(
            MainmenuScreen.delete_icon_mouseover_path)
        self.__delete_button = self._gui_picker.pickImageButton(
            self.__delete_button_image_normal)
        self.__delete_button.bind('<Enter>', lambda e: self.__delete_button.configure(
            image=self.__delete_button_image_mouseover))
        self.__delete_button.bind('<Leave>', lambda e: self.__delete_button.configure(
            image=self.__delete_button_image_normal))

        # Exit Button
        self.__exit_button_image_normal = self._gui_picker.pickImage(
            MainmenuScreen.exit_icon_normal_path)
        self.__exit_button_image_mouseover = self._gui_picker.pickImage(
            MainmenuScreen.exit_icon_mouseover_path)
        self.__exit_button = self._gui_picker.pickImageButton(
            self.__exit_button_image_normal)
        self.__exit_button.bind('<Enter>', lambda e: self.__exit_button.configure(
            image=self.__exit_button_image_mouseover))
        self.__exit_button.bind('<Leave>', lambda e: self.__exit_button.configure(
            image=self.__exit_button_image_normal))

    def draw(self):
        # Main Logo
        self.__main_logo_label.place(
            relx=0.3, rely=0.02, relheight=0.45, relwidth=.5)

        # Search Type Spinbox
        self.__search_type_spinbox.place(
            relx=0.16, rely=0.55, relheight=0.06, relwidth=0.14)

        # Search Entry
        self.__search_entry.place(
            relx=0.33, rely=0.55, relheight=0.06, relwidth=.44)

        # Search Button
        self.__search_button.place(
            relx=0.77, rely=0.55, relheight=0.06, relwidth=0.05)

        # Add Button
        self.__add_button.place(relx=0.05, rely=0.7,
                                relheight=0.193, relwidth=.13)

        # Modify Button
        self.__modify_button.place(
            relx=0.3, rely=0.7, relheight=0.193, relwidth=.13)

        # Delete Button
        self.__delete_button.place(
            relx=0.57, rely=0.7, relheight=0.193, relwidth=.13)

        # Exit Button
        self.__exit_button.place(relx=0.81, rely=0.7,
                                 relheight=0.193, relwidth=.13)

        super().draw()


if __name__ == "__main__":
    print('Performing Test in Screen Module\n')

    temp_window = Tk()
    temp_window.geometry('800x600')
    temp_window.resizable(False, False)
    test_screen = MainmenuScreen(temp_window)
    test_screen.draw()
    temp_window.mainloop()
