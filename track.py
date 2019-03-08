

class Track:

    SIGNATURE = "MTrk"

    def __init__(self, blength, bdata):
        self.blength = blength
        self.bdata = bdata
        self.messages = []

    def parse(self):
        pass