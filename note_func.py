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

    def delete_note(self):
        title = input("Enter the title of the note: ")
        note_to_delete = None

        for note in self.notes:
            if note.title == title:
                note_to_delete = note
                break

        if note_to_delete:
            self.notes.remove(note_to_delete)
            print("Deleted")
        else:
            print("Error")

    def show_notes(self):
        if not self.notes:
            print("Empty")
        else:
            for note in self.notes:
                print(f"Title: {note.title}")
                print(f"Content: {note.content}")
                print(f"Date Created: {note.date_created}\n")
