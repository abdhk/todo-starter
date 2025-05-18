class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Aufgabe '{task}' wurde hinzugefügt.")

    def remove_task(self, index):
        try:
            removed_task = self.tasks.pop(index - 1)
            print(f"Aufgabe '{removed_task}' wurde entfernt.")
        except IndexError:
            print("Ungültige Aufgabennummer!")

    def view_tasks(self):
        if not self.tasks:
            print("Keine Aufgaben vorhanden.")
            return
        
        print("\nAufgabenliste:")
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")

def main():
    todo_list = TodoList()
    
    while True:
        print("\n=== Todo Liste ===")
        print("1. Aufgabe hinzufügen")
        print("2. Aufgabe entfernen")
        print("3. Aufgaben anzeigen")
        print("4. Beenden")
        
        choice = input("\nWähle eine Option (1-4): ")
        
        if choice == "1":
            task = input("Neue Aufgabe eingeben: ")
            todo_list.add_task(task)
        
        elif choice == "2":
            todo_list.view_tasks()
            if todo_list.tasks:
                try:
                    index = int(input("Nummer der zu entfernenden Aufgabe: "))
                    todo_list.remove_task(index)
                except ValueError:
                    print("Bitte gib eine gültige Nummer ein!")
        
        elif choice == "3":
            todo_list.view_tasks()
        
        elif choice == "4":
            print("Programm wird beendet. Auf Wiedersehen!")
            break
        
        else:
            print("Ungültige Eingabe! Bitte wähle 1-4.")

if __name__ == "__main__":
    main()