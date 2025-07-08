import csv

def salva_txt(risultati, filename="risultati.txt"):
    with open(filename, "a", encoding="utf-8") as f:
        f.write(", ".join(map(str, risultati)) + "\n")

def salva_csv(risultati, filename="risultati.csv"):
    with open(filename, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(risultati)