from task_manager import TaskManager

def show_help():
    print("""
Dostępne komendy:
  create [nazwa]           - utwórz nową listę zadań i przełącz się na nią
  switch [nazwa]           - przełącz się na istniejącą listę
  lists                    - wyświetl dostępne listy zadań
  add [opis] [minuty]      - dodaj nowe zadanie (minuty opcjonalnie, domyślnie 60)
  show                     - pokaż widoczne zadania
  hidden                   - pokaż ukryte zadania
  done [numer]             - oznacz zadanie jako zrealizowane
  delete [numer]           - usuń zadanie o danym numerze
  edit [numer] [opis]|[czas] - edytuj opis i/lub czas ukrycia zadania
  help                     - pokaż pomoc
  exit                     - zakończ program
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
        elif cmd.startswith("delete "):
            try:
                index = int(cmd.removeprefix("delete ").strip())
                if manager.current_list.delete_task_by_index(index):
                    manager.save()
                    print("Zadanie usunięte.")
                else:
                    print("Nie znaleziono zadania.")
            except ValueError:
                print("Podaj numer zadania do usunięcia.")
        elif cmd.startswith("edit "):
            try:
                rest = cmd.removeprefix("edit ").strip()
                parts = rest.split(" ", 1)
                index = int(parts[0])
                desc = None
                minutes = None
                if len(parts) > 1:
                    if "|" in parts[1]:
                        fields = parts[1].split("|")
                        desc = fields[0].strip() if fields[0].strip() else None
                        try:
                            minutes = int(fields[1].strip())
                        except:
                            minutes = None
                    else:
                        desc = parts[1].strip()
                if manager.current_list.edit_task_by_index(index, desc, minutes):
                    manager.save()
                    print("Zadanie zaktualizowane.")
                else:
                    print("Nie znaleziono zadania.")
            except Exception as e:
                print("Błąd edycji. Użycie: edit [numer] [opis] lub edit [numer] opis|czas")
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