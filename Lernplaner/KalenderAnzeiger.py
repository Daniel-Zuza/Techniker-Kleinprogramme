

def differenzverhaeltnisseAnzeigen(soll_differenzen, ist_differenzen, toleranz=0.1):
    print('Differenzverhältnisse:')
    for termin_name in ist_differenzen:
        ist_diff = ist_differenzen[termin_name]
        soll_diff = soll_differenzen[termin_name.split(" - ")[1]]

        if (ist_diff - soll_diff) / soll_diff > toleranz:
            flag = '----'
        else:
            flag = '    '

        print(f'{flag} {termin_name}, soll: {soll_differenzen[termin_name.split(" - ")[1]]}, ist: {ist_differenzen[termin_name]}')
    print()

class KalenderTag():
    def __init__(self, datum):
        self.datum = datum
        self.tag_string = f'{self.datum}'

    def eventHinzufuegen(self, zeit, event_name, wiederholungsplan):
        self.tag_string += f'\n{zeit}: {event_name}'

    def anzeigen(self):
        print(self.tag_string)
        print()