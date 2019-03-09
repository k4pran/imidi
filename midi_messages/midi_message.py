from message import Message


class MidiMessage(Message):

    def __init__(self, bdelta, bstatus, blength, bdata):
        super().__init__(bdelta, bstatus, blength, bdata)
        self.channel: int = None

    def parse(self):
        self.channel = int.from_bytes(self.bstatus[1], byteorder='big')