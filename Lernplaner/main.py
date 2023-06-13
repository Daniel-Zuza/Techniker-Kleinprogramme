
from Thema import Thema
from parameter import *
from Kalenderverwalter import Kalenderverwalter

startkalender = 'kalender.ics'
#startkalender = 'start_kalender.ics'

themen = [
    Thema('M6/1', WIEDERHOLUNGSVARITATIONEN['Neuerfassung'], '1', 0.5, ersttermin_offset=0),
    Thema('M6/2', WIEDERHOLUNGSVARITATIONEN['Neuerfassung'], '1', 0.5, ersttermin_offset=0),

    Thema('M4/1', WIEDERHOLUNGSVARITATIONEN['Neuerfassung'], '5', 0.5, ersttermin_offset=0),
    Thema('M4/2', WIEDERHOLUNGSVARITATIONEN['Neuerfassung'], '4', 0.5, ersttermin_offset=0),
    Thema('M4/3', WIEDERHOLUNGSVARITATIONEN['Neuerfassung'], '4', 0.5, ersttermin_offset=0),

    Thema('M5/1', WIEDERHOLUNGSVARITATIONEN['Neuerfassung'], '3', 0.5, ersttermin_offset=0),
    Thema('M5/2', WIEDERHOLUNGSVARITATIONEN['Neuerfassung'], '2', 0.5, ersttermin_offset=0),
    Thema('M5/3', WIEDERHOLUNGSVARITATIONEN['Neuerfassung'], '2', 0.5, ersttermin_offset=0),

    Thema('WSK1', WIEDERHOLUNGSVARITATIONEN['Langzeiterinnerung'], '3', 0.5, ersttermin_offset=0),
    Thema('WSK2', WIEDERHOLUNGSVARITATIONEN['Langzeiterinnerung'], '3', 0.5, ersttermin_offset=0),
    Thema('WSK3', WIEDERHOLUNGSVARITATIONEN['Langzeiterinnerung'], '2', 0.5, ersttermin_offset=0),
    Thema('WSK4', WIEDERHOLUNGSVARITATIONEN['Langzeiterinnerung'], '2', 0.5, ersttermin_offset=0),

    Thema('D3', WIEDERHOLUNGSVARITATIONEN['Wochennah'], '7', 0.25, ersttermin_offset=0),
]

for thema in themen:
    kalenderverwalter = Kalenderverwalter(startkalender, thema, ZEITKAPATZITAETEN)
    kalenderverwalter.lerneinheitenEinplanen()
    kalenderverwalter.neuenKalenderSpeichern()

    if thema == themen[-1]:
        kalenderverwalter.kalenderInfosAnzeigen(kalender=kalenderverwalter.kalender_neu)
    else:
        kalenderverwalter.differenzverhaeltnisseAnzeigen(kalender=kalenderverwalter.kalender_neu)





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
