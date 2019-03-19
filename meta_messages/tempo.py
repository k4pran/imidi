import midi_constants
from meta_messages.meta_message import MetaMessage
from midi_exceptions import IncorrectStatusException
from midi_common import MessageType


class Tempo(MetaMessage):

    btype = b'\x51'
    message_type = MessageType.TEMPO
    name = "set tempo"
    default_microseconds = 500000
    default_beats = 120

    def __init__(self, bdelta, bstatus, blength, bdata):
        super().__init__(bdelta, bstatus, blength, bdata)
        if bstatus != b'\xFF':
            raise IncorrectStatusException("Invalid status: {:2x} for meta event".format(bstatus))
        self.microseconds = None
        self.microseconds = int.from_bytes(self.bdata[1:], byteorder='big')

    def parse(self):
        pass

    def as_ticks(self):
        return self.microseconds

    def as_ms_per_quart(self):
        return self.microseconds / 1000

    def as_ms_per_tick(self, ppq):
        return self.as_ms_per_quart() / ppq

    def as_bpm(self):
        return self.ms_to_bpm(self.microseconds)

    @staticmethod
    def ms_to_bpm(microseconds):
        return 60 / microseconds * 1000000

    @staticmethod
    def bpm_to_ms(beats):
        return 60 / beats * 1000000