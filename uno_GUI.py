"""2-Spieler GUI für UNO"""

from msilib.schema import Dialog
import sys
from tkinter import N, Button
from unicodedata import name
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton
from PySide6.QtGui import QPixmap
from uno import *
from ui.ui_uno import Ui_MainWindow

class UnoWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        """Erzeugt die Startumgebung"""
        #Ui einstellen
        super().__init__()
        self.setupUi(self)
        self.informationen.hide()
        
        #Startumgebung erstellen
        self.spielleitung = Spielleitung()
        self.spielleitung.spieler_hinzufügen(Spieler())
        self.spielleitung.spieler_hinzufügen(Spieler())
        self.spielleitung.neue_runde()
        self.update_display()
        
        #Buttonaktionen
        self.neues_spiel_button.clicked.connect(self.neue_runde)
        self.sp1_uno.stateChanged.connect(self.spielleitung.spieler_liste[0].uno_sagen)
        self.sp2_uno.stateChanged.connect(self.spielleitung.spieler_liste[1].uno_sagen)
        self.sp1_kartenslider.valueChanged.connect(self.update_display)
        self.sp2_kartenslider.valueChanged.connect(self.update_display)
        self.sp1_legen.clicked.connect(self.legen_ausführen)
        self.sp2_legen.clicked.connect(self.legen_ausführen)
        
    def update_display(self):
        """Aktualisiert alle angezeigten Informationen"""
        sp1 = self.spielleitung.spieler_liste[0]
        sp2 = self.spielleitung.spieler_liste[1]
        if self.spielleitung.gewinn == True:
            self.informationen.setText('Gewonnen')
            self.informationen.show()
        else:
            self.informationen.hide()
            self.sp1_anzahl_karten.setText('Anzahl Karten: %d'%len(sp1.karten))
            self.sp2_anzahl_karten.setText('Anzahl Karten: %d'%len(sp2.karten))
            self.sp1_kartenslider.setMaximum(len(sp1.karten)-1)
            self.sp2_kartenslider.setMaximum(len(sp2.karten)-1)
            self.sp1_karte.setPixmap(QPixmap(self.datei_finden(sp1.karten[self.sp1_kartenslider.value()])))
            self.sp2_karte.setPixmap(QPixmap(self.datei_finden(sp2.karten[self.sp2_kartenslider.value()])))
            self.stapel.setPixmap(QPixmap(self.datei_finden(Karte(self.spielleitung.farbe, self.spielleitung.zahl))))
            if self.spielleitung.aktueller_spieler_index == 0:
                self.sp1_legen.setEnabled(True)
                self.sp2_legen.setEnabled(False)
            else:
                self.sp1_legen.setEnabled(False)
                self.sp2_legen.setEnabled(True)
        
    def neue_runde(self):
        """Erstellt eine neue Runde"""
        self.spielleitung.neue_runde()
        self.update_display()

    def legen_ausführen(self):
        """Führt einen Zug mit der aktuell ausgewählten Karte aus"""
        if self.spielleitung.aktueller_spieler == self.spielleitung.spieler_liste[0]:
            k = self.spielleitung.aktueller_spieler.karten[self.sp1_kartenslider.value()]
        else:
            k = self.spielleitung.aktueller_spieler.karten[self.sp2_kartenslider.value()]
        
        if self.spielleitung.karte_überprüfen(k):
            f = self.spielleitung.karte_legen(self.spielleitung.aktueller_spieler, k)
            if not self.spielleitung.gewinn:
                if f:
                    self.farbauswahl()
                self.spielleitung.karten_ziehen()
                if self.sp1_uno.isChecked() and self.spielleitung.spieler_liste[0].uno == False:
                    self.sp1_uno.toggle()
                elif self.sp2_uno.isChecked() and self.spielleitung.spieler_liste[1].uno == False:
                    self.sp2_uno.toggle()
            self.update_display()
    
    def farbauswahl(self):
        """Erzeugt einen Dialog zur Farbauswahl"""
        Dialog = QMessageBox()
        Dialog.setText("Welche Farbe möchtest Du wählen?")
        btn_rot = QPushButton("rot")
        btn_grün = QPushButton("grün")
        btn_blau = QPushButton("blau")
        btn_gelb = QPushButton("gelb")
        Dialog.addButton(btn_rot, QMessageBox.AcceptRole)
        Dialog.addButton(btn_grün, QMessageBox.AcceptRole)
        Dialog.addButton(btn_blau, QMessageBox.AcceptRole)
        Dialog.addButton(btn_gelb, QMessageBox.AcceptRole)
        Dialog.buttonClicked.connect(self.farbe_festlegen)
        Dialog.exec()

    def farbe_festlegen(self, button):
        """Legt die Farbe der Spielleitung auf die des gedrückten Buttons fest"""
        self.spielleitung.farbe = button.text()
        
    def datei_finden(self, k:Karte) -> str:
        """Gibt den Dateipfad für die Bilddatei einer Karte an"""
        return 'karten/%s_%d.png'%(k.farbe, k.zahl)        
        
app = QApplication(sys.argv)
window = UnoWindow()
window.show()
app.exec()