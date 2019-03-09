from meta_messages.meta_message import MetaMessage
from midi_exceptions import IncorrectStatusException


class TextMessage(MetaMessage):

    btype = b'\x01'
    name = "text"

    def __init__(self, bdelta, bstatus, blength, bdata):
        super().__init__(bdelta, bstatus, blength, bdata)
        if bstatus != b'\xFF':
            raise IncorrectStatusException("Invalid status: {:2x} for meta event".format(bstatus))
        self.text = ""

    def parse(self):
        self.text = self.bdata.decode("utf-8")

