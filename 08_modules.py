import os

# operating system interaction

print(os.getcwd())

if os.path.exists("manage.py"):
    print("Avem fisierul in acest folder")
    print(os.path.getsize("manage.py"))
else:
    print("nema")

# os.listdir() returneaza o lista de nume de foldere si fisiere
# os.path.isfile(fisier) returneaza True daca "fisier" este un fisier
# os.path.getsize(fisier) returneaza marimea fisierului

#Ex.: Creati o functie care trece prin fisierele din folderul curent si returneaza marimea totala a fisierelor

def marime_totala():
    """
    Function that returns total file size for all files in root level directory.
    :return: total file size, in KB
    """
    total = 0
    fisiere = os.listdir()
    print(fisiere)

    for fisier in fisiere:
        # verificam daca este fisier
        if os.path.isfile(fisier):
            print(fisier)
            # adaugam marimea fisierului
            total += os.path.getsize(fisier)

    return total

print(marime_totala())