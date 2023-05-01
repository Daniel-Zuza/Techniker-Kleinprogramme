
import os
import datetime as dt
from datetime import timedelta
import pandas as pd
from ics import Calendar, Event

from parameter import LERNEINHEIT_WIEDERHOLUNGSPLAN

class Kalenderverwalter():
    def __init__(self, thema, zeitkapatzitaeten):
        self.thema = thema
        self.kalender_neu = Calendar()
        self.zeitkapatzitaeten = zeitkapatzitaeten

        if os.path.exists("kalender.ics"):
            self.kalender_alt = Calendar(open('kalender.ics', 'r').read())
            self.kalender_neu = self.kalender_alt
            if os.path.exists("kalender.ics"): os.remove('kalender.ics')
            with open('kalender_backup.ics', 'w') as my_file:
                my_file.writelines(self.kalender_alt.serialize_iter())
            self.plan = self.planErhalten(self.kalender_alt)
            self.alle_termine = self.alleTermineErhalten(self.kalender_alt)
            self.tageskapatzitaeten = self.tageskapatzitaetenErhalten()

            # print('Alle vorherigen Termine:')
            # for t in sorted(self.alle_termine):
            #     print(t)
            # print()
            #
            # print('Alle Tageskapatzitaeten:')
            # for t in self.tageskapatzitaeten:
            #     print(t)
            # print()

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
        self.ersttermin = min([e['begin'] for e in self.plan if e['begin'] > dt.datetime.now()]).date()
        self.letzttermin = max([e['begin'] for e in self.plan if e['begin'] > dt.datetime.now()]).date()

        return [
            (pd.to_datetime(str(e.begin)).tz_localize(None)).date()
            for e in kalender_alt.events
        ]

    def tageskapatzitaetenErhalten(self):
        tageskapatzitaeten = {}
        for tages_plus in range((self.letzttermin - self.ersttermin).days + 1):
            datum = self.ersttermin + timedelta(tages_plus)
            tageskapatzitaeten[datum] = timedelta(hours=self.zeitkapatzitaeten[datum.weekday()])

        for event in self.plan:
            datum = event['begin'].date()
            zeitaufwand = event['end'] - event['begin']
            tageskapatzitaeten[datum] -= zeitaufwand

        return tageskapatzitaeten

    def tagesTermineAnzahlErhalten(self):
        termin_anzahlen = {}
        for datum in self.alle_termine:
            if not datum in termin_anzahlen: termin_anzahlen[datum] = 1
            else: termin_anzahlen[datum] += 1
        return termin_anzahlen

    def freieTermineErhalten(self):
        return [
            datum
            for datum in self.tageskapatzitaeten
            if self.tageskapatzitaeten[datum] - timedelta(hours=self.thema.lerneinheit_zeitaufwand) >= timedelta(0)
        ]

    def neueLerneinheitenErrechnen(self, freie_termine, lerneinheit_wiederholungsplan):
        self.lerneinheitstermine = []
        lerneinheiten = []
        for le in lerneinheit_wiederholungsplan:
            termin = self.lerneinheitsTerminErhalten(le, lerneinheit_wiederholungsplan, freie_termine)
            self.lerneinheitstermine.append(termin)

            lerneinheiten.append(
                Event(
                    name=f'{self.thema.name} - {le}',
                    begin=termin,
                    end=pd.to_datetime(termin) + timedelta(hours=self.thema.lerneinheit_zeitaufwand)
                )
            )

        return lerneinheiten

    def lerneinheitsTerminErhalten(self, lerneinheit, wiederhoungsplan, freie_termine):
        if len(self.lerneinheitstermine) == 0:
            solltermin = freie_termine[0]
        else:
            voheriger_termin = self.lerneinheitstermine[-1]
            solltermin = voheriger_termin + timedelta(wiederhoungsplan[lerneinheit])

        if (solltermin in freie_termine or solltermin > self.letzttermin) and solltermin not in self.lerneinheitstermine:
            return solltermin

        else:
            for freier_termin in freie_termine:
                termindifferenz = freier_termin - solltermin
                voziehungstoleranz = timedelta(int(wiederhoungsplan[lerneinheit] / 3))

                if termindifferenz > timedelta(0) or abs(termindifferenz) <= voziehungstoleranz:
                    moeglicher_termin = solltermin + (freier_termin - solltermin)

                    if not moeglicher_termin in self.lerneinheitstermine:
                        return moeglicher_termin

        exit('KEIN TERMIN GEFUNDEN -- ABBRUCH')

    def lerneinheitenEinplanen(self):
        freie_termine = self.freieTermineErhalten()
        if freie_termine == []: freie_termine = [self.letzttermin + timedelta(1)]

        # print('Freie Termine:')
        # for t in sorted(freie_termine):
        #     print(t)
        # print()

        lernheiten = self.neueLerneinheitenErrechnen(freie_termine, LERNEINHEIT_WIEDERHOLUNGSPLAN)
        for event in lernheiten: self.kalender_neu.events.add(event)

    def neuenKalenderSpeichern(self):
        with open('kalender.ics', 'w') as my_file:
            my_file.writelines(self.kalender_neu.serialize_iter())


