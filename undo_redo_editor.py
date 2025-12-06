# undo_redo_editor.py

class UndoRedoEditor:
    def __init__(self):
        self.text = ""           # current text
        self.undo_stack = []     # stack for undo operations
        self.redo_stack = []     # stack for redo operations

    def type_text(self, new_text):
        # Before changing, save current state in undo stack
        self.undo_stack.append(self.text)
        # Once we type something new, redo history is cleared
        self.redo_stack.clear()
        # Add the new text
        self.text += new_text

    def undo(self):
        if not self.undo_stack:
            print("Nothing to undo!")
            return
        # Save current state in redo stack
        self.redo_stack.append(self.text)
        # Go back to last state
        self.text = self.undo_stack.pop()

    def redo(self):
        if not self.redo_stack:
            print("Nothing to redo!")
            return
        # Save current state in undo stack
        self.undo_stack.append(self.text)
        # Go forward to next state
        self.text = self.redo_stack.pop()

    def show_text(self):
        print(f"\nCurrent text: \"{self.text}\"\n")


def main():
    editor = UndoRedoEditor()

    while True:
        print("==== Undo–Redo Editor Using Stack ====")
        print("1. Type text (append)")
        print("2. Undo")
        print("3. Redo")
        print("4. Show current text")
        print("5. Exit")

        choice = input("Enter your choice (1–5): ")

        if choice == "1":
            new_text = input("Enter text to add: ")
            editor.type_text(new_text)
        elif choice == "2":
            editor.undo()
        elif choice == "3":
            editor.redo()
        elif choice == "4":
            editor.show_text()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Try again.\n")


if __name__ == "__main__":
    main()
