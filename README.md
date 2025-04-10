# 🗂️ Task Manager (Konsolowy)

Prosty, dynamiczny menedżer zadań działający w konsoli. Obsługuje wiele list zadań, ukrywanie zadań po czasie, zapisywanie do pliku JSON i oznaczanie jako zrealizowane. Całość napisana obiektowo w Pythonie.

## ✅ Funkcje

- Dodawanie i przeglądanie zadań
- Obsługa wielu list zadań
- Ukrywanie zadań po określonym czasie (domyślnie 60 minut)
- Dynamiczne numerowanie zadań (1, 2, 3, ...)
- Oznaczanie zadań jako zrealizowane
- Zapisywanie i wczytywanie zadań z pliku `tasks.json`

## ▶️ Uruchomienie

Wymagany Python 3.10 lub nowszy.

```bash
python main.py
```

## 🧪 Przykład użycia

```txt
> create dom
Utworzono i przełączono na listę: dom

> add Posprzątać pokój 30
Dodano zadanie.

> add Zrobić zakupy
Dodano zadanie.

> show
-- Lista zadań: dom --
1: [ ] Posprzątać pokój (dodano: 13:40)
2: [ ] Zrobić zakupy (dodano: 13:41)

> done 1
Oznaczono jako zrealizowane.

> hidden
Brak ukrytych zadań.
```

## 📂 Struktura projektu

```
.
├── main.py              # Wejście aplikacji
├── task.py              # Klasa pojedynczego zadania
├── task_list.py         # Klasa listy zadań
├── task_manager.py      # Główna logika aplikacji
└── tasks.json           # Zapisane dane (tworzy się automatycznie)
```

## 📄 Licencja

Projekt edukacyjny — używaj, modyfikuj i rozwijaj swobodnie. 💡