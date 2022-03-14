def legg_inn_null_maal(lagliste):
    orbok = {}
    for lag in lagliste:
        orbok.update({lag:0})
    return orbok

print(legg_inn_null_maal(["brann", "molde"]))

def ekstraher_lagliste(fn):
    fil = open(fn, "r")
    lagliste = []
    for i in fil:
        split = i.split()
        lagliste.append(split[0])
        lagliste.append(split[1])
    return lagliste

print(ekstraher_lagliste("lesefil.txt"))

def gull(lagoversikt):
    for i in lagoversikt:
        lag = lagoversikt[i]


    if lagoversikt{0} > lagoversikt {3}:
        return lagoversikt{0}
    elif lagoversikt{1} < lagoversikt {3}:
        return lagoversikt [2]
    else:
        return "uavgjort"

print(gull({"Brann" : 2, "Molde" : 3}))

def minste(tall1, tall2, tall3):
    minstetall = tall1
    if tall2 < tall1:
        minstetall = tall2
    elif tall3 < tall2:
        minstetall = tall3
    else:
        return minstetall


class Meny:
    def __init__(self, ketNavn):
        self._katord={}
        for navn in katNavn:
            self._katord[navn] = self._leskategoriFil(fil)

    def hentredusert(self, innholdsstoffer):
        redmen = {}
        for katnavn in self._katord:
            okrettlist=self._katord[katnavn].hentOkRetter(innholdsstoffer)
            if len(okRetter) > 0:
                redmen[katnavn] = self._katord[katnavn]
        return redmen

class kunde:
    def __init__(selfm tlf, liste):
        self.tlfnr = tlf
        self.innholdstofferliste = liste

    def velgretter(self, menyObj):
        redmen = menyObj.hentredmen(self.innholdstofferliste)
        bestilling = []
        for k in kategorier.values():
            print(katnavn,redmen[katnavn])
            kundensvalg = input("hvilken kat?")
            if kundensvalg == "":
                bestilling.append(valg)
        return bestilling
