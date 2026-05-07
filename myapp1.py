# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'oo.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QRadioButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionopen = QAction(MainWindow)
        self.actionopen.setObjectName(u"actionopen")
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(380, 50, 191, 26))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, 50, 71, 31))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(130, 120, 31, 21))
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(380, 110, 191, 26))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(120, 200, 49, 16))
        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(380, 190, 191, 26))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(130, 260, 49, 16))
        self.radioButton = QRadioButton(self.centralwidget)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(310, 260, 98, 24))
        self.radioButton_2 = QRadioButton(self.centralwidget)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(490, 260, 98, 24))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(120, 340, 49, 16))
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(370, 340, 181, 26))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(110, 460, 81, 26))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(260, 460, 81, 26))
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(420, 460, 81, 26))
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(550, 460, 81, 26))
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(90, 30, 511, 351))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionopen)
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionExit)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionopen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0e23\u0e2b\u0e31\u0e2a\u0e19\u0e31\u0e01\u0e28\u0e36\u0e01\u0e29\u0e32", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0e0a\u0e37\u0e48\u0e2d  ", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0e19\u0e32\u0e21\u0e2a\u0e01\u0e38\u0e25", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0e40\u0e1e\u0e28", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"\u0e0a\u0e32\u0e22", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0e2b\u0e0d\u0e34\u0e07", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0e2a\u0e32\u0e02\u0e32\u0e27\u0e34\u0e0a\u0e32", None))
        self.comboBox.setItemText(0, "")
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0e27\u0e34\u0e17\u0e22\u0e32\u0e28\u0e32\u0e15\u0e23\u0e4c", None))

        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0e25\u0e49\u0e32\u0e07", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0e25\u0e1a", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u0e41\u0e01\u0e49\u0e44\u0e02", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u0e1a\u0e31\u0e19\u0e17\u0e36\u0e01", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

# --- เติมส่วนนี้ต่อท้ายไฟล์เดิมของคุณ ---
import sys

# ส่วนประกาศ Slot (ฟังก์ชัน)
def say_hello(self):
    print("สวัสดีครับ! นักศึกษา")

if __name__ == "__main__":
    # 1. สร้างตัวจัดการแอปพลิเคชัน
    app = QApplication(sys.argv)

    # 2. สร้างหน้าต่างหลัก (Container)
    MainWindow = QMainWindow()

    # 3. สร้างอินสแตนซ์ UI ของคุณ แล้วโหลดใส่หน้าต่างหลัก
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    # --- Signal / Slot ---
    # สร้างปุ่มมา กดแล้วแสดงข้อความ
    ui.pushButton.clicked.connect(lambda: say_hello(ui))

    # 4. โชว์หน้าต่าง
    MainWindow.show()

    # 5. รันลูปการทำงาน (Event Loop)
    sys.exit(app.exec())