from meta_messages import meta_message


class Marker(meta_message.MetaMessage):

    type = b'\x06'

    def __init__(self, blength, bdata):
        super().__init__(blength, bdata)
        self.marker = ""

    def parse(self):
        self.marker = self.bdata.decode("utf-8")
