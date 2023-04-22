
import datetime as dt

ZEITKAPATZITAETEN = {
    'Mo': 1,
    'Di': 1,
    'Mi': 1,
    'Do': 1,
    'Fr': 2,
    'Sa': 6,
    'So': 6,
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
    '11': 10,
    '12': 14,
    '13': 21,
    '14': 31,
    '15': 45,
}

class Thema():
    def __init__(self, themenname, aktuelle_lerneinheit='1', prioritaet=False, lerneinheit_zeietaufwand=0.5, erfassungsdatum=None):
        self.themenname = themenname
        self.aktuelle_lerneinheit = aktuelle_lerneinheit
        self.prioritaet = prioritaet
        self.lerneinheit_zeietaufwand = lerneinheit_zeietaufwand
        self.erfassungsdatum = erfassungsdatum

