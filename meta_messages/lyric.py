from meta_messages import meta_message


class Lyric(meta_message.MetaMessage):

    type = b'\x05'

    def __init__(self, blength, bdata):
        super().__init__(blength, bdata)
        self.lyric = ""

    def parse(self):
        self.lyric = self.bdata.decode("utf-8")
