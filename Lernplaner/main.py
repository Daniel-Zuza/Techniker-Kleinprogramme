
import os
from parameter import *
from Kalenderverwalter import Kalenderverwalter

from tests import testDatei

# os.remove('kalender.ics')
# os.remove('kalender_backup.ics')
# testDatei()

thema = Thema('C', lerneinheit_zeitaufwand=0.5)
kalenderverwalter = Kalenderverwalter(thema, ZEITKAPATZITAETEN)
kalenderverwalter.lerneinheitenEinplanen()
kalenderverwalter.neuenKalenderSpeichern()
