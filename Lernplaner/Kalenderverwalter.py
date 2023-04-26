
import os
import datetime as dt
from datetime import timedelta
import pandas as pd
from ics import Calendar, Event

from parameter import LERNEINHEIT_WIEDERHOLUNGSPLAN

class Kalenderverwalter():
    def __init__(self, zeitkapatzitaeten):
        self.kalender_neu = Calendar()
        self.zeitkapatzitaeten = zeitkapatzitaeten

        if os.path.exists("kalender.ics"):
            kalender_alt = Calendar(open('kalender.ics', 'r').read())
            if os.path.exists("kalender_backup.ics"): os.remove('kalender_backup.ics')
            with open('kalender_backup.ics', 'w') as my_file:
                my_file.writelines(kalender_alt.serialize_iter())
            self.plan = self.planErhalten(kalender_alt)
            self.alle_termine = self.alleTermineErhalten(kalender_alt)

    def planErhalten(self, kalender_alt):
        return [
            {
                'name': e.name,
                'begin': pd.to_datetime(str(e.begin)).tz_localize(None),
                'end': pd.to_datetime(str(e.end)).tz_localize(None)
            }
            for e in kalender_alt.events
            ]

    def alleTermineErhalten(self, kalender_alt):
        return [
            pd.to_datetime(str(e.begin)).tz_localize(None)
            for e in kalender_alt.events
        ]

    def freieTermineErhalten(self):
        ersttermin = min([e['begin'] for e in self.plan if e['begin'] > dt.datetime.now()])
        letzttermin = max([e['begin'] for e in self.plan if e['begin'] > dt.datetime.now()])

        return [ersttermin + timedelta(tages_plus)
                         for tages_plus in range((letzttermin - ersttermin).days)
                         if not ersttermin + timedelta(tages_plus) in self.alle_termine]

    def neueLerneinheitenErrechnen(self, freie_termine, lerneinheit_wiederholungsplan):
        pass

    def lerneinheitenEinplanen(self, thema, bisheriger_lernplan):
        freie_termine = self.freieTermineErhalten(thema)
        thema_lerneinheiten = self.neueLerneinheitenErrechnen(freie_termine, LERNEINHEIT_WIEDERHOLUNGSPLAN)
        # lerneinheiten für neues thema einplanen basierend auf freien plätzen




