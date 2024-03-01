from .authorizationWindow import AuthorizationWindow
from .mainWindow import MainWindow


class UIManager:
    def __init__(self):
        self._activeWindow = None

    def createWindow(self, windowClass, *args):
        newWindow = windowClass(self, *args)
        if self._activeWindow is not None:
            self._activeWindow.withdraw()
            newWindow.mainloop()
            self._activeWindow.destroy()
        else:
            self._activeWindow = newWindow
            newWindow.mainloop()


uiManager = UIManager()
