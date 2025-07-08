# RollaDadiMoltoPocoProfessionale

Questo progetto è un semplice roller di dadi scritto in Python, con interfaccia grafica implementata in Tkinter.  
**Natura del progetto:**  
Il software è stato realizzato a scopo puramente amatoriale, per divertimento personale e sperimentazione.  
**Non è destinato ad alcun uso di produzione o professionale.**

## Caratteristiche

- Interfaccia grafica per il lancio di dadi
- Possibilità di salvare i risultati su file di testo
- Suono e icona personalizzati

## Requisiti

- Windows OS (per via dell'utilizzo della libreria WinSound)
- Python 3.11 o superiore

## Avvio

Per avviare l'applicazione:
```sh
python main.py
```

In alternativa avvia l'eseguibile compilato con PyInstaller.

## PyInstaller

Per realizzare il proprio EXE usando PyInstaller occorre installarlo tramite PIP
```sh
pip install pyinstaller
```
e successivamente da terminale, nella cartella del progetto:
```sh
pyinstaller.exe --onefile --name "RollaDadiMoltoPocoProfessionale" --icon=d20.ico --add-data "diceRoll.wav;." --add-data "d20.ico;." --noconsole .\main.py
```
aggiungendo eventualmente le proprie modifiche desiderate al comando

## Avvertenze

Questo software è fornito "così com'è", senza alcuna garanzia.  
Non è stato testato per l'affidabilità, la sicurezza o la robustezza.  
**Utilizzare solo a scopo personale e non in contesti critici o professionali.**

---
