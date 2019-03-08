import midi_constants
from meta_messages import meta_message


class ChannelPrefix(meta_message.MetaMessage):

    type = b'\x20'

    def __init__(self, bdata):
        super().__init__(midi_constants.CHANNEL_PREFIX_DATA_SIZE, bdata)
        self.prefix: int = None

    def parse(self):
        self.prefix = int.from_bytes(self.bdata, byteorder='big')

