
from Thema import Thema
from parameter import *
from Kalenderverwalter import Kalenderverwalter

startkalender = 'kalender.ics'

themen = [
    Thema('M7', WIEDERHOLUNGSVARITATIONEN['Konzept-Neuerfassung'], '1', 0.5, ersttermin_offset=0),
]

for thema in themen:
    kalenderverwalter = Kalenderverwalter(startkalender, thema, ZEITKAPATZITAETEN)
    kalenderverwalter.lerneinheitenEinplanen()

    kalenderverwalter.altenKalendeLoeschen()
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
