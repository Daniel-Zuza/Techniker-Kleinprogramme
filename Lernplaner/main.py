
from parameter import *
from Kalenderverwalter import Kalenderverwalter

kalenderverwalter = Kalenderverwalter(None)
freie_termine = kalenderverwalter.freieTermineErhalten()
print('freie_termine', freie_termine)

