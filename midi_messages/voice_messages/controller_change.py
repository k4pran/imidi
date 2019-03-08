import midi_constants
from midi_messages.midi_message import MidiMessage


class ControllerChange(MidiMessage):

    def __init__(self, bstatus, bdata):
        super().__init__(bstatus, midi_constants.CONTROLLER_CHANGE_DATA_SIZE, bdata)
        self.controller_num: int = None
        self.controller_val: int = None

    def parse(self):
        self.controller_num = int.from_bytes(self.bdata[0], byteorder='big')
        self.controller_val = int.from_bytes(self.bdata[1], byteorder='big')
