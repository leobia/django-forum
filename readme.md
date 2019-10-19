# Benvenuti in Piazza!

Ciao! Piazza è un progetto personale realizzato da me (Leonardo Bianco). Ho sviluppato questo progetto con l'intenzione di continuare ad imparare la tecnologia django (python) iniziata col progetto Libreria (sempre all'interno dei miei repos).


## Tecnologie utilizzate

Le tecnologie utilizzate all'interno di questo progetto sono le classiche per le *viste*:
- **HTML**
- **CSS** (Bootstrap e FontAwesome)
- JavaScript (davvero poco però!)

Il progetto però, come già scritto, è stato fatto con l'intenzione di imparare il framework **django** che permette di sviluppare con il pattern **MVC** (loro lo definiscono Model-View-Template, MVT, ma il concetto è lo stesso).
Con django si ha la possibilità di scrivere in python models e controller, ma la cosa più utile è la possibilità di fare dei moduli riutilizzabili che poi uniti vanno a formare un'applicazione.

## Installazione del progetto

Bisogna assicurarsi che sia installato **python3** (io ho usato la 3.7) per poter far girare il progetto.
Fatto ciò possiamo procedere alla creazione di un virtual environment per il progetto contenente tutte le librerie che ci servono. 

Dopo essersi posizionati nella cartella in cui si vuole scaricare il progetto, aprire un terminale o un cmd.exe e fare questo comando:

    python3 -m venv nome_v_env

Poi bisogna attivarlo:

    #Per windows lanciare:
    nome_v_env\Scripts\activate

    #Per Linux/OSX
    source nome_v_env/bin/activate

Poi si procede ad installare le varie **dipendenze**:

    pip install django
    pip install django_crispy_forms
    pip install pillow

Eseguire questa serie di comandi poi per eseguire le migrazioni del db, creare un superuser per console di amministrazione e far partire il server (assicurarsi di essere sempre all'interno dell'ambiente virtuale, lo si è se prima dell'utente sul terminale c'è il nome dell'ambiente):

    python manage.py migrate
    python manage.py createsuperuser
    python manage.py makemigrations libreria
    python manage.py migrate
    python manage.py runserver

Aprire un browser con il link http://localhost:8000 e verificare che il server sia partito (dovrebbe essere visualizzata la homepage senza dati).
Aprire la pagina http://localhost:8000/admin e entrare con username e password inseriti in precedenza. All'interno di questa pagina potranno essere fatte operazioni CRUD sulle entità presenti.


## Descrizione funzionale

Le funzioni principali dell'applicazione sono:
- Registrazione
- Login
- Creazione (per admin e moderatori) e visualizzazione di **sezioni**
- Creazioni e visualizzazione di **discussioni**
- Creazione e visualizzazione di **posts**
- Visualizzazione della lista utenti e di un singolo profilo
- Ricerca all'interno del forum

## Obiettivi futuri

Ci sono molte funzionalità che potrebbero essere implementate per migliorare il sito, ma più che aggiungere funzionalità avevo l'obiettivo di fare un restyle al sito applicando le linee guida del material design di google (che ho cercato di applicare in alcuni punti, tipo la scelta dei diversi font).
