from random import randint
from celle import Celle

class Spillebrett:
    def __init__(self, rader, kolonner):
        self._rader = rader
        self._kolonner = kolonner
        self._rutenett = []
        self._generasjonsnummer = 0
        for rad in range(rader):
            self._rutenett.append([])

            for kolonne in range(kolonner):
                self._rutenett[rad].append(Celle())

        self._generer()

    def tegnBrett(self):
        for x in range(10):
            print("")

        for el1 in range(self._rader):
            for el2 in range(self._kolonner):
                print(self._rutenett[el1][el2].hentStatusTegn(), end="")
            print("")

    def oppdatering(self):
        levendetildod = []
        dodtillevende = []
        for rad in range(self._rader):
            for kol in range(self._kolonner):
                celle = self._rutenett[rad][kol]
                naboer = self.finnNabo(rad,kol)
                teller = 0
                for x in naboer:
                    if x.erLevende() == True:
                        teller += 1

                if teller < 2 or teller > 3:
                    levendetildod.append(celle)
                if teller == 3:
                    dodtillevende.append(celle)

        for el1 in levendetildod:
            el1.settDoed()

        for el2 in dodtillevende:
            el2.settLevende()

        self._generasjonsnummer += 1

    def genNr(self):
        return self._generasjonsnummer

    def finnAntallLevende(self):
        levende = 0
        for rad in range(self._rader):
            for kol in range(self._kolonner):
                celle = self._rutenett[rad][kol].erLevende()
                if celle == True:
                    levende += 1
        return levende

    def _generer(self):
        for rad in range(self._rader):
            for kol in range(self._kolonner):
                random = randint(0,3)
                if random == 3:
                    self._rutenett[rad][kol].settLevende()

    def finnNabo(self, rad, kolonner):
        naboListe = []
        for row in range(-1,2):
            for kol in range(-1,2):
                naboRad = rad + row
                naboKol = kolonner + kol
                gyldig = True
                if naboRad == rad and naboKol == kolonner:
                    gyldig = False
                if naboRad >= self._rader-1 or naboRad < 0:
                    gyldig = False
                if naboKol >= self._kolonner-1 or naboKol < 0:
                    gyldig = False
                if gyldig == True: #kan også skrive if gyldig:
                    naboListe.append(self._rutenett[naboRad][naboKol])
        return naboListe
