from meta_messages.meta_message import MetaMessage
from midi_exceptions import IncorrectStatusException
from midi_common import MessageType


class TrackName(MetaMessage):

    btype = b'\x03'
    message_type = MessageType.TRACK_NAME
    name = "track name"

    def __init__(self, bdelta, bstatus, blength, bdata):
        super().__init__(bdelta, bstatus, blength, bdata)
        if bstatus != b'\xFF':
            raise IncorrectStatusException("Invalid status: {:2x} for meta event".format(bstatus))
        self.track_name = ""

    def parse(self):
        self.track_name = self.bdata.decode("utf-8")
