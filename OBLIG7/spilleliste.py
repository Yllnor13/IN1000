from sang import Sang #importerer Sang fra sang

class Spilleliste: #lager klasse
    def __init__(self, listenavn): #konstruktør metode med listenavn som parameter
        self._sanger = [] #self._sanger er en liste
        self._navn = listenavn #self._navn er parameter listenavn

    def lesFraFil(self, filnavn): #ny metode som har seg selv og filnavn som parametre
        fil = open(filnavn) #ny variabel som åpner hva en fil med samme navn som filnavn
        for laater in fil: #for løkke som går gjennom variabelen fil
            alleData = laater.strip().split(";") #variabel som er alle ordene i txt filen, splittet etter linje og ;
            sanger = Sang(alleData[0],alleData[1]) #ny variabel av Sang-klassen, hvor ord en erstatter tittel og ord 2 erstatter artist
            self._sanger.append(sanger) #appender variabelen sanger inn i lista
            print(laater) #printer ut alle laatene
        fil.close() #lukker igjen filen


    def leggTilSang(self, nySang): #lager ny metode hvor sang blir lagt til, parametre er segselv og nySang
        self._sanger.append(nySang) #appender (legger til ved slutten av lista) ny sang.

    def fjernSang(self, sang): #ny metode som skal fjerne sang
        self._sanger.remove(sang) #remover (fjerner sangen)

    def spillSang(self, sang): #ny metode med sang som parameter
        sang.spill() #utfører metoden spill fra Sang klassen med sangen man skriver i parameter

    def spillAlle(self): #ny metode som skal spille alle sanger med segselv som parameter
        for allesanger in self._sanger: #kjører koden under for hver sang i self._sanger
            allesanger.spill() #koden utfører metode spill fra klassen Sang, og printer ut sangen

    def finnSang(self, tittel): #ny metode for å finne sang med tittel som parameter
        for laater in self._sanger: #for hver laater in lista self._sanger
            if laater.sjekkTittel(tittel) is True: #hvis sjekktittel metoden returnerer true..
                return laater #skal den returnere laater
        return None #ellers returnerer den none

    def hentArtistUtvalg(self, artistnavn): #ny metode med artistnavn og self som parametre
        sangMedArtist = []#ny liste
        for laat in self._sanger:#for hver laat i lista self._sanger
            if laat.sjekkArtist(artistnavn) is True:#og om det laat returnerer true når metoden sjekkArtist blir brukt med et spesifikt navn
                sangMedArtist.append(laat) #så skal den appende sangen med det artist navne i lista
        return sangMedArtist #så returnerer den den nye lista som har alle sangene lagd av artisten
