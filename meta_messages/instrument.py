from meta_messages.meta_message import MetaMessage
from midi_exceptions import IncorrectStatusException
from midi_common import MessageType


class Instrument(MetaMessage):

    btype = b'\x04'
    message_type = MessageType.INSTRUMENT
    name = "instrument name"

    def __init__(self, bdelta, bstatus, blength, bdata):
        super().__init__(bdelta, bstatus, blength, bdata)
        if bstatus != b'\xFF':
            raise IncorrectStatusException("Invalid status: {:2x} for meta event".format(bstatus))
        self.instrument = ""

    def parse(self):
        self.instrument = self.bdata.decode("utf-8")
