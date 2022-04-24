# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uno.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSlider, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(720, 360)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setAutoFillBackground(True)
        self.sp1_label = QLabel(self.centralwidget)
        self.sp1_label.setObjectName(u"sp1_label")
        self.sp1_label.setGeometry(QRect(90, 40, 41, 31))
        self.sp1_label.setSizeIncrement(QSize(0, 0))
        self.sp1_karte = QLabel(self.centralwidget)
        self.sp1_karte.setObjectName(u"sp1_karte")
        self.sp1_karte.setGeometry(QRect(40, 90, 100, 150))
        self.sp1_karte.setPixmap(QPixmap(u"sprites/placeholder.png"))
        self.sp1_kartenslider = QSlider(self.centralwidget)
        self.sp1_kartenslider.setObjectName(u"sp1_kartenslider")
        self.sp1_kartenslider.setGeometry(QRect(160, 90, 21, 150))
        self.sp1_kartenslider.setOrientation(Qt.Vertical)
        self.sp1_legen = QPushButton(self.centralwidget)
        self.sp1_legen.setObjectName(u"sp1_legen")
        self.sp1_legen.setGeometry(QRect(40, 260, 100, 25))
        self.sp1_uno = QCheckBox(self.centralwidget)
        self.sp1_uno.setObjectName(u"sp1_uno")
        self.sp1_uno.setGeometry(QRect(150, 265, 70, 17))
        self.stapel = QLabel(self.centralwidget)
        self.stapel.setObjectName(u"stapel")
        self.stapel.setGeometry(QRect(310, 90, 100, 150))
        self.stapel.setPixmap(QPixmap(u"sprites/placeholder.png"))
        self.sp2_uno = QCheckBox(self.centralwidget)
        self.sp2_uno.setObjectName(u"sp2_uno")
        self.sp2_uno.setGeometry(QRect(670, 265, 70, 17))
        self.sp2_kartenslider = QSlider(self.centralwidget)
        self.sp2_kartenslider.setObjectName(u"sp2_kartenslider")
        self.sp2_kartenslider.setGeometry(QRect(680, 90, 21, 150))
        self.sp2_kartenslider.setOrientation(Qt.Vertical)
        self.sp2_karte = QLabel(self.centralwidget)
        self.sp2_karte.setObjectName(u"sp2_karte")
        self.sp2_karte.setGeometry(QRect(560, 90, 100, 150))
        self.sp2_karte.setPixmap(QPixmap(u"sprites/placeholder.png"))
        self.sp2_legen = QPushButton(self.centralwidget)
        self.sp2_legen.setObjectName(u"sp2_legen")
        self.sp2_legen.setGeometry(QRect(560, 260, 100, 25))
        self.sp2_label = QLabel(self.centralwidget)
        self.sp2_label.setObjectName(u"sp2_label")
        self.sp2_label.setGeometry(QRect(610, 40, 41, 31))
        self.sp2_label.setSizeIncrement(QSize(0, 0))
        self.neues_spiel_button = QPushButton(self.centralwidget)
        self.neues_spiel_button.setObjectName(u"neues_spiel_button")
        self.neues_spiel_button.setGeometry(QRect(310, 260, 100, 25))
        self.informationen = QLabel(self.centralwidget)
        self.informationen.setObjectName(u"informationen")
        self.informationen.setEnabled(True)
        self.informationen.setGeometry(QRect(310, 40, 100, 16))
        self.informationen.setAlignment(Qt.AlignCenter)
        self.sp1_anzahl_karten = QLabel(self.centralwidget)
        self.sp1_anzahl_karten.setObjectName(u"sp1_anzahl_karten")
        self.sp1_anzahl_karten.setGeometry(QRect(40, 300, 111, 16))
        self.sp2_anzahl_karten = QLabel(self.centralwidget)
        self.sp2_anzahl_karten.setObjectName(u"sp2_anzahl_karten")
        self.sp2_anzahl_karten.setGeometry(QRect(560, 300, 121, 16))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setAutoFillBackground(False)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.sp1_label.setText(QCoreApplication.translate("MainWindow", u"Spieler1", None))
        self.sp1_karte.setText("")
        self.sp1_legen.setText(QCoreApplication.translate("MainWindow", u"Karte legen", None))
        self.sp1_uno.setText(QCoreApplication.translate("MainWindow", u"UNO", None))
        self.stapel.setText("")
        self.sp2_uno.setText(QCoreApplication.translate("MainWindow", u"UNO", None))
        self.sp2_karte.setText("")
        self.sp2_legen.setText(QCoreApplication.translate("MainWindow", u"Karte legen", None))
        self.sp2_label.setText(QCoreApplication.translate("MainWindow", u"Spieler2", None))
        self.neues_spiel_button.setText(QCoreApplication.translate("MainWindow", u"Neues Spiel", None))
        self.informationen.setText(QCoreApplication.translate("MainWindow", u"Informationen", None))
        self.sp1_anzahl_karten.setText(QCoreApplication.translate("MainWindow", u"Kartenanzahl:", None))
        self.sp2_anzahl_karten.setText(QCoreApplication.translate("MainWindow", u"Kartenanzahl:", None))
#if QT_CONFIG(accessibility)
        self.statusbar.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
    # retranslateUi

