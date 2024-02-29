from .event import Event
from .authorizationWindow import AuthorizationWindow
from .mainWindow import MainWindow


class _UIManager:
    def __init__(self):
        self._activeWindow = None

        self.onButtonShowDateClicked = Event()
        self.onButtonListDirClicked = Event()
        self.onButtonCreateDirClicked = Event()
        self.onButtonTouchClicked = Event()
        self.onButtonCopyFileClicked = Event()
        self.onButtonDeleteTreeClicked = Event()

    def createAutorizationWindow(self):
        if self._activeWindow is None:
            self._activeWindow = AuthorizationWindow()
        if isinstance(self._activeWindow, AuthorizationWindow):
            self._activeWindow.mainloop()

    def createMainWindow(self):
        if self._activeWindow is None:
            self._activeWindow = MainWindow()
        if isinstance(self._activeWindow, MainWindow):
            self._activeWindow.mainloop()

    # def createWindow(self, windowClass, *args):
    #     newWindow = windowClass(*args)
    #     if self._activeWindow is not None:
    #         self._activeWindow.withdraw()
    #         newWindow.mainloop()
    #         self._activeWindow.destroy()
    #     else:
    #         newWindow.mainloop()
    #     self._activeWindow = newWindow

    def onDestroy(self):
        self._activeWindow.quit()
        self._activeWindow.destroy()


g_UiManager = _UIManager()
