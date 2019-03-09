from meta_messages.meta_message import MetaMessage
from midi_exceptions import IncorrectStatusException


class CopyrightNotice(MetaMessage):

    btype = b'\x02'
    name = "copyright notice"

    def __init__(self, bdelta, bstatus, blength, bdata):
        super().__init__(bdelta, bstatus, blength, bdata)
        if bstatus != b'\xFF':
            raise IncorrectStatusException("Invalid status: {:2x} for meta event".format(bstatus))
        self.copyright_text = ""

    def parse(self):
        self.copyright_text = self.bdata.decode("utf-8")
