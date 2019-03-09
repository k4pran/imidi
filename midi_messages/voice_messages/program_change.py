import midi_constants
from midi_messages.midi_message import MidiMessage


class ProgramChange(MidiMessage):

    def __init__(self, bdelta, blength, bstatus, bdata):
        super().__init__(bdelta, blength, bstatus, bdata)
        self.program_num: int = None

    def parse(self):
        self.program_num = int.from_bytes(self.bdata, byteorder='big')
