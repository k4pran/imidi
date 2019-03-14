from meta_messages.meta_message import MetaMessage
from midi_exceptions import IncorrectStatusException
from midi_common import MessageType


class SequenceNumber(MetaMessage):

    btype = b'\x00'
    message_type = MessageType.SEQUENCE_NUMBER
    name = "sequence number"

    def __init__(self, bdelta, bstatus, blength, bdata):
        super().__init__(bdelta, bstatus, blength, bdata)
        if bstatus != b'\xFF':
            raise IncorrectStatusException("Invalid status: {:2x} for meta event".format(bstatus))
        self.sequence_number: int = None

    def parse(self):
        self.sequence_number = int.from_bytes(self.bdata, byteorder='big')
