import midi_constants
from meta_messages import meta_message


class Tempo(meta_message.MetaMessage):

    type = b'\x51'
    default_microseconds = 500000
    default_beats = 120

    def __init__(self, bdata):
        super().__init__(midi_constants.TEMPO_DATA_SIZE, bdata)
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

