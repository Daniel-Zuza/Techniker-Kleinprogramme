
import datetime as dt

ZEITKAPATZITAETEN = {
    0: 1,
    1: 1,
    2: 1,
    3: 1,
    4: 2,
    5: 6,
    6: 6,
}

LERNEINHEIT_WIEDERHOLUNGSPLAN = {
    '1': 1,
    '2': 1,
    '3': 2,
    '4': 2,
    '5': 3,
    '6': 3,
    '7': 4,
    '8': 4,
    '9': 7,
    '10': 7,
    '11': 15,
    '12': 15,
    '13': 15,
    '14': 15,
    '15': 15,
}

class Thema():
    def __init__(self, themenname, aktuelle_lerneinheit='1', prioritaet=False, lerneinheit_zeitaufwand=0.5, erfassungsdatum=None):
        self.name = themenname
        self.aktuelle_lerneinheit = aktuelle_lerneinheit
        self.prioritaet = prioritaet
        self.lerneinheit_zeitaufwand = lerneinheit_zeitaufwand
        self.erfassungsdatum = erfassungsdatum

