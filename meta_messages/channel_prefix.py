from meta_messages.meta_message import MetaMessage
from midi_exceptions import IncorrectStatusException
from midi_common import MessageType


class ChannelPrefix(MetaMessage):

    btype = b'\x20'
    message_type = MessageType.CHANNEL_PREFIX
    name = "channel prefix"

    def __init__(self, bdelta, bstatus, blength, bdata):
        super().__init__(bdelta, bstatus, blength, bdata)
        if bstatus != b'\xFF':
            raise IncorrectStatusException("Invalid status: {:2x} for meta event".format(bstatus))
        self.prefix: int = None

    def parse(self):
        self.prefix = int.from_bytes(self.bdata, byteorder='big')
