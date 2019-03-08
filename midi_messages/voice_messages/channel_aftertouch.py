import midi_constants
from midi_messages.midi_message import MidiMessage


class ChannelAftertouch(MidiMessage):

    def __init__(self, bstatus, bdata):
        super().__init__(bstatus, midi_constants.CHANNEL_AFTERTOUCH_DATA_SIZE, bdata)
        self.pressure: int = None

    def parse(self):
        self.pressure = int.from_bytes(self.bdata, byteorder='big')
