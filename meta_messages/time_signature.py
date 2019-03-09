from meta_messages.meta_message import MetaMessage
from midi_exceptions import IncorrectStatusException


class TimeSignature(MetaMessage):

    btype = b'\x58'
    name = "time signature"

    def __init__(self, bdelta, bstatus, blength, bdata):
        super().__init__(bdelta, bstatus, blength, bdata)
        if bstatus != b'\xFF':
            raise IncorrectStatusException("Invalid status: {:2x} for meta event".format(bstatus))
        self.numerator: int = None
        self.denominator: int = None
        self.clocks_per_tick: int = None
        self.notes_per_clock: int = None


    def parse(self):
        self.numerator = int.from_bytes(self.bdata[0], byteorder='big')
        self.denominator = int.from_bytes(self.bdata[1], byteorder='big')
        self.clocks_per_tick = int.from_bytes(self.bdata[2], byteorder='big')
        self.notes_per_clock = int.from_bytes(self.bdata[3], byteorder='big')
