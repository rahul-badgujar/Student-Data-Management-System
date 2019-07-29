from tkinter import *
from tkinter import ttk


class SystemManager:
    # Constructor
    def __init__(self, sys_name, sys_geometry):
        self._system_name = sys_name
        self._system_geometry = sys_geometry

        # Configure System Window
        self._main_window = Tk()
        self._main_window.title(self._system_name)
        self._main_window.geometry(self._system_geometry)

    def run(self):
        # Run the mainloop for Window
        self._main_window.mainloop()


# for Unit Tests
if __name__ == "__main__":
    print('Performing Test in System Module\n')

    test_system = SystemManager(
        'Student Data Management System', '800x600')
    test_system.run()
