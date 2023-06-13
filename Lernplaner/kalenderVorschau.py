
import os
import random
import datetime
from ics import Calendar, Event
from KalenderAnzeiger import *

from Thema import Thema
from parameter import *
from Kalenderverwalter import Kalenderverwalter

def kalenderAnzeigen(kalender):
    thema = Thema('', WIEDERHOLUNGSVARITATIONEN['Neuerfassung'], '1', 0.5, ersttermin_offset=0)
    Kalenderverwalter(kalender, thema, '', True)

kalenderAnzeigen('kalender.ics')
#kalenderAnzeigen('start_kalender.ics')


