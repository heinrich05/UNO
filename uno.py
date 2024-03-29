"""Das Kartenspiel UNO für Python"""

from random import choices, randint

class Karte:
    def __init__(self, farbe:str, zahl:int):
        self.farbe = farbe
        self.zahl = zahl

class Spieler:
    def __init__(self):
        self.karten = list()
        self.uno = False
        
    def karte_annehmen(self, k: Karte):
        """Nimmt eine Karte auf"""
        self.karten.append(k)
        
    def uno_sagen(self):
        """Ändert den UNO-Status für den Spieler"""
        self.uno = not self.uno
    
class Spielleitung:
    def __init__(self):
        self.spieler_liste = list()
        self._aktueller_spieler_index = None
        self._aktueller_spieler = None
        self.farbe = None
        self.zahl = None
        self.strafkarten = 0
        self.gewinn = False
        
    @property
    def aktueller_spieler_index(self) -> int:
        return self._aktueller_spieler_index
    
    @aktueller_spieler_index.setter
    def aktueller_spieler_index(self, aktueller_spieler:int):
        self._aktueller_spieler_index = aktueller_spieler % len(self.spieler_liste)
    
    @property
    def aktueller_spieler(self) -> Spieler:
        return self.spieler_liste[self.aktueller_spieler_index]
    
    @aktueller_spieler.setter
    def aktueller_spieler(self, wert):
        pass
        
    def karte_erstellen(self) -> Karte:
        """Erstellt eine Karte"""
        farbmöglichkeiten = ["rot", "grün", "blau", "gelb", "schwarz"]
        farbe = choices(farbmöglichkeiten, weights=[13,13,13,13,2], k=1)[0]
        if farbe == 'schwarz':
            zahl = randint(13,14)
            karte = Karte(farbe, zahl)
        else:
            zahl = randint(0,12)
            karte = Karte(farbe, zahl)
        return karte
    
    def spieler_hinzufügen(self, spieler:Spieler):
        """Fügt einen Spieler hinzu"""
        self.spieler_liste.append(spieler)
        
    def strafkarten_verteilen(self, anzahl:int, spieler:Spieler):
        """Verteilt eine Menge an Karten an einen bestimmten Spieler"""
        for i in range(anzahl):
            karte = self.karte_erstellen()
            spieler.karte_annehmen(karte)
        self.strafkarten = 0
        spieler.uno = False
        
    def karte_überprüfen(self, karte:Karte) -> bool:
        """Überprüft, ob eine Karte auf den Stapel gelegt werden kann"""
        if self.strafkarten == 0:
            return(karte.farbe == 'schwarz' or karte.farbe == self.farbe or karte.zahl == self.zahl)
        else:
            return(karte.zahl == self.zahl or karte.zahl == 1)
        
    def zug_möglich(self, spieler:Spieler) -> bool:
        """Überprüft, ob ein Spieler eine Karte besitzt, die er legen kann"""
        möglich = False
        for karte in spieler.karten:
            if self.karte_überprüfen(karte):
                möglich = True
                break
        return möglich

    def verlängern_möglich(self, spieler:Spieler) -> bool:
        """Überprüft, ob ein Spieler eine Karte besitzt, die eine Strafkarte verlängert"""
        möglich = False
        for karte in spieler.karten:
            if karte.zahl == self.zahl or karte.zahl == 14:
                möglich = True
                break
        return möglich

    def karte_legen(self, spieler:Spieler, karte:Karte) -> bool:
        """Legt eine Karte auf den Stapel, führt die Aktionen, die auf das Legen einer Karte folgen, aus und gibt zurück, ob sich eine Farbe gewünscht werden muss"""
        spieler.karten.pop(spieler.karten.index(karte))
        farbe_wünschen = False
        
        if karte.zahl == 13: #Farbe wünschen
            farbe_wünschen = True
            self.aktueller_spieler_index += 1
        elif karte.zahl == 14: #+4 und Farbe wünschen
            farbe_wünschen = True
            self.strafkarten += 4
            self.aktueller_spieler_index += 1
        else:
            if karte.zahl == 10: #Aussetzen
                self.aktueller_spieler_index += 2
            elif karte.zahl == 11: #Richtungswechsel
                self.aktueller_spieler_index -= 1
            else:    
                if karte.zahl == 12: #+2
                    self.strafkarten += 2
                self.aktueller_spieler_index += 1
            self.farbe = karte.farbe
        self.zahl = karte.zahl

        #Auf UNO überprüfen
        if (len(spieler.karten) == 1 and spieler.uno == False) or (len(spieler.karten) > 1 and spieler.uno == True):
            self.strafkarten_verteilen(2, spieler)
        
        #Auf Gewinn überprüfen
        elif len(spieler.karten) == 0:
            self.gewinn = True

        return farbe_wünschen
    
    def karten_ziehen(self):
        """Wenn der aktuelle Spieler Karten ziehen muss, bekommt er diese, bis er wieder legen kann"""
        #Verteilt Strafkarten für den neuen Spieler, wenn er sie nicht verlängern kann
        if self.strafkarten != 0 and not self.verlängern_möglich(self.aktueller_spieler):
            self.strafkarten_verteilen(self.strafkarten, self.aktueller_spieler)
        
        #Verteilt Strafkarten für den neuen Spieler, wenn er nicht legen kann
        while not self.zug_möglich(self.aktueller_spieler):
            self.strafkarten_verteilen(1, self.aktueller_spieler)

    def neue_runde(self):
        """Erstellt die Spielumgebung für eine neue Runde"""
        self.gewinn = False
        self.farbe = "schwarz"
        
        for spieler in self.spieler_liste:
            spieler.karten.clear()
            self.strafkarten_verteilen(7, spieler)
            
        while self.farbe == "schwarz":
            erste_karte = self.karte_erstellen()
            self.farbe = erste_karte.farbe
            self.zahl = erste_karte.zahl
        self.aktueller_spieler_index = randint(0,len(self.spieler_liste)-1)
        
        #Falls der erste Spieler nicht legen kann
        while not self.zug_möglich(self.aktueller_spieler):
                self.strafkarten_verteilen(1, self.aktueller_spieler)