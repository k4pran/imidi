from meta_messages.meta_message import MetaMessage
from midi_exceptions import IncorrectStatusException
from midi_common import MessageType


class EndOfTrack(MetaMessage):

    btype = b'\x2F'
    message_type = MessageType.END_OF_TRACK
    name = "end of track"

    def __init__(self, bdelta, bstatus, blength, bdata):
        super().__init__(bdelta, bstatus, blength, bdata)
        if bstatus != b'\xFF':
            raise IncorrectStatusException("Invalid status: {:2x} for meta event".format(bstatus))

    def parse(self):
        pass
