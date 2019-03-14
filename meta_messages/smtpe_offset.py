from meta_messages.meta_message import MetaMessage
from midi_exceptions import IncorrectStatusException
from midi_common import MessageType


class SMTPEOffset(MetaMessage):

    btype = b'\x54'
    message_type = MessageType.SMTPE_OFFSET
    name = "SMTPE offset"

    def __init__(self, bdelta, bstatus, blength, bdata):
        super().__init__(bdelta, bstatus, blength, bdata)
        if bstatus != b'\xFF':
            raise IncorrectStatusException("Invalid status: {:2x} for meta event".format(bstatus))
        self.hours: int = None
        self.mins: int = None
        self.secs: int = None
        self.frames: int = None
        self.fract_frames: int = None


    def parse(self):
        self.hours = int.from_bytes(self.bdata[0], byteorder='big')
        self.mins = int.from_bytes(self.bdata[1], byteorder='big')
        self.secs = int.from_bytes(self.bdata[2], byteorder='big')
        self.frames = int.from_bytes(self.bdata[3], byteorder='big')
        self.fract_frames = int.from_bytes(self.bdata[4], byteorder='big')