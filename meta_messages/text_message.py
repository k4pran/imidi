from meta_messages import meta_message


class TextMessage(meta_message.MetaMessage):

    type = b'\x01'

    def __init__(self, blength, bdata):
        super().__init__(blength, bdata)
        self.text = ""

    def parse(self):
        self.text = self.bdata.decode("utf-8")

