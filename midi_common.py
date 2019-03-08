from enum import Enum

import midi_exceptions


class MessageType(Enum):
    MIDI_MESSAGE = 0
    META_MESSAGE = 1
    SYSEX_MESSAGE = 2

    @staticmethod
    def resolveStatusByte(bstatus):
        if bstatus == b'\xFF':
            return MessageType.META_MESSAGE

        elif bstatus == b'\xF0' or bstatus == b'\xF7':
            return MessageType.SYSEX_MESSAGE

        elif 8 <= (bstatus[0] >> 4) <= 15:
            return MessageType.MIDI_MESSAGE

        else:
            raise midi_exceptions.StatusNotFoundException("Invalid status byte - {}".format(hex(bstatus[0])))