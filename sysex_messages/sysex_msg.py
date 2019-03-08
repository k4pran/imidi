from message import Message


class SysexMsg(Message):

    bstatus = b'\xF0'
    bsys_end = b'\xF7'

    def __init__(self, blength, bdata):
        super().__init__(SysexMsg.bstatus, blength, bdata)

    def parse(self):
        pass



