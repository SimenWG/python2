# import pandas as pd
# import matplotlib.pyplot as plt
 
# data = pd.read_csv("medier.csv", index_col = 0, skiprows=[0,1], sep=";", na_values=[".", ".."], encoding="latin-1")
 
# print(data)
# print(data.head())
# data.plot()
# plt.show()


#! Oppgave 1
# starttall = int(input("Skriv inn et tall for nedtelling: "))

# tell = starttall
# while tell >= 0:
#     print(tell)
#     tell -= 1

# print("Nedtelling ferdig")
 
#! Oppgave 2

# tall = int(input("Skriv inn et tall for gangetabellen: "))
# for i in range(1, 11):
#     print(f"{tall} x {i} = {tall * i}")

#! Oppgave 3

# import random
# hemmelig_tall = random.randint(1, 100)

# gjett = -1
# while gjett != hemmelig_tall:
#     gjett = int(input("Gjett det hemmelige tallet mellom 1 og 100: "))
#     if gjett < hemmelig_tall:
#         print("For lavt. Prøv igjen.")
#     elif gjett > hemmelig_tall:
#         print("For høyt. Prøv igjen.")
#     else:
#         print("Gratulerer, du gjettet riktig!")

#! Oppgave 4

# def er_primtall(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# for tall in range(1, 101):
#     if er_primtall(tall):
#         print(tall)

#! Oppgave 5

# def sirkelareal(radius):
#     from math import pi
#     return pi * radius**2

# while True:
#     radius = input("Skriv inn radius for å finne arealet av sirkelen (eller 'stopp' for å avslutte): ")
#     if radius.lower() == "stopp":
#         break
#     try:
#         radius = float(radius)
#         print(f"Arealet av sirkelen med radius {radius} er {sirkelareal(radius):.2f}")
#     except ValueError:
#         print("Vennligst oppgi et gyldig tall for radius.")

#! Oppgave 6

# print("Skriv inn tekst (skriv 'stopp' for å avslutte):")
# antall_ord = 0
# while True:
#     tekst = input()
#     if tekst.lower() == "stopp":
#         break
#     antall_ord += len(tekst.split())
# print(f"Totalt antall ord: {antall_ord}")


# TODO Jobb med Spørsmål 7
import pandas as pd
import matplotlib.pyplot as plt
 
data = pd.read_csv("medier.csv", index_col = 0, skiprows=[0,1], sep=";", na_values=[".", ".."], encoding="latin-1")
 
print(data)
# print(data.head())
# data.plot(kind="bar")
# plt.show()