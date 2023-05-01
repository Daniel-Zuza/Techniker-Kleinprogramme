
class Thema():
    def __init__(self,
                 themenname,
                 wiederholungsplan,
                 aktuelle_lerneinheit='1',
                 lerneinheit_zeitaufwand=0.5,
                 ersttermin_offset=0,
                 prioritaet=False,
                 erfassungsdatum=None,
                 ):
        self.name = themenname
        self.wiederholungsplan = wiederholungsplan
        self.aktuelle_lerneinheit = aktuelle_lerneinheit
        self.prioritaet = prioritaet
        self.lerneinheit_zeitaufwand = lerneinheit_zeitaufwand
        self.erfassungsdatum = erfassungsdatum
        self.ersttermin_offset = ersttermin_offset
