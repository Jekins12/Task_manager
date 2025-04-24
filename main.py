from task_manager import TaskManager

def show_help():
    print("""
Dostępne komendy:
  create [nazwa]                - utwórz nową listę zadań i przełącz się na nią
  switch [nazwa]                - przełącz się na istniejącą listę
  lists                         - wyświetl dostępne listy zadań
  add [opis] [minuty] [-x/ISO]  - dodaj zadanie (czas ukrycia, deadline ISO lub np. -30)
  show                          - pokaż widoczne zadania
  hidden                        - pokaż ukryte zadania
  done [numer]                  - oznacz zadanie jako zrealizowane
  delete [numer]                - usuń zadanie
  edit [numer] opis|czas|dl     - edytuj zadanie
  help                          - pokaż pomoc
  exit                          - zakończ program
""")

def main():
    manager = TaskManager()
    print("== Menedżer Zadań ==")
    print("Wpisz 'help' żeby wyświetlić listę dostępnych komend")
    while True:
        cmd = input("\n> ").strip()
        if cmd.startswith("create "):
            name = cmd.removeprefix("create ").strip()
            manager.create_list(name)
            print(f"Utworzono i przełączono na listę: {name}")
        elif cmd.startswith("switch "):
            name = cmd.removeprefix("switch ").strip()
            manager.switch_list(name)
            print(f"Przełączono na listę: {name}")
        elif cmd == "lists":
            print("Dostępne listy:", ", ".join(manager.list_names()))
        elif cmd == "show":
            manager.show()
        elif cmd == "hidden":
            manager.show_hidden()
        elif cmd.startswith("add "):
            if manager.current_list:
                parts = cmd.removeprefix("add ").strip().split(" ")
                desc = " ".join(parts[:-2]) if len(parts) > 2 else parts[0]
                minutes = int(parts[-2]) if len(parts) > 2 and parts[-2].isdigit() else 60
                deadline = parts[-1] if len(parts) > 2 else None
                manager.current_list.add_task(desc, minutes, deadline)
                manager.save()
                print("Dodano zadanie.")
            else:
                print("Brak aktywnej listy. Użyj 'create [nazwa]'.")
        elif cmd.startswith("done "):
            if not manager.current_list:
                print("Brak aktywnej listy.")
                continue
            try:
                index = int(cmd.removeprefix("done ").strip())
                task = manager.current_list.find_task_by_index(index)
                if task:
                    task.mark_done()
                    manager.save()
                    print("Oznaczono jako zrealizowane.")
                else:
                    print("Nie znaleziono zadania.")
            except:
                print("Niepoprawny numer.")
        elif cmd.startswith("delete "):
            try:
                index = int(cmd.removeprefix("delete ").strip())
                if manager.current_list.delete_task_by_index(index):
                    manager.save()
                    print("Zadanie usunięte.")
                else:
                    print("Nie znaleziono zadania.")
            except:
                print("Błąd. Użycie: delete [numer]")
        elif cmd.startswith("edit "):
            try:
                rest = cmd.removeprefix("edit ").strip()
                parts = rest.split(" ", 1)
                index = int(parts[0])
                desc, minutes, deadline = None, None, None
                if len(parts) > 1 and "|" in parts[1]:
                    fields = parts[1].split("|")
                    if len(fields) > 0: desc = fields[0].strip() or None
                    if len(fields) > 1: minutes = int(fields[1]) if fields[1].strip().isdigit() else None
                    if len(fields) > 2: deadline = fields[2].strip() or None
                elif len(parts) > 1:
                    desc = parts[1].strip()
                if manager.current_list.edit_task_by_index(index, desc, minutes, deadline):
                    manager.save()
                    print("Zadanie zaktualizowane.")
                else:
                    print("Nie znaleziono zadania.")
            except:
                print("Błąd edycji. Użycie: edit [numer] opis|czas|deadline")
        elif cmd == "help":
            show_help()
        elif cmd == "exit":
            manager.save()
            print("Do zobaczenia!")
            break
        else:
            print("Nieznana komenda. Wpisz 'help'.")
if __name__ == "__main__":
    main()