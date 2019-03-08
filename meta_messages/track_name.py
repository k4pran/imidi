from meta_messages import meta_message


class TrackName(meta_message.MetaMessage):

    type = b'\x03'

    def __init__(self, blength, bdata):
        super().__init__(blength, bdata)
        self.track_name = ""

    def parse(self):
        self.track_name = self.bdata.decode("utf-8")
