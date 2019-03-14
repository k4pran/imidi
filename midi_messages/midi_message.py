from message import Message


class MidiMessage(Message):

    def __init__(self, bdelta, bstatus, blength, bdata):
        super().__init__(bdelta, bstatus, blength, bdata)
        self.channel = (bstatus[0] & 0x0F) + 1
        self.parse()

    def parse(self):
        pass