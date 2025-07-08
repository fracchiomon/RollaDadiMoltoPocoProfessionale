import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import math
import winsound
import sys
import os

from logic import DADI, tira_dadi
from salvaSuTesto import salva_txt, salva_csv

class RollaDadiApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("RollaDadi Molto Poco Professionale")
        window_width, window_height = 400, 350
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")
        self.resizable(False, False)
        self.iconbitmap("d20.ico") # Icona
        self.tipo_dado = tk.IntVar(value=20)
        self.quanti_lanci = tk.IntVar(value=1)
        self.risultati = []

        ttk.Label(self, text="Tipo di dado:").pack(pady=5)
        self.dado_menu = ttk.Combobox(self, values=DADI, textvariable=self.tipo_dado, state="readonly")
        self.dado_menu.pack()

        ttk.Label(self, text="Numero di lanci:").pack(pady=5)
        self.lanci_entry = ttk.Entry(self, textvariable=self.quanti_lanci)
        self.lanci_entry.pack()
        self.lanci_entry.bind("<FocusIn>", self.clear_lanci_entry)
        self.bind('<Return>', lambda event: self.lancia_dadi())

        self.roll_btn = ttk.Button(self, text="Lancia!", command=self.lancia_dadi)
        self.roll_btn.pack(pady=10)

        self.result_label = ttk.Label(self, text="Risultati: -")
        self.result_label.pack(pady=5)

        self.ops_frame = ttk.Frame(self)
        self.ops_frame.pack(pady=10)

        self.somma_btn = ttk.Button(self.ops_frame, text="Somma", command=self.somma)
        self.somma_btn.grid(row=0, column=0, padx=5)
        self.media_btn = ttk.Button(self.ops_frame, text="Media", command=self.media)
        self.media_btn.grid(row=0, column=1, padx=5)
        self.max_btn = ttk.Button(self.ops_frame, text="Massimo", command=self.massimo)
        self.max_btn.grid(row=0, column=2, padx=5)
        self.min_btn = ttk.Button(self.ops_frame, text="Minimo", command=self.minimo)
        self.min_btn.grid(row=0, column=3, padx=5)

        self.output_label = ttk.Label(self, text="")
        self.output_label.pack(pady=5)

        # Frame per centrare i pulsanti di salvataggio
        self.save_frame = ttk.Frame(self)
        self.save_frame.pack(pady=10)

        self.save_txt_btn = ttk.Button(self.save_frame, text="Salva su TXT", command=self.salva_su_txt)
        self.save_txt_btn.pack(side="left", padx=10)
        self.save_csv_btn = ttk.Button(self.save_frame, text="Salva su CSV", command=self.salva_su_csv)
        self.save_csv_btn.pack(side="left", padx=10)

    def lancia_dadi(self):
        try:
            # Suono opzionale
            if getattr(sys, 'frozen', False):
                base_path = sys._MEIPASS
            else:
                base_path = os.path.abspath(".")
            audio_path = os.path.join(base_path, "diceRoll.wav")
            if os.path.exists(audio_path):
                winsound.PlaySound(audio_path, winsound.SND_FILENAME | winsound.SND_ASYNC)
            tipo = int(self.tipo_dado.get())
            n = int(self.quanti_lanci.get())
            if tipo not in DADI or n < 1:
                raise ValueError
            self.risultati = tira_dadi(tipo, n)
            self.result_label.config(text=f"Risultati: {self.risultati}")
            self.output_label.config(text="")
        except Exception:
            messagebox.showerror("Errore", "Controlla i dati inseriti.")

    def somma(self):
        if self.risultati:
            self.output_label.config(text=f"Somma: {sum(self.risultati)}")
        else:
            self.output_label.config(text="Nessun risultato.")

    def media(self):
        if self.risultati:
            media = math.floor(sum(self.risultati) / len(self.risultati))
            self.output_label.config(text=f"Media arrotondata per difetto: {media}")
        else:
            self.output_label.config(text="Nessun risultato.")

    def massimo(self):
        if self.risultati:
            self.output_label.config(text=f"Massimo: {max(self.risultati)}")
        else:
            self.output_label.config(text="Nessun risultato.")

    def minimo(self):
        if self.risultati:
            self.output_label.config(text=f"Minimo: {min(self.risultati)}")
        else:
            self.output_label.config(text="Nessun risultato.")

    def clear_lanci_entry(self, event):
        self.lanci_entry.delete(0, tk.END)

    def salva_su_txt(self):
        if self.risultati:
            filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("File di testo", "*.txt")])
            if filename:
                salva_txt(self.risultati, filename)
                messagebox.showinfo("Salvataggio", f"Risultati salvati su {filename}")

    def salva_su_csv(self):
        if self.risultati:
            filename = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("File CSV", "*.csv")])
            if filename:
                salva_csv(self.risultati, filename)
                messagebox.showinfo("Salvataggio", f"Risultati salvati su {filename}")