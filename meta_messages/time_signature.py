import midi_constants
from meta_messages import meta_message


class TimeSignature(meta_message.MetaMessage):

    type = b'\x58'

    def __init__(self, bdata):
        super().__init__(midi_constants.TIME_SIG_DATA_SIZE, bdata)
        self.numerator: int = None
        self.denominator: int = None
        self.clocks_per_tick: int = None
        self.notes_per_clock: int = None


    def parse(self):
        self.numerator = int.from_bytes(self.bdata[0], byteorder='big')
        self.denominator = int.from_bytes(self.bdata[1], byteorder='big')
        self.clocks_per_tick = int.from_bytes(self.bdata[2], byteorder='big')
        self.notes_per_clock = int.from_bytes(self.bdata[3], byteorder='big')
