
def gewichtetenThemenmittelwertErrechnen(themen_punkte, clippwert):
    # Gewichtungen errechnen basierend darauf wie aktuell eine Lernsession ist
    # und dann alte Lernsessions auf Medianwerte setzen und laenge der Session je nach Gewichtung kürzen
    sessionanzahl = len(themen_punkte)
    gewichtete_themenpunkte = []
    step = (1 - clippwert) / (sessionanzahl -1)
    gewichtungen = [clippwert + step * i for i, gewicht in enumerate(themen_punkte)]

    for gewicht, punkte in zip(gewichtungen, themen_punkte):
        median_sessionpunkte = sum(punkte) / len(punkte)
        punkte_gewichtungsgrenze = int(len(punkte) * gewicht)

        for i in range(punkte_gewichtungsgrenze):
            gewichtete_themenpunkte.append(median_sessionpunkte)

    return sum(gewichtete_themenpunkte) / len(gewichtete_themenpunkte)

def punkteErrechnen(clippwert):
    with open('punktzahlen.txt', 'r') as file:
        session_punkte = []
        themen_punkte = []
        themen_mittelwerte = []
        themen_letztsession_mittelwerte = []
        themenbereich = ''


        for line in file:

            if '/' in line:
                if themenbereich != '':
                    themenmittelwert = gewichtetenThemenmittelwertErrechnen(themen_punkte, clippwert)

                    themen_mittelwerte.append(themenmittelwert)
                    themen_letztsession_mittelwerte.append(ref_session_punktzahl)
                    print(f'Themen Punktzahl von {themenbereich}: {themenmittelwert}\n')

                    themen_punkte = []

                themenbereich = ' '.join(line.strip().split(' ')[1:])

            elif '#' in line:
                if len(session_punkte) != 0:
                    ref_sessionlaenge = len(session_punkte)
                    ref_session_punktzahl = sum(session_punkte) / len(session_punkte)
                    print(f'Session Punktzahl: {ref_session_punktzahl}')
                    themen_punkte.append(session_punkte)
                    session_punkte = []

            else:
                for punkt in line.strip().split(', '):
                    if not '-' in punkt:
                        session_punkte.append(int(punkt))

    if not len(themen_punkte) == 0:
        print(f'Themen Punktzahl von {themenbereich}: {gewichtetenThemenmittelwertErrechnen(themen_punkte, clippwert)}\n')
    if not len(themen_mittelwerte) == 0:
        print(f'themenübergreifende Gesamte Punktzahl: {sum(themen_mittelwerte) / len(themen_mittelwerte)}')
    if not len(themen_letztsession_mittelwerte) == 0:
        print(f'themenübergreifende Letztsession Punktzahl: {sum(themen_letztsession_mittelwerte) / len(themen_letztsession_mittelwerte)}')

# gewichtet
punkteErrechnen(clippwert=0.25)

# ungewichtet
#punkteErrechnen(clippwert=1)