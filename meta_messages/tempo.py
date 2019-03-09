import midi_constants
from meta_messages.meta_message import MetaMessage
from midi_exceptions import IncorrectStatusException


class Tempo(MetaMessage):

    btype = b'\x51'
    name = "set tempo"
    default_microseconds = 500000
    default_beats = 120

    def __init__(self, bdelta, bstatus, blength, bdata):
        super().__init__(bdelta, bstatus, blength, bdata)
        if bstatus != b'\xFF':
            raise IncorrectStatusException("Invalid status: {:2x} for meta event".format(bstatus))
        self.microseconds = None

    def parse(self):
        self.microseconds = int.from_bytes(self.bdata, byteorder='big')

    def asMicroSeconds(self):
        return self.microseconds

    def asBeats(self):
        return self.microsecond_to_beats(self.microseconds)

    @staticmethod
    def microsecond_to_beats(microseconds):
        return 100000 / microseconds * 60

    @staticmethod
    def beats_to_microseconds(beats):
        return 60 / beats * 1000000

