import json
import time
import rumps
from ScorcsoftCore import config
from PyQt5.QtCore import QTime
from PyQt5 import QtCore, QtGui, QtWidgets
import ScorcsoftCore.ScorcsoftUtils as scorcsoftUtils


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(610, 748)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setGeometry(QtCore.QRect(225, 680, 160, 32))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(70, 340, 480, 2))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(70, 470, 81, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.listView_2 = QtWidgets.QListView(self.centralwidget)
        self.listView_2.setGeometry(QtCore.QRect(60, 290, 500, 100))
        self.listView_2.setObjectName("listView_2")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(70, 110, 480, 2))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(60, 60, 500, 150))
        self.listView.setObjectName("listView")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 170, 60, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.listView_3 = QtWidgets.QListView(self.centralwidget)
        self.listView_3.setGeometry(QtCore.QRect(60, 460, 500, 200))
        self.listView_3.setObjectName("listView_3")
        self.input_countdown_note = QtWidgets.QLineEdit(self.centralwidget)
        self.input_countdown_note.setGeometry(QtCore.QRect(430, 70, 113, 30))
        self.input_countdown_note.setObjectName("input_countdown_note")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(70, 160, 480, 2))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 70, 81, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(50, 260, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(70, 210, 491, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color=rgb(170, 170, 170)")
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(50, 410, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(70, 510, 480, 2))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 30, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(70, 560, 480, 2))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.input_wage = QtWidgets.QLineEdit(self.centralwidget)
        self.input_wage.setGeometry(QtCore.QRect(430, 570, 113, 30))
        self.input_wage.setObjectName("input_wage")
        self.timeEdit_start_time = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit_start_time.setGeometry(QtCore.QRect(430, 120, 118, 30))
        self.timeEdit_start_time.setObjectName("timeEdit_start_time")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(70, 610, 480, 2))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(80, 570, 81, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(80, 350, 81, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.input_percent_note = QtWidgets.QLineEdit(self.centralwidget)
        self.input_percent_note.setGeometry(QtCore.QRect(430, 300, 113, 30))
        self.input_percent_note.setObjectName("input_percent_note")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 120, 60, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(80, 300, 81, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(80, 520, 81, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.input_wage_note = QtWidgets.QLineEdit(self.centralwidget)
        self.input_wage_note.setGeometry(QtCore.QRect(430, 470, 113, 30))
        self.input_wage_note.setObjectName("input_wage_note")
        self.input_wage_symbol = QtWidgets.QLineEdit(self.centralwidget)
        self.input_wage_symbol.setGeometry(QtCore.QRect(430, 520, 113, 30))
        self.input_wage_symbol.setObjectName("input_wage_symbol")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(80, 620, 81, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.switch_wage = QtWidgets.QComboBox(self.centralwidget)
        self.switch_wage.setGeometry(QtCore.QRect(430, 620, 113, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.switch_wage.setFont(font)
        self.switch_wage.setObjectName("switch_wage")
        self.switch_wage.addItem("")
        self.switch_wage.addItem("")
        self.switch_percent = QtWidgets.QComboBox(self.centralwidget)
        self.switch_percent.setGeometry(QtCore.QRect(430, 350, 113, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.switch_percent.setFont(font)
        self.switch_percent.setObjectName("switch_percent")
        self.switch_percent.addItem("")
        self.switch_percent.addItem("")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(80, 470, 81, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(70, 110, 480, 2))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(70, 340, 480, 2))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.timeEdit_end_time = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit_end_time.setGeometry(QtCore.QRect(430, 170, 118, 30))
        self.timeEdit_end_time.setObjectName("timeEdit_end_time")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(70, 420, 491, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color=rgb(170, 170, 170)")
        self.label_15.setWordWrap(True)
        self.label_15.setObjectName("label_15")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        self.retranslateUi(MainWindow)
        self.buttonBox.rejected.connect(MainWindow.close)
        self.buttonBox.accepted.connect(self.saveSetting)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(f"🐒Monkey APP HW-2024限定版🍌🐒")
        self.label_10.setText(_translate("MainWindow", "日薪提示词"))
        self.label_2.setText(_translate("MainWindow", "下班时间"))
        self.label_3.setText(_translate("MainWindow", "倒计时提示词"))
        self.label_6.setText(_translate("MainWindow", "百分比功能🐒"))
        self.label_5.setText(_translate("MainWindow", "如果你的下班涉及跨天，例如上班时间17:00，下班时间01:00，则会自动计算为次日的01:00。不会出现上班时间小于下班时间的情况。🍌🐒"))
        self.label_9.setText(_translate("MainWindow", "日薪功能🐒"))
        self.label_4.setText(_translate("MainWindow", "倒计时功能🐒"))
        self.label_12.setText(_translate("MainWindow", "日薪（元）"))
        self.label_8.setText(_translate("MainWindow", "显示百分比"))
        self.label.setText(_translate("MainWindow", "上班时间"))
        self.label_7.setText(_translate("MainWindow", "百分比提示词"))
        self.label_11.setText(_translate("MainWindow", "日薪符号"))
        self.label_13.setText(_translate("MainWindow", "显示日薪"))
        self.switch_wage.setItemText(0, _translate("MainWindow", "显示"))
        self.switch_wage.setItemText(1, _translate("MainWindow", "不显示"))
        self.switch_percent.setItemText(0, _translate("MainWindow", "显示"))
        self.switch_percent.setItemText(1, _translate("MainWindow", "不显示"))
        self.label_14.setText(_translate("MainWindow", "日薪提示词"))
        self.label_15.setText(_translate("MainWindow", "强烈建议打开此功能🐒，看着每秒增加的元子💰，封起 IP 来更有劲er！！！全给他封咯🍌🐒！！！"))

        try:
            if 'countdown_note' in config.Settings.keys():
                self.input_countdown_note.setText(config.Settings['countdown_note'])

            if 'percent_note' in config.Settings.keys():
                self.input_percent_note.setText(config.Settings['percent_note'])

            if 'percent_display' in config.Settings.keys():
                if config.Settings['percent_display'] in [0, 1]:
                    self.switch_percent.setCurrentIndex(int(config.Settings['percent_display']))
                else:
                    self.switch_percent.setCurrentIndex(1)

            if 'wage_note' in config.Settings.keys():
                self.input_wage_note.setText(config.Settings['wage_note'])
            if 'wage_symbol' in config.Settings.keys():
                self.input_wage_symbol.setText(config.Settings['wage_symbol'])
            if 'wage' in config.Settings.keys():
                self.input_wage.setText(str(config.Settings['wage']))

            if 'wage_display' in config.Settings.keys():
                if config.Settings['wage_display'] in [0, 1]:
                    self.switch_wage.setCurrentIndex(int(config.Settings['wage_display']))
                else:
                    self.switch_wage.setCurrentIndex(1)

            if 'start_time' in config.Settings.keys():
                timeSet = config.Settings['start_time'].split(':')
                self.timeEdit_start_time.setTime(QTime(int(timeSet[0]), int(timeSet[1])))
            if 'end_time' in config.Settings.keys():
                timeSet = config.Settings['end_time'].split(':')
                self.timeEdit_end_time.setTime(QTime(int(timeSet[0]), int(timeSet[1])))
        except:
            pass

    def saveSetting(self):
        # 倒计时功能
        countdownNote = self.input_countdown_note.text()
        startTime = self.timeEdit_start_time.text()
        endTime = self.timeEdit_end_time.text()

        # 百分比功能
        percentNote = self.input_percent_note.text()
        percentDisplay = self.switch_percent.currentIndex()

        # 日薪功能
        wageNote = self.input_wage_note.text()
        wageSymbol = self.input_wage_symbol.text()
        wageDisplay = self.switch_wage.currentIndex()
        try:
            wage = int(self.input_wage.text())
        except:
            wage = 0

        config.Settings = {
            'countdown_note': countdownNote,
            'start_time': startTime,
            'end_time': endTime,
            'percent_note': percentNote,
            'percent_display': percentDisplay,
            'wage_note': wageNote,
            'wage_symbol': wageSymbol,
            'wage': wage,
            'wage_display': wageDisplay
        }
        try:
            fp = open('config.json', 'w')
            fp.write(json.dumps(config.Settings))
            fp.close()
        except:
            pass
