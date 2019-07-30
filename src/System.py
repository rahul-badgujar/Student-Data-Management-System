from tkinter import *
from tkinter import ttk
from Screen import MainmenuScreen


class SystemManager:
    # Constructor
    def __init__(self, sys_name, sys_geometry):
        self._system_name = sys_name
        self._system_geometry = sys_geometry

        # Configure System Window
        self._main_window = Tk()
        self._main_window.title(self._system_name)
        self._main_window.geometry(self._system_geometry)
        self._main_window.resizable(False, False)

        # Main Menu Screen
        self.__mainmenu_screen = MainmenuScreen(
            self._main_window, self.screensReturnDataHandler)

    def run(self):
        self.__mainmenu_screen.draw()
        # Run the mainloop for Window
        self._main_window.mainloop()

    def screensReturnDataHandler(self, data):
        self.__mainmenu_screen.clean()
        if data[0] is 'MAINMENU_SCREEN':
            if data[1] is 'EXIT':
                self._main_window.destroy()
            elif data[1] is 'SEARCH':
                search_type = data[2][0]
                search_entry = data[2][1]
                print(search_type, search_entry)
            elif data[1] is 'ADD':
                print('No handling implemented yet for '+data[1])
            elif data[1] is 'MODIFY':
                print('No handling implemented yet for '+data[1])
            elif data[1] is 'DELETE':
                print('No handling implemented yet for '+data[1])


# for Unit Tests
if __name__ == "__main__":
    print('Performing Test in System Module\n')

    test_system = SystemManager(
        'Student Data Management System', '800x600')
    test_system.run()
