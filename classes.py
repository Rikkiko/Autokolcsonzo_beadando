from abc import ABC, abstractmethod

class Auto(ABC):
	@abstractmethod
	def __init__(self, rendszam, tipus, berletiDij):
		self.rendszam = rendszam
		self.tipus = tipus
		self.berletiDij = berletiDij
	
	@abstractmethod
	def printData(self):
		print("\tTipus: " + self.tipus)
		print("\tRendszam: " + self.rendszam)
		print("\tBerleti dij: " + str(self.berletiDij) + " Ft")

class SzemelyAuto(Auto):
	def __init__(self, rendszam, tipus, berletiDij, tetoCsomagtarto, kalapTartoMeret):
		super().__init__(rendszam, tipus, berletiDij)
		self.tetoCsomagtarto = tetoCsomagtarto
		self.kalapTartoMeret = kalapTartoMeret

	def printData(self):
		super(SzemelyAuto, self).printData()
		print("\tTetocsomagtarto: " + ("Van" if self.tetoCsomagtarto else "Nincs"))
		print("\tKalaptarto meret: " + str(self.kalapTartoMeret) + " m2")

class TeherAuto(Auto):
	def __init__(self, rendszam, tipus, berletiDij, platoMeret, vontathatoSuly):
		super().__init__(rendszam, tipus, berletiDij)
		self.platoMeret = platoMeret
		self.vontathatoSuly = vontathatoSuly

	def printData(self):
		super(TeherAuto, self).printData()
		print("\tPlato meret: " + str(self.platoMeret) + " m2")
		if self.vontathatoSuly > 0:
			print("\tVontathato suly: " + str(self.vontathatoSuly) + " tonna")

class AutoKolcsonzo():
	def __init__(self, autok, nev):
		self.autok = autok
		self.nev = nev

class Berles():
	def __init__(self, auto, datum):
		self.auto = auto
		self.datum = datum