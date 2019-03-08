import midi_constants
from meta_messages import meta_message


class EndOfTrack(meta_message.MetaMessage):

    type = b'\x2F'

    def __init__(self):
        super().__init__(midi_constants.END_OF_TRACK_DATA_SIZE, b'')

    def parse(self):
        pass
