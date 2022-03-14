class Sang: #lager klassen
    def __init__(self, tittel, artist): #starter konstruktøren med 3 parametre
        self._tittel=tittel #gjør self._tittel om til parameter tittel
        self._artist=artist # gjør self._artist om til parameter artist

    def spill(self): #metode spill som refererer bare til seg selv
        print("tittel: ", self._tittel,"\nartist: ", self._artist) #printer ut hva tittel og artist til sangen er

    def sjekkArtist(self, navn): #ny metode sjekkartist med segselv og navn som parametre
        for i in navn.split(): #splitter opp det personen skriver
            for j in self._artist.split(): #splitter opp navna som er allerede i sangen
                if i.lower() == j.lower(): #sammenligner navna for å se om de er der (lowerer teksten slik at man kan skrive med stor og liten bokstav)
                    return True #returnerer True
        return False #hvis det over ikke funker, returnerer false

    def sjekkTittel(self, tittel): #metode sjekkTittel med seg selv og tittel som parametre
        if tittel.lower() == self._tittel.lower():#sammenligner tittel skrevet og titler som er i sangen
            return True #returnerer true om det over finker
        return False #returnerer false om det ikke funker

    def sjekkArtistogTittel(self, artist, tittel): #ny metode for å sjekke navn på artist og tittel. self, artist of tittel som parameter
        if artist.lower() in self._artist.lower() and tittel.lower() == self._tittel.lower(): #hvis artist som er skrevet er lik artist i sangen, og tittel skrevet er lik tittel i sangen
            return True #så skal den returnere true
        return False#returnerer false hvis ikke
