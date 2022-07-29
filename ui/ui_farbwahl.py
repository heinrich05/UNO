# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'farbwahlqwmNVk.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 146)
        self.button_rot = QPushButton(Dialog)
        self.button_rot.setObjectName(u"button_rot")
        self.button_rot.setGeometry(QRect(20, 90, 75, 24))
        self.button_gruen = QPushButton(Dialog)
        self.button_gruen.setObjectName(u"button_gruen")
        self.button_gruen.setGeometry(QRect(115, 90, 75, 24))
        self.button_blau = QPushButton(Dialog)
        self.button_blau.setObjectName(u"button_blau")
        self.button_blau.setGeometry(QRect(210, 90, 75, 24))
        self.button_gelb = QPushButton(Dialog)
        self.button_gelb.setObjectName(u"button_gelb")
        self.button_gelb.setGeometry(QRect(305, 90, 75, 24))
        self.farbwahl_text = QLabel(Dialog)
        self.farbwahl_text.setObjectName(u"farbwahl_text")
        self.farbwahl_text.setGeometry(QRect(90, 40, 240, 16))
        font = QFont()
        font.setPointSize(11)
        self.farbwahl_text.setFont(font)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.button_rot.setText(QCoreApplication.translate("Dialog", u"Rot", None))
        self.button_gruen.setText(QCoreApplication.translate("Dialog", u"Gr\u00fcn", None))
        self.button_blau.setText(QCoreApplication.translate("Dialog", u"Blau", None))
        self.button_gelb.setText(QCoreApplication.translate("Dialog", u"Gelb", None))
        self.farbwahl_text.setText(QCoreApplication.translate("Dialog", u"Welche Farbe m\u00f6chtest Du w\u00e4hlen?", None))
    # retranslateUi

