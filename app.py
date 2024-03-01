from initializer.initializer import Initializer
from ui.mainWindow import MainWindow
from ui.authorizationWindow import AuthorizationWindow
from ui.uiManager import uiManager


class App:


    def __init__(self):
        Initializer.run()

    def run(self):
        uiManager.createWindow(AuthorizationWindow)
