Przepraszam za pominięcie przykładów. Oto zaktualizowane notatki z zachowaniem przykładów dotyczących Git:

# Aplikacja Frezja

**URL:**
- Lista postów: `http://127.0.0.1:8000/posts/`
- Szczegóły posta: `http://127.0.0.1:8000/posts/1`

## HOWTO (Command Line)

### Wirtualne Środowiska

1. **Tworzenie:**
    ```sh
    python -m venv <nazwategosrodowiska>
    python -m venv .venv
    ```

2. **Aktywacja:**
    - **Windows:**
      ```sh
      .venv\Scripts\activate
      ```
    - **Unix:**
      ```sh
      source .venv/bin/activate
      ```

3. **Deaktywacja:**
    ```sh
    deactivate
    ```

### Git

1. **Klonowanie:**
    ```sh
    git clone <ścieżka np. z GitHub>
    ```

2. **Status - sprawdzenie:**
    ```sh
    git status
    ```
    Informuje o plikach śledzonych, nieśledzonych, dodanych na stos.

3. **Dodawanie plików do stosu:**
    ```sh
    git add <nazwa pliku>
    git add .
    ```

4. **Resetowanie zmian do złożenia:**
    ```sh
    git reset
    ```

5. **Usuwanie śledzenia pliku:**
    ```sh
    git rm --cached <ścieżka do pliku>
    ```

6. **Robienie commita:**
    ```sh
    git commit
    ```
    Następnie wpisz wiadomość w edytorze, zapisz i zamknij plik, aby zakończyć commit.
    Można również commitować z wiadomością w poleceniu:
    ```sh
    git commit -m "opis zmian"
    ```

7. **Dopisywanie zmian do poprzedniego commita:**
    ```sh
    git commit -a --amend
    ```

8. **Branching - gałęzie:**
    - **Tworzenie nowego brancha:**
      ```sh
      git checkout -b <nazwa_brancha>
      ```
    - **Przełączanie się:**
      ```sh
      git checkout <nazwa_brancha>
      ```
    - **Sprawdzanie istniejących branży:**
      ```sh
      git branch
      ```

9. **Pokazywanie różnic:**
    ```sh
    git diff
    ```
    Pokazuje różnice w stosunku do poprzedniego commita.

10. **Mergowanie:**
    ```sh
    git merge <nazwa_brancha>
    ```
    Merguje zmiany z `<nazwa_brancha>` do bieżącego brancha.

    **Przykład:**
    ```
    master ---- A -- B --- C --- D --- E -----------------
                         \                        / 
                     szablon_lista_postow - D1 --- D2 -- D3
    ```
    - Będąc na master robimy:
      ```sh
      git merge szablon_lista_postow
      ```

11. **Rebase:**
    ```sh
    git rebase <nazwa_brancha>
    ```
    Przesuwa nasze zmiany za zmiany z innego brancha.

    **Przykład:**
    ```
    master ---- A -- B --- C --- D --- E -----------------
                                    \                  / 
                                szablon_lista_postow - D1 --- D2 -- D3
    ```
    - Na gałęzi `szablon_lista_postow` robimy:
      ```sh
      git rebase master
      ```
    - Jeśli są konflikty, napraw je, a następnie:
      ```sh
      git rebase --continue
      ```

12. **Wymuszanie zmian w zdalnym repozytorium:**
    - Stan lokalny:
      ```
      L:  A --- B ---- C
      ```
    - Po `git push origin master`:
      ```
      O:  A --- B ---- C
      ```
    - Po rebase lub innej operacji, historia commitów zmienia się:
      ```
      L:  A --- B -- D -- C
      ```
    - `git push` się nie powiedzie, ale:
      ```sh
      git push -f origin master
      ```
      zakończy się powodzeniem.

13. **Ściąganie zmian:**
    ```sh
    git pull origin master
    ```

14. **Flow:**
    - Na masterze:
      ```sh
      git pull origin master
      git checkout -b <nazwa_brancha>
      git commit ...
      git push origin <nazwa_brancha>
      ```

### Vim

- **Tryb insert:** `i`
- **Tryb poleceń:** `esc` (lub `ctrl + c` na Windows w PyCharmie)

**Polecenia w trybie poleceń:**
    ```sh
    :w
    :q
    :wq
    ```

### isort

- Uruchomienie: `isort .`

### flake8

- **Zasady PEP8:**
  - Uruchomienie: `flake8`
  - Uruchomienie dla konkretnego pliku: `flake8 ścieżka_do_pliku`

## Contributors
- AM
- PP
- MS
- RK