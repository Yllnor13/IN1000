"""
oppgaven er å lage en class av menneske hvor de kan registrere navn, alder og vekt i kilo.
brukeren skal kunne sjekke navn og alder, spise (og gå opp i vekt om de spiser mer enn de sulter)
brukenren skal også kunne brenne ned vekta si, og kalkulere fett i kilo etter å vite hvor mange prosent fett de har
"""

class Person: #starter klassekoden
    def __init__(self, navn, alder, vekt): #starter init for å definere klassen
        sult= 0 #sult starter på 0
        self._navn=str(navn) #navnet blir lagt inn
        self._alder=int(alder) #alder blir lagt inn
        self._sult=int(sult) #sulten blir lagt inn
        self._vekt=int(vekt) #vekta blir lagt inn

    def informasjon(self): #def som skal vise hva navn, alder og vekt er for den nye brukeren
        print("personen ", self._navn, " er ", self._alder, "år gammel, og de veier", self._vekt, (" kg")) #printer ut kombinasjon av str og objekter

    def brenn(self, sesjoner): #ny def som lar brukeren brenne kalorier
        self._sult += 5*sesjoner #treningen øker sulten og blir ganget med sesjoner
        if self._sult > 0: #om sulten er større en null, så skal koden under kjøre
            self._vekt -= 0.5 #vekta går ned med en halv kilo

    def kalk(self, prosent): #ny def for å kalkulere kilo fett
        fettprosent=self._vekt*(prosent/100) #gjør heltallet de skrev inn om til prosent.
        print("kroppen din inneholder", fettprosent, " kilo fett") #printer ut et svar som forteller brukeren hvor mange kilo fett de har

    def spis(self, porsjoner): #ny def som spør etter hvor mange porsjoner han spiser
        self._sult -= 3*porsjoner #sulten minger
        if self._sult < 0: #om sulten er mindre enn 0...
            self._vekt = self._vekt + int(porsjoner) * 0.5 #så skal vekta øke med en halv kilo
        print("du veier", self._vekt, " kg nå.") #så blir de fortalt om hvor mye de veier
