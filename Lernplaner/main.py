
from Thema import Thema
from parameter import *
from Kalenderverwalter import Kalenderverwalter

LERNEINHEIT_WIEDERHOLUNGSPLAN = LERNEINHEITS_WIEDERHOLUNGSVARITATIONEN[2]

themen = [
    Thema('M5/1 - Basis', LERNEINHEIT_WIEDERHOLUNGSPLAN, '1', 0.25, ersttermin_offset=9),
    Thema('M5/3 - Basis', LERNEINHEIT_WIEDERHOLUNGSPLAN, '1', 0.25, ersttermin_offset=9),
]

for thema in themen:
    kalenderverwalter = Kalenderverwalter(thema, ZEITKAPATZITAETEN)
    kalenderverwalter.lerneinheitenEinplanen()
    kalenderverwalter.neuenKalenderSpeichern()








# Kalender anzeigen für Debugging
# import os
# import datetime as dt
# from ics import Calendar, Event
#
#
# plan = kalenderverwalter.planErhalten(kalenderverwalter.kalender_neu)
# # alle_termine = self.alleTermineErhalten(kalender_alt)
# # tageskapatzitaeten = tageskapatzitaetenErhalten()
#
# print('Plan:')
#
# def sortierung(event):
#     return event['begin']
#
# events = []
# for e in plan:
#     events.append(e)
#
# for t in sorted(plan, key=sortierung):
#     print(t['begin'])
#     print(t['name'])
#     print()
# print()
