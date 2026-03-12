brojevi = []

while True:
    unos = input("\nUnesite broj: ")

    if unos == "Done":
        break

    try:
        broj = float(unos)
        brojevi.append(broj)
    except ValueError:
        print("\nGreska, pogresan unos")

print("Broj brojeva:", len(brojevi))
print("Srednja vrijednost:", sum(brojevi) / len(brojevi))
print("Minimalna vrijednost:", min(brojevi))
print("Maksimalna vrijednost:", max(brojevi))

brojevi.sort()
print("Sortirana lista:", brojevi)