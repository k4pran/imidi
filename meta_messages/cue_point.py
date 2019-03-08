from meta_messages import meta_message


class CuePoint(meta_message.MetaMessage):

    type = b'\x07'

    def __init__(self, blength, bdata):
        super().__init__(blength, bdata)
        self.cue_point = ""

    def parse(self):
        self.cue_point = self.bdata.decode("utf-8")


