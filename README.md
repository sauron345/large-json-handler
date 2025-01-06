# Rozpoczęcie

* Przed wykonaniem jakiejkolwiek operacji, należy przejść do katalogu głównego projektu.
Załóżmy, że repozytorium znajduje się w katalogu podanym poniżej:

```commandline
cd C:\Users\User\Desktop\recruitment_task_nask
```

gdzie `recruitment_task_nask` jest katalogiem głównym projektu.

* Następnie wymagane jest zbudowanie obrazów oraz uruchomienie serwera produkcyjnego, którym jest Docker:

```commandline
docker-compose up --build
```

## Dostępność usługi

Usługa dostępna jest pod URI: http://localhost:8080/

## Baza wiedzy

Została stworzona w katalogu projektu `recruitment_task_nask/recruitment_task_nask` w pliku `knowledge_base.json`

## Obsługa błędnie przekazanego ip

Jeżeli klient przekaże niepoprawnie skonstruowany adres ip dla endpointu `GET /ip-tags/{ip}`,
to program zwróci wartość w postaci JSONa:

`{'error': 'Invalid ip structure'}`

## Testy jednostkowe

Znajdują się w pliku `tags_requests_handlers/test.py`.

Zostały stworzone, aby przetestować:

* walidację przekazanego ip przez klienta,
* funkcjonalność odpowiedzialną za wykrycie oraz uporządkowanie tagów należących do przekazanego ip.

W tym przypadku do weryfikacji użyta została prosta baza wiedzy `simple_knowledge_base.json`. 
Aby wykonać testy, należy użyć polecenia:

```commandline
py manage.py test
```
