from midi_messages.midi_message import MidiMessage
from midi_common import MessageType


class ResetControllers(MidiMessage):

    message_type = MessageType.RESET_CONTROLLERS

    def __init__(self, bdelta, bstatus, blength, bdata):
        super().__init__(bdelta, bstatus, blength, bdata)
        self