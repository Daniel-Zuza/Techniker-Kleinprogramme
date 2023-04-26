
import os
from ics import Calendar, Event

if os.path.exists("kalender.ics"):
    kalender_alt = Calendar(open('kalender.ics', 'r').read())
    if os.path.exists("kalender_backup.ics"): os.remove('kalender_backup.ics')
    with open('kalender_backup.ics', 'w') as my_file: my_file.writelines(kalender_alt.serialize_iter())
kalender_neu = Calendar()

for i in range(10):
    kalender_neu.events.add(
        Event(
            name="My cool event neu" + str(i),
            begin='2023-04-27 00:00:00',
            end='2023-04-27 01:00:00')
    )

kalender_neu.events.add(
    Event(
        name="xxxxxxxxxxxxxxxxx" + str(i),
        begin='2023-05-03 00:00:00',
        end='2023-05-03 01:00:00')
)

kalender_neu.events.add(
    Event(
        name="aaaaaaaaaaaaa" + str(i),
        begin='2023-04-30 00:00:00',
        end='2023-04-30 01:00:00')
)

print(kalender_neu.events)
es = kalender_neu.events
for e in es: print(e.begin)

with open('kalender.ics', 'w') as my_file:
    my_file.writelines(kalender_neu.serialize_iter())

