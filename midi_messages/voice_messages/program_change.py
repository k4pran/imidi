import midi_constants
from midi_messages.midi_message import MidiMessage


class ProgramChange(MidiMessage):

    def __init__(self, bstatus, bdata):
        super().__init__(bstatus, midi_constants.PROGRAM_CHANGE_DATA_SIZE, bdata)
        self.program_num: int = None

    def parse(self):
        self.program_num = int.from_bytes(self.bdata, byteorder='big')
