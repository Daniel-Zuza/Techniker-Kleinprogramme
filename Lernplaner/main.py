
import os
from parameter import *
from Kalenderverwalter import Kalenderverwalter

from tests import testDatei

#os.remove('kalender.ics')
#os.remove('kalender_backup.ics')
#testDatei()


# themen = [
#     Thema('WSK/3/1', aktuelle_lerneinheit='3', lerneinheit_zeitaufwand=0.5),
#     Thema('WSK/3/2 und 4', aktuelle_lerneinheit='3', lerneinheit_zeitaufwand=0.5),
#     Thema('WSK/3/3', aktuelle_lerneinheit='3', lerneinheit_zeitaufwand=0.5),
#     Thema('WSK/2', aktuelle_lerneinheit='7', lerneinheit_zeitaufwand=0.5),
#     Thema('WSK/1', aktuelle_lerneinheit='7', lerneinheit_zeitaufwand=0.5),
# ]

themen = [
    Thema('D/2', aktuelle_lerneinheit='1', lerneinheit_zeitaufwand=1),
]

for thema in themen:
    kalenderverwalter = Kalenderverwalter(thema, ZEITKAPATZITAETEN)
    kalenderverwalter.lerneinheitenEinplanen()
    kalenderverwalter.neuenKalenderSpeichern()
