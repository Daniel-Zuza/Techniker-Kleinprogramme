
from Thema import Thema
from parameter import *
from Kalenderverwalter import Kalenderverwalter


themen = [
    Thema('WSK/1', WIEDERHOLUNGSVARITATIONEN['Langzeiterinnerung'], '1', 0.5, ersttermin_offset=6),
    Thema('WSK/2', WIEDERHOLUNGSVARITATIONEN['Langzeiterinnerung'], '1', 0.5, ersttermin_offset=6),
    Thema('WSK/3', WIEDERHOLUNGSVARITATIONEN['Langzeiterinnerung'], '1', 1, ersttermin_offset=7),
    Thema('WSK/4', WIEDERHOLUNGSVARITATIONEN['Langzeiterinnerung'], '1', 1, ersttermin_offset=7),

    Thema('M4/1 - Basis', WIEDERHOLUNGSVARITATIONEN['Basiseinpraegung'], '1', 0.25, ersttermin_offset=1),
    Thema('M4/3 - Basis', WIEDERHOLUNGSVARITATIONEN['Basiseinpraegung'], '1', 0.25, ersttermin_offset=1),
    Thema('M5/1 - Basis', WIEDERHOLUNGSVARITATIONEN['Basiseinpraegung'], '1', 0.25, ersttermin_offset=8),
    Thema('M5/3 - Basis', WIEDERHOLUNGSVARITATIONEN['Basiseinpraegung'], '1', 0.25, ersttermin_offset=8),

    Thema('M4/1', WIEDERHOLUNGSVARITATIONEN['Aufbaueinpraegung'], '1', 0.5, ersttermin_offset=1),
    Thema('M4/2', WIEDERHOLUNGSVARITATIONEN['Aufbaueinpraegung'], '1', 0.5, ersttermin_offset=1),
    Thema('M4/3', WIEDERHOLUNGSVARITATIONEN['Aufbaueinpraegung'], '1', 0.5, ersttermin_offset=1),
    Thema('M5/1', WIEDERHOLUNGSVARITATIONEN['Aufbaueinpraegung'], '1', 0.5, ersttermin_offset=8),
    Thema('M5/2', WIEDERHOLUNGSVARITATIONEN['Aufbaueinpraegung'], '1', 0.5, ersttermin_offset=8),
    Thema('M5/3', WIEDERHOLUNGSVARITATIONEN['Aufbaueinpraegung'], '1', 0.5, ersttermin_offset=8),

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
