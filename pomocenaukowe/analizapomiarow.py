'''
Skrypt służący do analizy pomiarów.
Wylicza on wartość średnią, odchylenie standardowe, błąd standardowy, oraz odchylenie procentowe.

Wykonany przez:
Miłosz Grześkowiak
Informatyka Stosowana i Systemy Pomiarowe Wydział Fizyki i Astronomii Uniwersytet Wrocławski
'''

import numpy as np

class AnalizaPomiarow:
    def __init__(self, pomiary):
        self.pomiary = pomiary

    def srednia(self):
        return np.mean(self.pomiary)

    def odchylenie_standardowe(self):
        return np.std(self.pomiary)

    def blad_standardowy(self):
        return np.std(self.pomiary)/np.sqrt(len(self.pomiary))

    def odchylenie_procentowe(self):
        return np.std(self.pomiary)/np.mean(self.pomiary)*100

    def analiza_pomiarow(self):
        print("Średnia: ", self.srednia())
        print("Odchylenie standardowe: ", self.odchylenie_standardowe())
        print("Błąd standardowy: ", self.blad_standardowy())
        print("Odchylenie procentowe: ", self.odchylenie_procentowe())

# Get input from user
pomiary = []
print("Podaj pomiary, aby zakończyć wprowadzanie, wprowadź wartość niebędącą liczbą (zmiennoprzecinkową)")
while True:
    try:
        pomiary.append(float(input("Podaj pomiar: ")))
    except ValueError:
        break

# Create object of class AnalizaPomiarow
analiza = AnalizaPomiarow(pomiary)
analiza.analiza_pomiarow()