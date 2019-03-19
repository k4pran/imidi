from midi_constants import *
from midi_messages.midi_message import MidiMessage
from midi_common import MessageType


class ControllerChange(MidiMessage):

    message_type = MessageType.CONTROLLER_CHANGE

    def __init__(self, bdelta, blength, bstatus, bdata):
        super().__init__(bdelta, bstatus, blength, bdata)
        self.controller_num = self.bdata[0]
        self.controller_val = self.bdata[1]

    def parse(self):
        pass

    def __str__(self):
        return "|| Control change || {padding:10} function - {0} {padding:4} value - {1}".format(
            CONTROL_CHANGE_MAP[self.controller_num], self.controller_val, padding="")
