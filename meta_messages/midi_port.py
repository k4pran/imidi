from meta_messages.meta_message import MetaMessage
from midi_exceptions import IncorrectStatusException
from midi_common import MessageType


class MidiPort(MetaMessage):

    btype = b'\x21'
    message_type = MessageType.MIDI_PORT
    name = "midi port"

    def __init__(self, bdelta, bstatus, blength, bdata):
        super().__init__(bdelta, bstatus, blength, bdata)
        if bstatus != b'\xFF':
            raise IncorrectStatusException("Invalid status: {:2x} for meta event".format(bstatus))
        self.port_number: int = None

    def parse(self):
        self.port_number = int.from_bytes(self.bdata, byteorder='big')