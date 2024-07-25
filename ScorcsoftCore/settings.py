import sys
from ScorcsoftCore import settingsUI
import ScorcsoftCore.config as config
from PyQt5.QtWidgets import QApplication, QMainWindow


def setting():
    if config.settingUI is None:
        app = QApplication(sys.argv)
        MainWindow = QMainWindow()
        ui = settingsUI.Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        MainWindow.setMinimumSize(610, 748)
        MainWindow.setMaximumSize(610, 748)
        MainWindow.raise_()
        config.settingUI = MainWindow
        app.exec_()
        config.settingUI = None
    else:
        config.settingUI.raise_()

