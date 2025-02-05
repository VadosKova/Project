from tkinter import *
from tkinter import messagebox, filedialog
from note import Note
import os

#консоль
# class NoteFunc:
#     def __init__(self):
#         self.notes = []
#         self.file_path = "notes.txt"
#
#     def create_note(self):
#         title = input("Title: ")
#         content = input("Content: ")
#         new_note = Note(title, content)
#         self.notes.append(new_note)
#
#         try:
#             with open(self.file_path, 'a') as file:
#                 file.write(f"Title: {new_note.title}\n")
#                 file.write(f"Content: {new_note.content}\n")
#                 file.write(f"Date: {new_note.date_created}\n")
#             print(f"Note '{new_note.title}' created and saved")
#         except Exception:
#             print("Error")
#
#     def delete_note(self):
#         title = input("Enter the title of the note: ")
#         note_to_delete = None
#
#         for note in self.notes:
#             if note.title == title:
#                 note_to_delete = note
#                 break
#
#         if note_to_delete:
#             self.notes.remove(note_to_delete)
#             print("Deleted")
#         else:
#             print("Error")
#
#     def show_notes(self):
#         if not self.notes:
#             print("Empty")
#         else:
#             for note in self.notes:
#                 print(f"Title: {note.title}")
#                 print(f"Content: {note.content}")
#                 print(f"Date Created: {note.date_created}\n")
#
#     def load_notes(self):
#         file_path = input("Path to note file: ")
#
#         if not os.path.exists(file_path):
#             print("Error")
#             return
#
#         try:
#             with open(file_path, 'r') as file:
#                 lines = file.readlines()
#                 self.notes.clear()
#                 note = None
#
#                 for line in lines:
#                     if line.startswith("Title:"):
#                         if note:
#                             self.notes.append(note)
#                         note = Note(line[len("Title: "):].strip(), "")
#                     elif line.startswith("Content:"):
#                         note.content = line[len("Content: "):].strip()
#                     elif line.startswith("Date:"):
#                         note.date_created = line[len("Date: "):].strip()
#
#                 if note:
#                     self.notes.append(note)
#
#             print("Notes loaded")
#             self.show_notes()
#         except Exception:
#             print("Error")
#
#     def run(self):
#         while True:
#             print("\nMenu:")
#             print("1. Create note")
#             print("2. Delete note")
#             print("3. Show all notes")
#             print("4. Load notes from file")
#             print("5. Exit")
#
#             try:
#                 choice = int(input("Choose an option: "))
#                 if choice == 1:
#                     self.create_note()
#                 elif choice == 2:
#                     self.delete_note()
#                 elif choice == 3:
#                     self.show_notes()
#                 elif choice == 4:
#                     self.load_notes()
#                 elif choice == 5:
#                     print("End")
#                     break
#                 else:
#                     print("Error")
#             except ValueError:
#                 print("Error")

#GUI
class NoteFunc:
    def __init__(self, root):
        self.root = root
        self.root.title("Notes")
        self.notes = []
        self.view()