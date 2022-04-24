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
        farbmöglichkeiten = ["rot", "grün", "blau", "gelb"] #"schwarz" wegen fehlender Implementation für Farbauswahl erst einmal deaktiviert
        farbe = choices(farbmöglichkeiten, weights=[13,13,13,13], k=1)[0]
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
        
    def karte_überprüfen(self, karte:Karte, verlängern:bool = False) -> bool:
        """Überprüft, ob eine Karte auf den Stapel gelegt werden kann oder ggf. ob sie eine Strafkarte verlängert"""
        if verlängern == False:
            return(karte.farbe == 'schwarz' or karte.farbe == self.farbe or karte.zahl == self.zahl)
        else:
            return (karte.zahl == self.zahl or karte.zahl == 14)
        
    def zug_möglich(self, spieler:Spieler, verlängern:bool = False) -> bool:
        """Überprüft, ob ein Spieler eine Karte besitzt, die er legen kann oder ggf. eine, mit der er eine Strafkarte verlängern kann"""
        möglich = False
        for karte in spieler.karten:
            if self.karte_überprüfen(karte, verlängern):
                möglich = True
                break
        return möglich
    
    def farbe_wünschen(self) -> str:
        #todo
        pass
    
    def karte_legen(self, spieler:Spieler, karte:Karte):
        """Wenn eine Karte gültig ist, wird die Karte aus der Hand des Spielers genommen und auf den Stapel gelegt.
        Außerdem werden die aus dem Zug resultierenden Strafkarten verteilt und es wird auf UNO/Gewinn überprüft"""
        #Kann die Karte ohne Weiteres auf den Stapel gelegt werden?
        if (self.strafkarten == 0 and self.karte_überprüfen(karte)) or (self.strafkarten != 0 and self.karte_überprüfen(karte,True)):
            spieler.karten.pop(spieler.karten.index(karte))
            
            #Kartenaktionen
            if karte.zahl == 13: #Farbe wünschen
                self.farbe = self.farbe_wünschen()
                self.aktueller_spieler_index += 1
            elif karte.zahl == 14: #+4 und Farbe wünschen
                self.farbe = self.farbe_wünschen()
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
            
            #Verteilt Strafkarten für den nächsten Spieler, wenn er sie nicht verlängern kann
            if self.strafkarten != 0 and not self.zug_möglich(self.aktueller_spieler,True):
                self.strafkarten_verteilen(self.strafkarten, self.aktueller_spieler)
            
            #Verteilt Strafkarten für den nächsten Spieler, wenn er nicht legen kann
            while not self.zug_möglich(self.aktueller_spieler):
                self.strafkarten_verteilen(1, self.aktueller_spieler)
    
    def neue_runde(self):
        """Erstellt die Spielumgebung für eine neue Runde"""
        self.gewinn = False
        
        for spieler in self.spieler_liste:
            spieler.karten.clear()
            self.strafkarten_verteilen(7, spieler)
            
        erste_karte = self.karte_erstellen()
        self.farbe = erste_karte.farbe
        self.zahl = erste_karte.zahl
        self.aktueller_spieler_index = randint(0,len(self.spieler_liste)-1)
        
        #Falls der erste Spieler nicht legen kann
        while not self.zug_möglich(self.aktueller_spieler):
                self.strafkarten_verteilen(1, self.aktueller_spieler)