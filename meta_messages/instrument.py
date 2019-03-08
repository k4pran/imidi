from meta_messages import meta_message


class Instrument(meta_message.MetaMessage):

    type = b'\x04'

    def __init__(self, blength, bdata):
        super().__init__(blength, bdata)
        self.instrument = ""

    def parse(self):
        self.instrument = self.bdata.decode("utf-8")
