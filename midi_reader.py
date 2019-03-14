from meta_messages.meta_message import MetaMessage
from midi_common import *
from midi_exceptions import *
import midi_constants


class MidiReader:

    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def open_file(self):
        self.file = open(self.filename, 'rb')
        print()

    def read_bytes(self, n_bytes):
        while True:
            byte = self.file.read(1)
            if byte:
                yield byte
            else:
                break

            if n_bytes > 0:
                n_bytes -= 1
                if n_bytes == 0:
                    break

    def close_file(self):
        self.file.close()


class ChunkExtractor:

    def __init__(self, filename):
        self.midi_reader = MidiReader(filename)
        self.midi_reader.open_file()
        self.header = tuple
        self.tracks = []
        self.__parse()

    def __parse(self):
        self.header = self.__parse_header()
        for track_ind in range(int.from_bytes(self.header[3], byteorder='big')):
            self.tracks.append(self.__parse_next_track())

    def __parse_header(self):
        header_sig = b''.join([i for i in self.midi_reader.read_bytes(midi_constants.HEADER_SIG_SIZE)])
        length = b''.join([i for i in self.midi_reader.read_bytes(midi_constants.HEADER_LENGTH_SIZE)])
        midi_format = b''.join([i for i in self.midi_reader.read_bytes(midi_constants.HEADER_FORMAT_SIZE)])
        track_count = b''.join([i for i in self.midi_reader.read_bytes(midi_constants.HEADER_TRACKS_SIZE)])
        division = b''.join([i for i in self.midi_reader.read_bytes(midi_constants.HEADER_DIVISION_SIZE)])
        return header_sig, length, midi_format, track_count, division

    def __parse_next_track(self):
        track_sig = b''.join([i for i in self.midi_reader.read_bytes(midi_constants.TRACK_SIG_SIZE)])
        if track_sig == b'':
            return None
        length = b''.join([i for i in self.midi_reader.read_bytes(midi_constants.TRACK_LENGTH_SIZE)])
        data = b''.join([i for i in self.midi_reader.read_bytes(int.from_bytes(length, byteorder='big'))])
        return track_sig, length, data


class MessageExtractor:

    def __init__(self, track):
        self.track: tuple = track
        self.data = track[2]
        self.byte_pos = 0
        self.running_status = None
        self.events = []
        self.__parse_track()

    def __parse_track(self):
        while self.byte_pos < len(self.data):
            delta = self.__read_delta()
            msg_body = self.__read_data()
            self.events.append((delta, msg_body))

    def __read_delta(self):
        end_flag = False
        delta = b''
        while not end_flag:
            b = self.__next_byte()
            delta += bytes([(b[0] >> 1)])
            if (b[0] >> 7) & 1 == 0:
                end_flag = True
        return delta

    def __read_data(self):
        status_byte = self.__next_byte()
        try:
            message_type = MessageCategory.resolveStatusByte(status_byte)
            self.running_status = status_byte
        except StatusNotFoundException:
            message_type = MessageCategory.resolveStatusByte(self.running_status)
            status_byte = self.running_status
            self.byte_pos -= 1

        if message_type == MessageCategory.MIDI_MESSAGE:
            return self.__extract_midi_message(status_byte)

        elif message_type == MessageCategory.META_MESSAGE:
            return self.__extract_meta_message(status_byte)

        elif message_type == MessageCategory.SYSEX_MESSAGE:
            return self.__extract_sysex_message(status_byte)

        else:
            raise StatusNotFoundException(
                "Unable to resolve status byte {} to a message type".format(hex(status_byte[0])))

    def __extract_midi_message(self, status_byte):
        midi_msg = b''
        data_length = 2

        if (status_byte[0] >> 4) == 12 or (status_byte[0] >> 4) == 13:
            data_length = 1

        for _ in range(data_length):
            midi_msg += self.__next_byte()
        return status_byte, data_length.to_bytes(1, byteorder='big'), midi_msg

    def __extract_meta_message(self, status_byte):
        meta_msg = b''
        data_length = b''

        type_byte = self.__next_byte()
        meta_msg += type_byte
        if type_byte in MetaMessage.fixed_length_types:
            data_length = self.__next_byte()

        # variable length quantity
        else:
            length_bytes_read = False
            while not length_bytes_read:
                next_byte = self.__next_byte()
                data_length += bytes([(next_byte[0] >> 1)])
                length_bytes_read = (next_byte[0] >> 7) & 1 == 0

        for _ in range(int.from_bytes(data_length, byteorder='big')):
            meta_msg += self.__next_byte()
        return status_byte, data_length, meta_msg

    def __extract_sysex_message(self, status_byte):
        sysex_msg = b''
        data_length = b''

        length_bytes_read = False
        while not length_bytes_read:
            next_byte = self.__next_byte()
            data_length += bytes([(next_byte[0] >> 1)])
            length_bytes_read = (next_byte[0] >> 7) & 1 == 0

        for _ in range(int.from_bytes(data_length, byteorder='big')):
            sysex_msg += self.__next_byte()
        return status_byte, data_length, sysex_msg

    def __next_byte(self):
        b = self.data[self.byte_pos]
        self.byte_pos += 1
        return bytes([b])
