import midi_constants
from meta_messages.meta_message import MetaMessage
from midi_exceptions import IncorrectStatusException


class EndOfTrack(MetaMessage):

    btype = b'\x2F'
    name = "end of track"

    def __init__(self, bdelta, bstatus, blength, bdata):
        super().__init__(bdelta, bstatus, blength, bdata)
        if bstatus != b'\xFF':
            raise IncorrectStatusException("Invalid status: {:2x} for meta event".format(bstatus))

    def parse(self):
        pass
