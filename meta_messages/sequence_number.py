import midi_constants
from meta_messages.meta_message import MetaMessage


class SequenceNumber(MetaMessage):

    type = b'\x00'

    def __init__(self, bdata):
        super().__init__(midi_constants.SEQUENCE_NUMBER_DATA_SIZE, bdata)
        self.sequence_number = None

    def parse(self):
        self.sequence_number = int.from_bytes(self.bdata, byteorder='big')
