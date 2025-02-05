from note import Note

class NoteFunc:
    def __init__(self):
        self.notes = []

    def create_note(self):
        title = input("Title: ")
        content = input("Content: ")
        new_note = Note(title, content)
        self.notes.append(new_note)
        print("Created")