import classes as c
from datetime import datetime
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

autok = [c.SzemelyAuto("KWD-322", "Renault Thalia 3.0 V6", 500000, False, 1.2),
c.SzemelyAuto("RACE-001", "C classe", 20000, True, 1.3),
c.TeherAuto("PISTA", "Tatra 813 8x8", 50000, 20, 70)
]

pistaKolcsonzoje = c.AutoKolcsonzo(autok, "Pista autokolcsonzoje")
berlesek = [c.Berles(autok[0], "2024.11.20"), c.Berles(autok[0], "2024.11.22"), c.Berles(autok[1], "2024.11.26"), c.Berles(autok[2], "2024.12.24")]


def removeExpiredBerlesek():
	datum = datetime.today().strftime('%Y.%m.%d')
	datum = datetime.strptime(datum, '%Y.%m.%d')
	
	for v in berlesek:
		if (datum > datetime.strptime(v.datum, "%Y.%m.%d")):
			berlesek.remove(v)

def autoBerles():
	cls()
	print("Berelheto autok:\n(Szam beirasaval lehet valasztani)\n")
	for i, v in enumerate(autok):
		print("  " + str(i))
		v.printData()
		print()

	try:
		key = int(input())
	except:
		main()
		return -1

	if key <= len(autok) - 1:
		cls()
		maiDatum = datetime.today().strftime('%Y.%m.%d')
		print("Kivalasztott auto:")
		autok[key].printData()

		foglaltIdopontok = []
		print("\nFoglalt idopontok:")
		for v in berlesek:
			if v.auto == autok[key]:
				print("\t" + v.datum)
				foglaltIdopontok.append(v.datum)

		print("\nMelyik napra szeretned kiberelni? (YYYY.MM.DD formatum)")
		
		sikerult = False
		while(not sikerult):
			try:
				datum = input()
				datetime.strptime(datum, "%Y.%m.%d")
				
				if (datum not in foglaltIdopontok):
					if datum < maiDatum:
						print("Multba ne foglalj autot")
					else:
						sikerult = True
				else:
					sikerult = False
					print("Ez az idopont mar foglalt")
			except:
				sikerult = False
				print("Nem jo datum formatum")
		
		cls()
		print("Sikeres foglalas!\n")
		print("Ennyit kell fizetni: " + str(autok[key].berletiDij) + " Ft\n(Enter: vissza a menube)")
		berlesek.append(c.Berles(autok[key], datum))
		input()
		main()
		return autok[key].berletiDij
	
def berlesekListazasa():
	cls()
	print("Jelenlegi berlesek\n")
	removeExpiredBerlesek()
	for v in berlesek:
		v.auto.printData()
		print("\tDatum: " + v.datum + "\n")
	print("(Enter: vissza a menube)")
	input()
	main()

def berlesLemondasa():
	cls()
	print("Berles lemondasa\n(Szam beirasaval lehet valasztani)\n")
	for i, v in enumerate(berlesek):
		print("  " + str(i))
		v.auto.printData()
		print("\tDatum: " + v.datum)
	print("\n(Enter: vissza a menube)")
	try:
		key = int(input())
		berlesek.pop(key)
	except:
		main()
		return -1
	berlesLemondasa()

def main():
	cls()
	print("Autokolcsonzo rendszer\n")
	print("1: Autoberles")
	print("2: Berles lemondasa")
	print("3: Berlesek listazasa")
	print("4: Kilepes")
	key = input()
	if key == "1":
		autoBerles()
	elif key == "2":
		berlesLemondasa()
	elif key == "3":
		berlesekListazasa()
main()
