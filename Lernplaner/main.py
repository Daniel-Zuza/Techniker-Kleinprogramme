
from Thema import Thema
from parameter import *
from Kalenderverwalter import Kalenderverwalter

startkalender = 'kalender.ics'

themen = [
    # Thema('M1', WIEDERHOLUNGSVARITATIONEN['Aufbaueinpraegung'], '1', 0.5, ersttermin_offset=1),
    #
    # Thema('M2', WIEDERHOLUNGSVARITATIONEN['kurzzeitintervall'], '1', 0.5, ersttermin_offset=1),
    #
    # Thema('M3', WIEDERHOLUNGSVARITATIONEN['Aufbaueinpraegung'], '1', 0.5, ersttermin_offset=1),
    #
    # Thema('M4/1', WIEDERHOLUNGSVARITATIONEN['Halb-Woechentlich'], '1', 0.5, ersttermin_offset=1),
    # Thema('M4/2', WIEDERHOLUNGSVARITATIONEN['Halb-Woechentlich'], '1', 0.5, ersttermin_offset=1),
    # Thema('M4/5', WIEDERHOLUNGSVARITATIONEN['Konzept-Neuerfassung'], '1', 0.5, ersttermin_offset=1),
    #
    # Thema('M5/1', WIEDERHOLUNGSVARITATIONEN['Konzept-Neuerfassung'], '1', 0.5, ersttermin_offset=1),
    # Thema('M5/2', WIEDERHOLUNGSVARITATIONEN['Wochennah'], '1', 0.5, ersttermin_offset=1),
    # Thema('M5/3', WIEDERHOLUNGSVARITATIONEN['Aufbaueinpraegung'], '1', 0.5, ersttermin_offset=1),
    #
    # Thema('M6/1', WIEDERHOLUNGSVARITATIONEN['Aufbaueinpraegung'], '1', 0.5, ersttermin_offset=1),
    # Thema('M6/2', WIEDERHOLUNGSVARITATIONEN['Aufbaueinpraegung'], '3', 0.5, ersttermin_offset=1),
    #
    # Thema('M7', WIEDERHOLUNGSVARITATIONEN['Aufbaueinpraegung'], '3', 0.5, ersttermin_offset=1),

    Thema('M8/1', WIEDERHOLUNGSVARITATIONEN['Auswendig-Neuerfassung'], '1', 0.5, ersttermin_offset=7),
    Thema('M8/2', WIEDERHOLUNGSVARITATIONEN['Auswendig-Neuerfassung'], '1', 0.75, ersttermin_offset=7),

    Thema('M9/1', WIEDERHOLUNGSVARITATIONEN['Auswendig-Neuerfassung'], '1', 0.5, ersttermin_offset=7),
    Thema('M9/2', WIEDERHOLUNGSVARITATIONEN['Auswendig-Neuerfassung'], '1', 0.5, ersttermin_offset=7)
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
