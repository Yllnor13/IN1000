class Hund: #oppretter klassen Hund
    def __init__(self, alder, vekt): #starter konstruktør for hunden, med alder og vekt som variabel
        self._alder=alder #argumentet for alder blir om til self._alder
        self._vekt=vekt #argumentet for vekt blir om til self._vekt
        metthet=10 #la til metthet her slik som den er fordi oppgaven ville at den alltid skulle være 10
        self._metthet=metthet #self._metthet får verdien til metthet, som er 10

    def vektogalder(self): #ny instansmetode som bruker bare self som variabel
        print("hunden veier ", self._vekt, " og er ", self._alder, " år gammel.") #printer ut vekt og alder av hunden med tekst slik at man forstår hva tallene står for.

    def spring(self): #ny instansmetode med self som parameter.
        self._metthet -= 1 #senker metthet med -1 hver gang koden kjører
        if self._metthet < 5: #if kode for å se om metthet er mindre enn 5
            self._vekt -= 1 #senker vekta med 1 om metthet er mindre enn 5

    def spis(self, tall): #nytt instansmetode med self og tall som parameter
        self._metthet += tall # mettheten skal øke med tall
        if self._metthet > 7: # om mettheten er større enn 7, så skal følgende kode kjøres
            self._vekt += 1 # vekta skal øke med en om metthet er større enn 7
