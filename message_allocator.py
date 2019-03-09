from midi_common import MessageType
from meta_messages import *
from midi_messages.voice_messages import *
from midi_messages.mode_messages import *
from sysex_messages import SysexMessage
from midi_exceptions import *


def allocate(bdelta, bstatus, blength, bdata):
    message_type = MessageType.resolveStatusByte(bstatus)

    if message_type == MessageType.MIDI_MESSAGE:
        return create_midi_message(bdelta, bstatus, blength, bdata)

    elif message_type == MessageType.META_MESSAGE:
        return create_meta_message(bdelta, bstatus, blength, bdata)

    elif message_type == MessageType.SYSEX_MESSAGE:
        return create_sysex_message(bdelta, bstatus, blength, bdata)


def create_midi_message(bdelta, bstatus, blength, bdata):
    midi_type = bstatus.hex()[0]

    if midi_type == '8':
        return NoteOff(bdelta, bstatus, blength, bdata)

    elif midi_type == '9':
        return NoteOn(bdelta, bstatus, blength, bdata)

    elif midi_type.upper() == 'A':
        return PolyphonicAftertouch(bdelta, bstatus, blength, bdata)

    elif midi_type.upper() == 'C':
        return ProgramChange(bdelta, bstatus, blength, bdata)

    elif midi_type.upper() == 'D':
        return ChannelAftertouch(bdelta, bstatus, blength, bdata)

    elif midi_type.upper() == 'E':
        return PitchBend(bdelta, bstatus, blength, bdata)

    elif midi_type.upper() == 'B':

        # Mode messages
        midi_type = bdata[0].to_bytes(1, byteorder='big').hex()

        if midi_type == '78':
            return SoundOff(bdelta, bstatus, blength, bdata)

        elif midi_type == '79':
            return ResetControllers(bdelta, bstatus, blength, bdata)

        elif midi_type == '7A':
            return LocalChange(bdelta, bstatus, blength, bdata)

        elif midi_type == '7B':
            return NotesOff(bdelta, bstatus, blength, bdata)

        elif midi_type == '7C':
            return OmniModeOff(bdelta, bstatus, blength, bdata)

        elif midi_type == '7D':
            return OmniModeOn(bdelta, bstatus, blength, bdata)

        elif midi_type == '7E':
            return MonoModeOn(bdelta, bstatus, blength, bdata)

        elif midi_type == '7F':
            return PolyModeOn(bdelta, bstatus, blength, bdata)

        else:
            return ControllerChange(bdelta, bstatus, blength, bdata)

    else:
        raise TypeNotFoundException("Unrecognised midi message")


def create_meta_message(bdelta, bstatus, blength, bdata):
    meta_type = bdata[0].to_bytes(1, byteorder='big')

    if meta_type == b'\x00':
        return SequenceNumber(bdata, bstatus, blength, bdata)

    elif meta_type == b'\x01':
        return TextMessage(bdelta, bstatus, blength, bdata)

    elif meta_type == b'\x02':
        return CopyrightNotice(bdelta, bstatus, blength, bdata)

    elif meta_type == b'\x03':
        return TrackName(bdelta, bstatus, blength, bdata)

    elif meta_type == b'\x04':
        return Instrument(bdelta, bstatus, blength, bdata)

    elif meta_type == b'\x05':
        return Lyric(bdelta, bstatus, blength, bdata)

    elif meta_type == b'\x06':
        return Marker(bdelta, bstatus, blength, bdata)

    elif meta_type == b'\x07':
        return CuePoint(bdelta, bstatus, blength, bdata)

    elif meta_type == b'\x20':
        return ChannelPrefix(bdelta, bstatus, blength, bdata)

    elif meta_type == b'\x21':
        return MidiPort(bdelta, bstatus, blength, bdata)

    elif meta_type == b'\x2F':
        return EndOfTrack(bdelta, bstatus, blength, bdata)

    elif meta_type == b'\x51':
        return Tempo(bdelta, bstatus, blength, bdata)

    elif meta_type == b'\x54':
        return SMTPEOffset(bdelta, bstatus, blength, bdata)

    elif meta_type == b'\x58':
        return TimeSignature(bdelta, bstatus, blength, bdata)

    elif meta_type == b'\x59':
        return KeySignature(bdelta, bstatus, blength, bdata)

    elif meta_type == b'\x7F':
        return SequencerMessage(bdelta, bstatus, blength, bdata)

    else:
        raise TypeNotFoundException("Unrecognised meta message")

def create_sysex_message(bdelta, bstatus, blength, bdata):
    return SysexMessage(bdelta, bstatus, blength, bdata)

