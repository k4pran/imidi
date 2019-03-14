from midi_messages.midi_message import MidiMessage
from midi_common import MessageType


class LocalControl(MidiMessage):

    message_type = MessageType.LOCAL_CONTROL


    def __init__(self, bdelta, bstatus, blength, bdata):
        super().__init__(bdelta, bstatus, blength, bdata)
