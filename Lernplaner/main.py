
from Thema import Thema
from parameter import *
from Kalenderverwalter import Kalenderverwalter

LERNEINHEIT_WIEDERHOLUNGSPLAN = LERNEINHEITS_WIEDERHOLUNGSVARITATIONEN[1]

# themen = [
#     Thema('WSK/3/1', LERNEINHEIT_WIEDERHOLUNGSPLAN, '3', 0.5),
#     Thema('WSK/3/2 und 4', LERNEINHEIT_WIEDERHOLUNGSPLAN, '3', 0.5),
#     Thema('WSK/3/3', LERNEINHEIT_WIEDERHOLUNGSPLAN, '3', 0.5),
#     Thema('WSK/2', LERNEINHEIT_WIEDERHOLUNGSPLAN, '7', 0.5),
#     Thema('WSK/1', LERNEINHEIT_WIEDERHOLUNGSPLAN, '7', 0.5),
# ]

themen = [
    Thema('D/2', LERNEINHEIT_WIEDERHOLUNGSPLAN, '1', 1, ersttermin_offset=0),
]

for thema in themen:
    kalenderverwalter = Kalenderverwalter(thema, ZEITKAPATZITAETEN)
    kalenderverwalter.lerneinheitenEinplanen()
    kalenderverwalter.neuenKalenderSpeichern()
