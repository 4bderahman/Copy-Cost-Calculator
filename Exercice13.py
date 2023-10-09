copies = int(input("Entrez le nombre de copies effectuées : "))

if copies <= 10:
    facture = copies * 0.30
elif copies <= 30:
    facture = (10 * 0.30) + ((copies - 10) * 0.25)
else:
    facture = (10 * 0.30) + (20 * 0.25) + ((copies - 30) * 0.20)

print("La facture est de :", facture, "dh")