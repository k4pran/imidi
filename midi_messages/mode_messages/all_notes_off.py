from midi_messages.midi_message import MidiMessage
from midi_common import MessageType


class AllNotesOff(MidiMessage):

    message_type = MessageType.ALL_NOTES_OFF

    def __init__(self, bdelta, bstatus, blength, bdata):
        super().__init__(bdelta, bstatus, blength, bdata)
        self