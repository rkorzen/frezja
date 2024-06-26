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


7. Dopisywanie zmian do poprzedniego commita

    git commit -a --amend

8. branche - gałęzie

* tworzenie nowego brancha

    git checkout -b <nazwa_brancha>

* przełączanie się:

    git checkout <nazwa brancha>

* sprawdzanie jakie są branche i na którym jesteśmy:

    git branch

* git diff

pokazuje różnice w stosunku do poprzedniego commita


* mergowanie

    git merge <nazwa brancha>

merguje zmiany z <naazwa brancha> do bieżacego brancha na którym pracujemy

master ---- A -- B --- C --- D --- E --------------------------------------
                         \                                         / (będąc na master robimy git merge szablon_lista_postow)
                         szablon_lista_postow - D1 --- D2 -- D3 ---


* rebase 

    git rebase <nazwa brancha>

przesuwanie naszych zmian za zmiany z innego brancha

master ---- A -- B --- C --- D --- E --------------------------------------
                                    \                                         / (będąc na master robimy git merge szablon_lista_postow)
                                     szablon_lista_postow - D1 --- D2 -- D3 ---

na gałęzy szablon_lista_postow robimy:  
git rebase master
jeśli są konflikty to naprawiamy je i potem

git rebase --continue

* wymuszanie zmian w zdalnym repo

L - local, O- origin (zdalne repo)

L:  A --- B ---- C

git push origin master:

O:  A --- B ---- C

- tutaj coś robimy  np jakiegoś rebse i zmienia się historia commitow

L:  A --- B -- D -- C

git push się nie powiedzie

ale powiedzie się to:

    git push -f origin master

# vim

i - tryb insert
esc - tryb poleceń  (ctrl c - na windowsie - w pycharmie) 

polecenia wydajemy w trybie polecń


    :w
    :q

lub

    :wq


### isort

isort .

### flake8

flake8

flake8 sciezka do pliku






xxxx

## Contributors
- [AM]
- [PP]
- [MS]
- [RK]
drugi
trzeci

czwarty


