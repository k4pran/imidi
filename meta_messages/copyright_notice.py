from meta_messages import meta_message


class CopyrightNotice(meta_message.MetaMessage):

    type = b'\x02'

    def __init__(self, blength, bdata):
        super().__init__(blength, bdata)
        self.copyright_text = ""

    def parse(self):
        self.copyright_text = self.bdata.decode("utf-8")