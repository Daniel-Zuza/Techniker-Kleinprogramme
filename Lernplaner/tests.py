
import os
import random
import datetime
from ics import Calendar, Event

def testDatei():
    if os.path.exists("kalender.ics"):
        kalender_alt = Calendar(open('kalender.ics', 'r').read())
        if os.path.exists("kalender.ics"): os.remove('kalender.ics')
        with open('kalender_backup.ics', 'w') as my_file: my_file.writelines(kalender_alt.serialize_iter())
    kalender_neu = Calendar()


    kalender_neu.events.add(
        Event(
            name="xxxxxxxxxxxxxxxxx",
            begin=datetime.datetime.now() + datetime.timedelta(1),
            end=datetime.datetime.now() + datetime.timedelta(1) + datetime.timedelta(hours=0.5)
        )
    )

    kalender_neu.events.add(
        Event(
            name="xxxxxxxxxxxxxxxxx",
            begin=datetime.datetime.now() + datetime.timedelta(4),
            end=datetime.datetime.now() + datetime.timedelta(4) + datetime.timedelta(hours=0.5)
        )
    )

    kalender_neu.events.add(
        Event(
            name="xxxxxxxxxxxxxxxxx",
            begin=datetime.datetime.now() + datetime.timedelta(3),
            end=datetime.datetime.now() + datetime.timedelta(3) + datetime.timedelta(hours=0.5)
        )
    )

    kalender_neu.events.add(
        Event(
            name="xxxxxxxxxxxxxxxxx",
            begin=datetime.datetime.now() + datetime.timedelta(5),
            end=datetime.datetime.now() + datetime.timedelta(5) + datetime.timedelta(hours=0.5)
        )
    )

    kalender_neu.events.add(
        Event(
            name="xxxxxxxxxxxxxxxxx",
            begin=datetime.datetime.now() + datetime.timedelta(7),
            end=datetime.datetime.now() + datetime.timedelta(7) + datetime.timedelta(hours=0.5)
        )
    )

    kalender_neu.events.add(
        Event(
            name="xxxxxxxxxxxxxxxxx",
            begin=datetime.datetime.now() + datetime.timedelta(10),
            end=datetime.datetime.now() + datetime.timedelta(10) + datetime.timedelta(hours=0.5)
        )
    )

    kalender_neu.events.add(
        Event(
            name="xxxxxxxxxxxxxxxxx",
            begin=datetime.datetime.now() + datetime.timedelta(15),
            end=datetime.datetime.now() + datetime.timedelta(15) + datetime.timedelta(hours=0.5)
        )
    )

    kalender_neu.events.add(
        Event(
            name="xxxxxxxxxxxxxxxxx",
            begin=datetime.datetime.now() + datetime.timedelta(17),
            end=datetime.datetime.now() + datetime.timedelta(17) + datetime.timedelta(hours=0.5)
        )
    )

    with open('kalender.ics', 'w') as my_file:
        my_file.writelines(kalender_neu.serialize_iter())

