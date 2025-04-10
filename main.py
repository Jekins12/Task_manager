from task_manager import TaskManager

def show_help():
    print("""
Dostępne komendy:
  create [nazwa]         - utwórz nową listę zadań i przełącz się na nią
  switch [nazwa]         - przełącz się na istniejącą listę
  lists                  - wyświetl dostępne listy zadań
  add [opis] [minuty]    - dodaj nowe zadanie (minuty opcjonalnie, domyślnie 60)
  show                   - pokaż widoczne zadania
  hidden                 - pokaż ukryte zadania
  done [numer]           - oznacz zadanie jako zrealizowane
  help                   - pokaż pomoc
  exit                   - zakończ program
""")

def main():
    manager = TaskManager()
    print("== Menedżer Zadań ==")
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
                parts = cmd.removeprefix("add ").strip().rsplit(" ", 1)
                if len(parts) == 2 and parts[1].isdigit():
                    manager.current_list.add_task(parts[0], int(parts[1]))
                else:
                    manager.current_list.add_task(cmd.removeprefix("add "))
                manager.save()
                print("Dodano zadanie.")
            else:
                print("Brak aktywnej listy. Użyj 'create [nazwa]'.")
        elif cmd.startswith("done "):
            if not manager.current_list:
                print("Brak aktywnej listy. Użyj 'create [nazwa]' najpierw.")
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
            except ValueError:
                print("Niepoprawny numer zadania.")
        elif cmd == "help":
            show_help()
        elif cmd == "exit":
            manager.save()
            print("Do zobaczenia!")
            break
        else:
            print("Nieznana komenda. Wpisz 'help' aby zobaczyć dostępne komendy.")

if __name__ == "__main__":
    main()