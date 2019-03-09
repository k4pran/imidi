from message import Message


class SysexMessage(Message):

    bstatus = b'\xF0'
    bsys_end = b'\xF7'

    def __init__(self, bdelta, bstatus, blength, bdata):
        super().__init__(bdelta, bstatus, blength, bdata)

    def parse(self):
        pass




