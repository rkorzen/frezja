# Aplikacja Frezja

http://127.0.0.1:8000/posts/

/posts/  - lista
/posts/1 - szczegóły posta

## HOWTO (Command line)

### wirtualne środowiska

1. Tworzenie

    python -m venv <nazwategosrodowiska>
    python -m venv .venv

2. Aktywacja

* windows

    .venv\Scripts\activate

* Unix:

    source .venv/bin/activate

3. Deaktywacja:

    deactivate


### git

1. klonowanie:

    git clone <ściezka np z github>

2. status - sprawdzenie

    git status

To nam powie co jest śledzone, nieśledzone, dodane na stos

3. dodawanie plikow do stosu (przygotowanie do złożenia)

    git add <nazwa pliku>
    
    git add .

4. resetowanie zmian do złożenia

    git reset

5. usuwanie śledzenia pliku

    git rm --cached <scieżka do pliku>

6. Robienie commita

    git commit

    po tym wpisujemy w edytorze git message. Zapisujemy i zamykamy plik i commit się kończy

ale można też commitować z git message w poleceniu 

    git commit -m "opis zmian"


# vim

i - tryb insert
esc - tryb poleceń  (ctrl c - na windowsie - w pycharmie) 

polecenia wydajemy w trybie polecń


    :w
    :q

lub

    :wq











## Contributors
- [AM]
- [PP]
- [MS]
- [RK]
drugi
trzeci

czwarty


