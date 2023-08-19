
import os

def gewichtetenThemenmittelwertErrechnen(themen_punkte, clippwert):
    # Gewichtungen errechnen basierend darauf wie aktuell eine Lernsession ist
    # und dann alte Lernsessions auf Durchschnittswerte setzen und laenge der Session je nach Gewichtung kürzen

    print('themen_punkte', themen_punkte)

    if len(themen_punkte) < 2:  # sicherstellen, dass mind. 2 Lernsession vorhanden sind um weiter zu machen

        return sum(themen_punkte[0]) / len(themen_punkte[0])

    sessionanzahl = len(themen_punkte)
    gewichtete_themenpunkte = []
    step = (1 - clippwert) / (sessionanzahl - 1)
    gewichtungen = [clippwert + step * i for i, gewicht in enumerate(themen_punkte)]

    for gewicht, punkte in zip(gewichtungen, themen_punkte):
        durchschnitt_sessionpunkte = sum(punkte) / len(punkte)
        punkte_gewichtungsgrenze = int(len(punkte) * gewicht)

        for i in range(punkte_gewichtungsgrenze):
            gewichtete_themenpunkte.append(durchschnitt_sessionpunkte)

    return sum(gewichtete_themenpunkte) / len(gewichtete_themenpunkte)

def Themenabschlussberechnungen():
    pass

def b():
    pass

def c():
    pass

def punkteErrechnen(clippwert):
    if os.path.exists('resultate.txt'):
        os.remove('resultate.txt')

    with open('punktzahlen.txt', 'r') as file:
        with open('resultate.txt', 'w') as resultate:

            session_punkte = []
            themen_punkte = []
            themen_mittelwerte = []
            themen_letztsession_mittelwerte = []
            themenbereich = ''
            lines = file.readlines()

            for i, line in enumerate(lines):

                if line is lines[-1]:
                    if len(session_punkte) != 0:
                        ref_session_punktzahl = sum(session_punkte) / len(session_punkte)
                        #print(f'Session Punktzahl: {ref_session_punktzahl}')
                        #resultate.write(f'Session Punktzahl: {ref_session_punktzahl}\n')
                        themen_punkte.append(session_punkte)

                        session_punkte = []

                        themenmittelwert = gewichtetenThemenmittelwertErrechnen(themen_punkte, clippwert)

                        themen_mittelwerte.append(themenmittelwert)
                        themen_letztsession_mittelwerte.append(ref_session_punktzahl)
                        print(f'Themen Punktzahl von {themenbereich}: {themenmittelwert}\n')
                        resultate.write(f'Themen Punktzahl von {themenbereich}: {themenmittelwert}\n')

                        themen_punkte = []

                    themenbereich = ' '.join(line.strip().split(' ')[1:])

                elif '/' in line:
                    print('line', line, i)
                    if themenbereich != '':
                        themenmittelwert = gewichtetenThemenmittelwertErrechnen(themen_punkte, clippwert)

                        themen_mittelwerte.append(themenmittelwert)
                        themen_letztsession_mittelwerte.append(ref_session_punktzahl)
                        print(f'Themen Punktzahl von {themenbereich}: {themenmittelwert}\n')
                        resultate.write(f'Themen Punktzahl von {themenbereich}: {themenmittelwert}\n')

                        themen_punkte = []

                    themenbereich = ' '.join(line.strip().split(' ')[1:])

                elif '#' in line:
                    print(i)
                    if len(session_punkte) != 0:
                        ref_session_punktzahl = sum(session_punkte) / len(session_punkte)
                        #print(f'Session Punktzahl: {ref_session_punktzahl}')
                        #resultate.write(f'Session Punktzahl: {ref_session_punktzahl}\n')
                        themen_punkte.append(session_punkte)

                        session_punkte = []

                else:
                    for punkt in line.strip().split(', '):
                        if not '-' in punkt:
                            session_punkte.append(int(punkt))



            if not len(themen_punkte) == 0:
                print(f'Themen Punktzahl von {themenbereich}: {gewichtetenThemenmittelwertErrechnen(themen_punkte, clippwert)}\n')
                resultate.write(f'Themen Punktzahl von {themenbereich}: {gewichtetenThemenmittelwertErrechnen(themen_punkte, clippwert)}\n')
            if not len(themen_mittelwerte) == 0:
                print(f'themenübergreifende Gesamte Punktzahl: {sum(themen_mittelwerte) / len(themen_mittelwerte)}')
                resultate.write(f'\nthemenübergreifende Gesamte Punktzahl: {sum(themen_mittelwerte) / len(themen_mittelwerte)}\n')
            if not len(themen_letztsession_mittelwerte) == 0:
                print(f'themenübergreifende Letztsession Punktzahl: {sum(themen_letztsession_mittelwerte) / len(themen_letztsession_mittelwerte)}')
                resultate.write(f'themenübergreifende Letztsession Punktzahl: {sum(themen_letztsession_mittelwerte) / len(themen_letztsession_mittelwerte)}\n')

                print('themen_letztsession_mittelwerte', themen_letztsession_mittelwerte)

# gewichtet
punkteErrechnen(clippwert=0.25)


# ungewichtet
#punkteErrechnen(clippwert=1)