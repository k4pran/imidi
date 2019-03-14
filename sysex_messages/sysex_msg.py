from message import Message
from midi_common import MessageType


class SysexMessage(Message):

    bstatus = b'\xF0'
    bsys_end = b'\xF7'
    message_type = MessageType.SYSEX

    def __init__(self, bdelta, bstatus, blength, bdata):
        super().__init__(bdelta, bstatus, blength, bdata)

    def parse(self):
        pass




