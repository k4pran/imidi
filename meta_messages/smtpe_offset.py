import midi_constants
from meta_messages import meta_message


class SMTPEOffset(meta_message.MetaMessage):

    type = b'\x54'

    def __init__(self, bdata):
        super().__init__(midi_constants.SMTPE_OFFSET_DATA_SIZE, bdata)
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