from meta_messages.meta_message import MetaMessage
from midi_exceptions import IncorrectStatusException
from midi_common import MessageType


class CuePoint(MetaMessage):

    btype = b'\x07'
    message_type = MessageType.CUE_POINT
    name = "cue point"

    def __init__(self, bdelta, bstatus, blength, bdata):
        super().__init__(bdelta, bstatus, blength, bdata)
        if bstatus != b'\xFF':
            raise IncorrectStatusException("Invalid status: {:2x} for meta event".format(bstatus))
        self.cue_point = ""

    def parse(self):
        self.cue_point = self.bdata.decode("utf-8")


