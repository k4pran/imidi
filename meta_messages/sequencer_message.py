import midi_constants
from meta_messages.meta_message import MetaMessage
from midi_exceptions import IncorrectStatusException
from midi_common import MessageType


class SequencerMessage(MetaMessage):

    btype = b'\x7F'
    message_type = MessageType.SEQUENCER_MESSAGE
    name = "sequencer specific meta"

    def __init__(self, bdelta, bstatus, blength, bdata):
        super().__init__(bdelta, bstatus, blength, bdata)
        if bstatus != b'\xFF':
            raise IncorrectStatusException("Invalid status: {:2x} for meta event".format(bstatus))
        self.id: str = None
        self.id_len: int = None

    def parse(self):
        self.id_len = int.from_bytes(self.blength, byteorder='big') - midi_constants.SEQUENCER_MESSAGE_DATA_SIZE
        self.id = self.bdata[:-1].decode("utf-8")
