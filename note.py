

class Note:

    def __init__(self, note_on, note_off):
        pass
        self.value = note_on.note
        self.velocity = note_on.velocity
        self.start_time = note_on.delta
        self.end_time = note_off.delta
        self.duration = self.end_time[0] - self.start_time[0]


    @staticmethod
    def pair_notes(note_ons, note_offs):
        notes = []

        # handle all notes off
        for note_on in note_ons:
            for note_off in note_offs:

                if note_off.note == note_on.note:
                    notes.append(Note(note_on, note_off))

