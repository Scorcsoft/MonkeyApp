import sys
from ScorcsoftCore import settingsUI
from PyQt5.QtWidgets import QApplication, QMainWindow


def setting():
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()

    ui = settingsUI.Ui_MainWindow()
    ui.setupUi(MainWindow)

    MainWindow.show()
    MainWindow.setMinimumSize(610, 748)
    MainWindow.setMaximumSize(610, 748)
    MainWindow.raise_()

    sys.exit(app.exec_())
