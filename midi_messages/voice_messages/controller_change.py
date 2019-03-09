import midi_constants
from midi_messages.midi_message import MidiMessage


class ControllerChange(MidiMessage):

    def __init__(self, bdelta, blength, bstatus, bdata):
        super().__init__(bdelta, bstatus, blength, bdata)
        self.controller_num: int = None
        self.controller_val: int = None

    def parse(self):
        self.controller_num = int.from_bytes(self.bdata[0], byteorder='big')
        self.controller_val = int.from_bytes(self.bdata[1], byteorder='big')
