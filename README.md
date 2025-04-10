# 🗂️ Task Manager (Konsolowy)

Prosty, dynamiczny menedżer zadań działający w konsoli. Obsługuje wiele list zadań, ukrywanie zadań po czasie, zapisywanie do pliku JSON i oznaczanie jako zrealizowane. Całość napisana obiektowo w Pythonie.

## ✅ Funkcje

- Dodawanie i przeglądanie zadań
- Obsługa wielu list zadań
- Ukrywanie zadań po określonym czasie (domyślnie 60 minut)
- Deadline z ostrzeżeniami:
  - ⏰ zbliża się termin (do 1h)
  - ⛔️ termin minął
- Wsparcie dla deadline względnego (`-30` = 30 minut przed końcem)
- Edytowanie i usuwanie zadań
- Dynamiczne numerowanie zadań (1, 2, 3, ...)
- Zapis i odczyt danych z pliku `tasks.json`

## ▶️ Uruchomienie

Wymagany Python 3.10 lub nowszy.

```bash
python main.py
```

## 🧪 Przykład użycia

```txt
> create dom
Utworzono i przełączono na listę: dom

> add Zrobić pranie 30 -10
Dodano zadanie.

> show
-- Lista zadań: dom --
1: [ ] ⏰ Zrobić pranie | deadline: 2025-04-11T13:25 (dodano: 13:05)

> done 1
Oznaczono jako zrealizowane.

> delete 1
Zadanie usunięte.
```

## ✏️ Edytowanie

```bash
edit 1 Nowy opis|45|-15
```

- Zmienia opis, czas ukrycia i deadline na 30 minut przed końcem

## 📂 Struktura projektu

```
.
├── main.py              # Wejście aplikacji
├── task.py              # Klasa pojedynczego zadania
├── task_list.py         # Klasa listy zadań
├── task_manager.py      # Główna logika aplikacji
├── tasks.json           # Zapisane dane (tworzy się automatycznie)
└── README.md            # Instrukcja użycia
```

## 📄 Licencja

Projekt edukacyjny — używaj, modyfikuj i rozwijaj swobodnie. 💡
