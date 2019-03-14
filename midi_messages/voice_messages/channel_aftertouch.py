import midi_constants
from midi_messages.midi_message import MidiMessage
from midi_common import MessageType


class ChannelAftertouch(MidiMessage):
    
    message_type = MessageType.CHANNEL_AFTERTOUCH

    def __init__(self, bdelta, blength, bstatus, bdata):
        super().__init__(bdelta, bstatus, blength, bdata)
        self.pressure = self.bdata[0]

    def parse(self):
        pass
