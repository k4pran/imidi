from enum import Enum

import midi_exceptions


class MessageCategory(Enum):
    MIDI_MESSAGE = 0
    META_MESSAGE = 1
    SYSEX_MESSAGE = 2

    @staticmethod
    def resolveStatusByte(bstatus):
        if bstatus == b'\xFF':
            return MessageCategory.META_MESSAGE

        elif bstatus == b'\xF0' or bstatus == b'\xF7':
            return MessageCategory.SYSEX_MESSAGE

        elif 8 <= (bstatus[0] >> 4) <= 15:
            return MessageCategory.MIDI_MESSAGE

        else:
            raise midi_exceptions.StatusNotFoundException("Invalid status byte - {}".format(hex(bstatus[0])))


class MessageType(Enum):
    CHANNEL_PREFIX = 0
    COPYRIGHT_NOTICE = 1
    CUE_POINT = 2
    END_OF_TRACK = 3
    INSTRUMENT = 4
    KEY_SIGNATURE = 5
    LYRIC = 6
    MARKER = 7
    MIDI_PORT = 8
    SEQUENCE_NUMBER = 9
    SEQUENCER_MESSAGE = 10
    SMTPE_OFFSET = 11
    TEMPO = 12
    TEXT_MESSAGE = 13
    TIME_SIGNATURE = 14
    TRACK_NAME = 15
    LOCAL_CONTROL = 16
    MONO_MODE_ON = 17
    ALL_NOTES_OFF = 18
    OMNI_MODE_OFF = 19
    OMNI_MODE_ON = 20
    POLY_MODE_ON = 21
    RESET_CONTROLLERS = 22
    SOUND_OFF = 23
    CHANNEL_AFTERTOUCH = 24
    CONTROLLER_CHANGE = 25
    NOTE_OFF = 26
    NOTE_ON = 27
    PITCH_BEND = 28
    POLYPHONIC_AFTERTOUCH = 29
    PROGRAM_CHANGE = 30
    SYSEX = 31
