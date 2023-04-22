
from parameter import LERNEINHEIT_WIEDERHOLUNGSPLAN

class Kalenderverwalter():
    def __init__(self, email, _pass, zeitkapatzitaeten):
        # bei Kalenderapp anmelden und client erstellen
        self.zeitkapatzitaeten = zeitkapatzitaeten
        pass

    def planErhalten(self):
        # bisherigen Lernplan erhalten
        self.plan = None
        pass

    def freieTermineErhalten(self, thema):
        # mögliche Zeiten für die Lerneinheiten finden
        pass

    def lerntermineEntfernen(self, themenname, lernplan):
        # lerneinheiten von Thema entfernen im Kalnder
        lernplan_neu = lernplan
        return lernplan_neu

    def neueLerneinheitenErrechnen(self, freie_termine, lerneinheit_wiederholungsplan):
        pass

    def lerneinheitenEinplanen(self, thema, bisheriger_lernplan):
        if thema.aktuelle_lerneinheit != '1':
            self.lerntermineEntfernen(thema.themenname, bisheriger_lernplan)

        freie_termine = self.freieTermineErhalten(thema)
        thema_lerneinheiten = self.neueLerneinheitenErrechnen(freie_termine, LERNEINHEIT_WIEDERHOLUNGSPLAN)
        # lerneinheiten für neues thema einplanen basierend auf freien plätzen




