from midi_messages.midi_message import MidiMessage
from midi_common import MessageType


class MonoModeOn(MidiMessage):
    
    message_type = MessageType.MONO_MODE_ON

    def __init__(self, bdelta, bstatus, blength, bdata):
        super().__init__(bdelta, bstatus, blength, bdata)
        self