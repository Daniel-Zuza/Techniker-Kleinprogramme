
import os
import random
import datetime
from ics import Calendar, Event
from KalenderAnzeiger import *

kal = KalenderAnzeiger()

tag = KalenderTag(datetime.datetime.now().date())
tag.eventHinzufuegen('12:00', 'M1 1')
tag.eventHinzufuegen('13:00', 'Test 2')
tag.eventHinzufuegen('14:00', 'M1 3')
tag.eventHinzufuegen('15:00', 'Test 4')

print(tag.tag_string)



