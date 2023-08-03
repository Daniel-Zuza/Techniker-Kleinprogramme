
import os
import datetime as dt
from datetime import timedelta
import pandas as pd
from ics import Calendar, Event
from KalenderAnzeiger import KalenderTag, differenzverhaeltnisseAnzeigen

class Kalenderverwalter():
    def __init__(self, startkalender_name, thema, zeitkapatzitaeten, anzeigemodus=False):
        self.thema = thema
        self.kalender_neu = Calendar()
        self.zeitkapatzitaeten = zeitkapatzitaeten

        if anzeigemodus:
            if os.path.exists(startkalender_name):
                plan = self.planErhalten(Calendar(open(startkalender_name, 'r').read()))
                plan = self.tagessortiertenPlanErhalten(plan)
                self.kalenderTermineAnzeigen(plan)

            exit()

        if os.path.exists(startkalender_name):
            self.kalender_alt = Calendar(open(startkalender_name, 'r').read())
            self.kalender_neu = self.kalender_alt

            # backup erstellen
            # backup_name = str(dt.datetime.now()).replace(':', '%').replace('.', '%')
            # with open(f'Kalender-Backups/kalender_backup_{backup_name}.ics', 'w') as my_file:
            #    my_file.writelines(self.kalender_alt.serialize_iter())

            self.plan = self.planErhalten(self.kalender_alt)
            self.alle_termine = self.alleTermineErhalten(self.kalender_alt)
            self.tageskapatzitaeten = self.tageskapatzitaetenErhalten()

            # print('Plan:')
            # for t in self.plan:
            #     print(t)
            # print()
            #
            # print('Alle vorherigen Termine:')
            # for t in sorted(self.alle_termine):
            #     print(t)
            # print()
            #
            # print('Alle Tageskapatzitaeten:')
            # for t in self.tageskapatzitaeten:
            #     print(t, self.tageskapatzitaeten[t])
            # print()

        else:
            self.verwaltungsparaterAufStartwerteSetzen()

    def verwaltungsparaterAufStartwerteSetzen(self):
        self.ersttermin = dt.datetime.now().date() - timedelta(1)
        self.letzttermin = dt.datetime.now().date() - timedelta(1)
        self.alle_termine = []

        self.tageskapatzitaeten = {
            dt.datetime.now().date(): timedelta(hours=self.zeitkapatzitaeten[dt.datetime.now().weekday()])
        }

    def planErhalten(self, kalender_alt):
        return [
            {
                'name': e.name,
                'begin': pd.to_datetime(str(e.begin)).tz_localize(None),
                'end': pd.to_datetime(str(e.end)).tz_localize(None),
                'status': e.status
            }
            for e in kalender_alt.events
            ]

    def alleTermineErhalten(self, kalender_alt):
        self.ersttermin = min([e['begin'] for e in self.plan if e['begin'].date() >= dt.datetime.now().date()]).date()
        self.letzttermin = max([e['begin'] for e in self.plan if e['begin'].date() >= dt.datetime.now().date()]).date()


        return [
            (pd.to_datetime(str(e.begin)).tz_localize(None)).date()
            for e in kalender_alt.events
        ]

    def tageskapatzitaetenErhalten(self):
        tageskapatzitaeten = {}
        # print('self.letzttermin', self.letzttermin)
        # print('self.ersttermin', self.ersttermin)

        for tages_plus in range(0, (self.letzttermin - self.ersttermin).days + 1):
            datum = self.ersttermin + timedelta(tages_plus)
            tageskapatzitaeten[datum] = timedelta(hours=self.zeitkapatzitaeten[datum.weekday()])

        for event in self.plan:
            datum = event['begin'].date()
            if datum >= dt.datetime.now().date():
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

    def neueLerneinheitenErrechnen(self, freie_termine):
        self.lerneinheitstermine = []
        lerneinheiten = []
        for le in self.thema.wiederholungsplan:
            if int(le) < int(self.thema.aktuelle_lerneinheit): continue

            termin = self.lerneinheitsTerminErhalten(le, freie_termine)
            self.lerneinheitstermine.append(termin)

            lerneinheiten.append(
                Event(
                    name=f'{self.thema.name} - {le}',
                    begin=termin,
                    end=pd.to_datetime(termin) + timedelta(hours=self.thema.lerneinheit_zeitaufwand)
                )
            )

        return lerneinheiten

    def lerneinheitsTerminErhalten(self, lerneinheit, freie_termine):
        # print('lerneinheit, freie_termine', lerneinheit, freie_termine)

        if len(self.lerneinheitstermine) == 0:
            solltermin = freie_termine[0]
        else:
            voheriger_termin = self.lerneinheitstermine[-1]
            solltermin = voheriger_termin + timedelta(self.thema.wiederholungsplan[lerneinheit])

        offset_null = self.thema.ersttermin_offset == 0
        termin_platz = solltermin in freie_termine or solltermin > self.letzttermin
        termin_unverwendet = solltermin not in self.lerneinheitstermine

        if offset_null and termin_platz and termin_unverwendet:
            return solltermin

        else:
            if solltermin > self.letzttermin and solltermin not in self.lerneinheitstermine:
                return solltermin

            for freier_termin in freie_termine:
                if freier_termin >= dt.datetime.now().date() + timedelta(self.thema.ersttermin_offset):
                    termindifferenz = freier_termin - solltermin
                    voziehungstoleranz = timedelta(int(self.thema.wiederholungsplan[lerneinheit] / 3))

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

        lernheiten = self.neueLerneinheitenErrechnen(freie_termine)
        for event in lernheiten: self.kalender_neu.events.add(event)

    def vergangendeTermineWeglassen(self):
        vergangene_events = [e for e in self.kalender_neu.events if e.begin.date() < dt.datetime.now().date()]
        for event in vergangene_events:
            self.kalender_neu.events.remove(event)

    def neuenKalenderSpeichern(self):
        self.vergangendeTermineWeglassen()
        with open('kalender.ics', 'w') as my_file:
            my_file.writelines(self.kalender_neu.serialize_iter())

    def altenKalendeLoeschen(self):
        if os.path.exists("kalender.ics"): os.remove('kalender.ics')

    def kalenderInfosAnzeigen(self, kalender):
        plan = self.planErhalten(kalender)
        plan = self.tagessortiertenPlanErhalten(plan)

        self.kalenderTermineAnzeigen(plan)
        self.differenzverhaeltnisseAnzeigen(plan)

    def differenzverhaeltnisseAnzeigen(self, plan=None, kalender=None):
        if plan is None:
            plan = self.planErhalten(kalender)
            plan = self.tagessortiertenPlanErhalten(plan)

        differenzen = self.istLerneinheitsdifferenzenErhalten(plan)
        differenzverhaeltnisseAnzeigen(self.thema.wiederholungsplan, differenzen, toleranz=0.1)

    def kalenderTermineAnzeigen(self, plan):
        print('Kalendertermine:')
        for datum in plan:
            tag = KalenderTag(datum)

            for t in plan[datum]:
                tag.eventHinzufuegen(t['begin'], t['name'], self.thema.wiederholungsplan)

            tag.anzeigen()


    def istLerneinheitsdifferenzenErhalten(self, plan):
        differenzen = {}
        letzter_termin = None

        for datum in plan:
            for event in plan[datum]:
                if f'{self.thema.name} ' in event['name']:

                    if letzter_termin == None:
                        differenzen[event['name']] = int(self.thema.wiederholungsplan[self.thema.aktuelle_lerneinheit])
                        letzter_termin = datum

                    else:
                        differenzen[event['name']] = (datum - letzter_termin).days
                        letzter_termin = datum

        return differenzen

    def tagessortiertenPlanErhalten(self, plan):
        neuer_plan = {}

        for event in plan:

            if not event['begin'] in neuer_plan:
                neuer_plan[event['begin']] = [event]
            else:
                neuer_plan[event['begin']].append(event)

        return dict(sorted(neuer_plan.items()))


