import message


class MidiMessage(message.Message):

    def __init__(self, bstatus, blength, bdata):
        super().__init__(bstatus, blength, bdata)
        self.channel: int = None

    def parse(self):
        self.channel = int.from_bytes(self.bstatus[1], byteorder='big')