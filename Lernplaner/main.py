
from Thema import Thema
from parameter import *
from Kalenderverwalter import Kalenderverwalter

LERNEINHEIT_WIEDERHOLUNGSPLAN = LERNEINHEITS_WIEDERHOLUNGSVARITATIONEN[0]

# themen = [
#     Thema('WSK/3/1', LERNEINHEIT_WIEDERHOLUNGSPLAN, '3', 0.5),
#     Thema('WSK/3/2 und 4', LERNEINHEIT_WIEDERHOLUNGSPLAN, '3', 0.5),
#     Thema('WSK/3/3', LERNEINHEIT_WIEDERHOLUNGSPLAN, '3', 0.5),
#     Thema('WSK/2', LERNEINHEIT_WIEDERHOLUNGSPLAN, '7', 0.5),
#     Thema('WSK/1', LERNEINHEIT_WIEDERHOLUNGSPLAN, '7', 0.5),
# ]

themen = [
    Thema('WSK/4/2', LERNEINHEIT_WIEDERHOLUNGSPLAN, '4', 0.5, ersttermin_offset=0),
    Thema('WSK/4/3', LERNEINHEIT_WIEDERHOLUNGSPLAN, '1', 0.5, ersttermin_offset=2),
    Thema('WSK/4/5', LERNEINHEIT_WIEDERHOLUNGSPLAN, '1', 0.5, ersttermin_offset=4),
    Thema('WSK/4/6', LERNEINHEIT_WIEDERHOLUNGSPLAN, '1', 0.5, ersttermin_offset=6),
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
