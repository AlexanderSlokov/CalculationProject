from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import pyqtSignal, QObject

class Ui_MainWindowExcutable(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1253, 783)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_20 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(640, 140, 201, 61))
        self.label_20.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.label_20.setObjectName("label_20")
        self.banker_groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.banker_groupBox.setGeometry(QtCore.QRect(20, 220, 591, 411))
        self.banker_groupBox.setAutoFillBackground(False)
        self.banker_groupBox.setStyleSheet("background-color: rgb(214, 214, 214);")
        self.banker_groupBox.setObjectName("banker_groupBox")
        self.hk_banker_input_Edit = QtWidgets.QLineEdit(parent=self.banker_groupBox)
        self.hk_banker_input_Edit.setGeometry(QtCore.QRect(250, 160, 141, 31))
        self.hk_banker_input_Edit.setObjectName("hk_banker_input_Edit")
        self.label_2 = QtWidgets.QLabel(parent=self.banker_groupBox)
        self.label_2.setGeometry(QtCore.QRect(150, 100, 231, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(156, 30, 21);\n"
"font: 75 16pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.banker_groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 150, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(156, 30, 21);")
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(parent=self.banker_groupBox)
        self.label.setGeometry(QtCore.QRect(20, 60, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(156, 30, 21);")
        self.label.setObjectName("label")
        self.banker_total_label = QtWidgets.QLabel(parent=self.banker_groupBox)
        self.banker_total_label.setGeometry(QtCore.QRect(250, 60, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.banker_total_label.setFont(font)
        self.banker_total_label.setObjectName("banker_total_label")
        self.label_7 = QtWidgets.QLabel(parent=self.banker_groupBox)
        self.label_7.setGeometry(QtCore.QRect(20, 200, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(156, 30, 21);")
        self.label_7.setObjectName("label_7")
        self.label_14 = QtWidgets.QLabel(parent=self.banker_groupBox)
        self.label_14.setGeometry(QtCore.QRect(40, 270, 55, 16))
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(parent=self.banker_groupBox)
        self.label_15.setGeometry(QtCore.QRect(20, 260, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: rgb(156, 30, 21);")
        self.label_15.setObjectName("label_15")
        self.betRate_banker_Edit = QtWidgets.QLineEdit(parent=self.banker_groupBox)
        self.betRate_banker_Edit.setGeometry(QtCore.QRect(250, 270, 141, 31))
        self.betRate_banker_Edit.setObjectName("betRate_banker_Edit")
        self.malay_value_followHK_label = QtWidgets.QLabel(parent=self.banker_groupBox)
        self.malay_value_followHK_label.setGeometry(QtCore.QRect(250, 200, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.malay_value_followHK_label.setFont(font)
        self.malay_value_followHK_label.setObjectName("malay_value_followHK_label")
        self.banker_plus_1000_pushButton = QtWidgets.QPushButton(parent=self.banker_groupBox)
        self.banker_plus_1000_pushButton.setGeometry(QtCore.QRect(20, 340, 93, 28))
        self.banker_plus_1000_pushButton.setStyleSheet("background-color: rgb(166, 0, 3);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.banker_plus_1000_pushButton.setObjectName("banker_plus_1000_pushButton")
        self.banker_plus_2000_pushButton = QtWidgets.QPushButton(parent=self.banker_groupBox)
        self.banker_plus_2000_pushButton.setGeometry(QtCore.QRect(130, 340, 93, 28))
        self.banker_plus_2000_pushButton.setStyleSheet("background-color: rgb(166, 0, 3);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.banker_plus_2000_pushButton.setObjectName("banker_plus_2000_pushButton")
        self.banker_plus_3000_pushButton = QtWidgets.QPushButton(parent=self.banker_groupBox)
        self.banker_plus_3000_pushButton.setGeometry(QtCore.QRect(240, 340, 93, 28))
        self.banker_plus_3000_pushButton.setStyleSheet("background-color: rgb(166, 0, 3);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.banker_plus_3000_pushButton.setObjectName("banker_plus_3000_pushButton")
        self.banker_plus_5000_pushButton = QtWidgets.QPushButton(parent=self.banker_groupBox)
        self.banker_plus_5000_pushButton.setGeometry(QtCore.QRect(460, 340, 93, 28))
        self.banker_plus_5000_pushButton.setStyleSheet("background-color: rgb(166, 0, 3);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.banker_plus_5000_pushButton.setObjectName("banker_plus_5000_pushButton")
        self.banker_plus_4000_pushButton = QtWidgets.QPushButton(parent=self.banker_groupBox)
        self.banker_plus_4000_pushButton.setGeometry(QtCore.QRect(350, 340, 93, 28))
        self.banker_plus_4000_pushButton.setStyleSheet("background-color: rgb(166, 0, 3);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.banker_plus_4000_pushButton.setObjectName("banker_plus_4000_pushButton")
        self.player_apply_pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.player_apply_pushButton.setGeometry(QtCore.QRect(530, 640, 191, 81))
        self.player_apply_pushButton.setAutoFillBackground(False)
        self.player_apply_pushButton.setStyleSheet("background-color: rgb(0, 147, 29);\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.player_apply_pushButton.setObjectName("player_apply_pushButton")
        self.player_groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.player_groupBox.setGeometry(QtCore.QRect(640, 220, 591, 411))
        self.player_groupBox.setStyleSheet("background-color: rgb(214, 214, 214);")
        self.player_groupBox.setObjectName("player_groupBox")
        self.hk_player_input_Edit = QtWidgets.QLineEdit(parent=self.player_groupBox)
        self.hk_player_input_Edit.setGeometry(QtCore.QRect(250, 160, 141, 31))
        self.hk_player_input_Edit.setObjectName("hk_player_input_Edit")
        self.label_8 = QtWidgets.QLabel(parent=self.player_groupBox)
        self.label_8.setGeometry(QtCore.QRect(140, 100, 241, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(10, 176, 37);\n"
"font: 75 16pt \"MS Shell Dlg 2\";")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(parent=self.player_groupBox)
        self.label_9.setGeometry(QtCore.QRect(20, 150, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(10, 176, 37)")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(parent=self.player_groupBox)
        self.label_10.setGeometry(QtCore.QRect(20, 60, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(10, 176, 37)")
        self.label_10.setObjectName("label_10")
        self.player_total_label = QtWidgets.QLabel(parent=self.player_groupBox)
        self.player_total_label.setGeometry(QtCore.QRect(250, 60, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.player_total_label.setFont(font)
        self.player_total_label.setObjectName("player_total_label")
        self.label_13 = QtWidgets.QLabel(parent=self.player_groupBox)
        self.label_13.setGeometry(QtCore.QRect(20, 200, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: rgb(10, 176, 37)")
        self.label_13.setObjectName("label_13")
        self.label_17 = QtWidgets.QLabel(parent=self.player_groupBox)
        self.label_17.setGeometry(QtCore.QRect(40, 270, 55, 16))
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(parent=self.player_groupBox)
        self.label_18.setGeometry(QtCore.QRect(20, 270, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("color: rgb(10, 176, 37)")
        self.label_18.setObjectName("label_18")
        self.betRate_banker_player_Edit = QtWidgets.QLineEdit(parent=self.player_groupBox)
        self.betRate_banker_player_Edit.setGeometry(QtCore.QRect(250, 280, 141, 31))
        self.betRate_banker_player_Edit.setObjectName("betRate_banker_player_Edit")
        self.player_malay_value_followHK_label = QtWidgets.QLabel(parent=self.player_groupBox)
        self.player_malay_value_followHK_label.setGeometry(QtCore.QRect(250, 200, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.player_malay_value_followHK_label.setFont(font)
        self.player_malay_value_followHK_label.setObjectName("player_malay_value_followHK_label")
        self.player_plus_3000_pushButton = QtWidgets.QPushButton(parent=self.player_groupBox)
        self.player_plus_3000_pushButton.setGeometry(QtCore.QRect(250, 340, 93, 28))
        self.player_plus_3000_pushButton.setStyleSheet("background-color: rgb(0, 180, 0);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.player_plus_3000_pushButton.setObjectName("player_plus_3000_pushButton")
        self.player_plus_1000_pushButton = QtWidgets.QPushButton(parent=self.player_groupBox)
        self.player_plus_1000_pushButton.setGeometry(QtCore.QRect(30, 340, 93, 28))
        self.player_plus_1000_pushButton.setStyleSheet("background-color: rgb(0, 180, 0);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.player_plus_1000_pushButton.setObjectName("player_plus_1000_pushButton")
        self.player_plus_2000_pushButton = QtWidgets.QPushButton(parent=self.player_groupBox)
        self.player_plus_2000_pushButton.setGeometry(QtCore.QRect(140, 340, 93, 28))
        self.player_plus_2000_pushButton.setStyleSheet("background-color: rgb(0, 180, 0);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.player_plus_2000_pushButton.setObjectName("player_plus_2000_pushButton")
        self.player_plus_5000_pushButton = QtWidgets.QPushButton(parent=self.player_groupBox)
        self.player_plus_5000_pushButton.setGeometry(QtCore.QRect(470, 340, 93, 28))
        self.player_plus_5000_pushButton.setStyleSheet("background-color: rgb(0, 180, 0);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.player_plus_5000_pushButton.setObjectName("player_plus_5000_pushButton")
        self.player_plus_4000_pushButton = QtWidgets.QPushButton(parent=self.player_groupBox)
        self.player_plus_4000_pushButton.setGeometry(QtCore.QRect(360, 340, 93, 28))
        self.player_plus_4000_pushButton.setStyleSheet("background-color: rgb(0, 180, 0);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.player_plus_4000_pushButton.setObjectName("player_plus_4000_pushButton")
        self.image_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.image_label.setGeometry(QtCore.QRect(10, 10, 281, 201))
        self.image_label.setStyleSheet("image: url(:/newPrefix/money.jpg);")
        self.image_label.setText("")
        self.image_label.setObjectName("image_label")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(820, 150, 201, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.fix_malay_ratio_pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.fix_malay_ratio_pushButton.setGeometry(QtCore.QRect(1040, 157, 141, 31))
        self.fix_malay_ratio_pushButton.setStyleSheet("background-color: rgb(61, 227, 49);")
        self.fix_malay_ratio_pushButton.setObjectName("fix_malay_ratio_pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1253, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Fixed codes
        # variable
        self.malay_value_followHK_label.setText(str(float(0.8)))
        self.player_malay_value_followHK_label.setText(str(float(-0.94)))

        # Plus buttons events
        self.banker_plus_1000_pushButton.clicked.connect(self.plus_1000)
        self.player_plus_1000_pushButton.clicked.connect(self.player_plus_1000)

        # Apply buttons events
        self.player_apply_pushButton.clicked.connect(self.player_malay_to_hk)
        self.fix_malay_ratio_pushButton.clicked.connect(self.fix_ratios)

    def plus_1000(self):
        base_sum = int(self.betRate_banker_Edit.text())
        sum = base_sum + 1000
        self.betRate_banker_Edit.setText(str(sum))

    def player_plus_1000(self):
        base_sum = int(self.betRate_banker_player_Edit.text())
        sum = base_sum + 1000
        self.betRate_banker_player_Edit.setText(str(sum))

    # ti le hk ben theo maylay, phai bam nut apply cua player moi trigger duoc event tinh tien
    def player_malay_to_hk(self):
        player_malay = float(self.player_malay_value_followHK_label.text())
        malay = float(self.malay_value_followHK_label.text())

        if malay < 0:
            hk = 100 + 100 * (1 + malay)
        else:
            hk = 100 * malay

        self.hk_banker_input_Edit.setText(str(hk))
        self.banker_total_label.setText(str(self.betRate_banker_Edit.text()))

        if player_malay < 0:
            player_hk = 100 + 100 * (1 + player_malay)
        else:
            player_hk = 100 * player_malay

        self.hk_player_input_Edit.setText(str(player_hk))
        self.player_total_label.setText(str(self.betRate_banker_player_Edit.text()))

    def fix_ratios(self):
        max_money = int(self.lineEdit.text())
        malay_ratio_value = float(self.player_malay_value_followHK_label.text())
        betRate_difference = int(self.betRate_banker_player_Edit.text()) - int(self.betRate_banker_Edit.text())
        ratio_fix = (betRate_difference / max_money) * 0.01
        fixed = malay_ratio_value - ratio_fix
        self.player_malay_value_followHK_label.setText(str(float(fixed)))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_20.setText(_translate("MainWindow", "MAX $ SIZE:"))
        self.banker_groupBox.setTitle(_translate("MainWindow", "BANKER"))
        self.label_2.setText(_translate("MainWindow", "----Banker Odds----"))
        self.label_3.setText(_translate("MainWindow", "Hong Kong:"))
        self.label.setText(_translate("MainWindow", "Banker Bet Total:"))
        self.banker_total_label.setText(_translate("MainWindow", "Banker total number"))
        self.label_7.setText(_translate("MainWindow", "Malaysia:"))
        self.label_15.setText(_translate("MainWindow", "Bet Rate:"))
        self.malay_value_followHK_label.setText(_translate("MainWindow", "Num based on HK"))
        self.banker_plus_1000_pushButton.setText(_translate("MainWindow", "1000 $"))
        self.banker_plus_2000_pushButton.setText(_translate("MainWindow", "2000 $"))
        self.banker_plus_3000_pushButton.setText(_translate("MainWindow", "3000 $"))
        self.banker_plus_5000_pushButton.setText(_translate("MainWindow", "5000 $"))
        self.banker_plus_4000_pushButton.setText(_translate("MainWindow", "4000 $"))
        self.player_apply_pushButton.setText(_translate("MainWindow", "APPLY"))
        self.player_groupBox.setTitle(_translate("MainWindow", "PLAYER"))
        self.label_8.setText(_translate("MainWindow", "----Banker Odds----"))
        self.label_9.setText(_translate("MainWindow", "Hong Kong:"))
        self.label_10.setText(_translate("MainWindow", "Banker Bet Total:"))
        self.player_total_label.setText(_translate("MainWindow", "Player total number"))
        self.label_13.setText(_translate("MainWindow", "Malaysia:"))
        self.label_18.setText(_translate("MainWindow", "Bet Rate:"))
        self.player_malay_value_followHK_label.setText(_translate("MainWindow", "Num based on HK"))
        self.player_plus_3000_pushButton.setText(_translate("MainWindow", "3000 $"))
        self.player_plus_1000_pushButton.setText(_translate("MainWindow", "1000 $"))
        self.player_plus_2000_pushButton.setText(_translate("MainWindow", "2000 $"))
        self.player_plus_5000_pushButton.setText(_translate("MainWindow", "5000 $"))
        self.player_plus_4000_pushButton.setText(_translate("MainWindow", "4000 $"))
        self.fix_malay_ratio_pushButton.setText(_translate("MainWindow", "Config Malaysia ratio"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindowExcutable()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
