from celle import Celle #importerer klassen Celle
from random import randint #importerer randint

class Spillebrett: #oppretter ny class
    def __init__(self, rader, kolonner): #konstruktør med rader og kolonner som parameter
        self._rader = rader #ny variabel, self._rader
        self._kolonner = kolonner #ny variabel, self._kolonner
        self._rutenett = [] #ny variabel, self._rutenett (som er en tom liste)
        self._gen = 0 #ny variabel, self._gen
        for i in range(self._rader): #for løkke som skal fylle rutenett med en liste
            Xrader = [] #tom liste som skal settes inn i rutenett
                        #for å sette inn rader
            self._rutenett.append(Xrader) #setter xrader i rutenett
            for j in range(self._kolonner): #for løkke for å fylle radene
                self._rutenett[i].append(Celle()) #fylle radene med celler
        self._generer() #kjører generer metoden

    def tegnBrett(self): #ny metode for å tegne brettet
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        #for å dytte det som var tidligere ut av terminalens syn
        for i in self._rutenett: #for hver liste i rutenett
            print("\n") #skal skilles med linjeskifte
            for j in i: #for hver verdi i listene
                print(j.hentStatusTegn(), end="") #printer ut enten " O " eller " . " om den er levende eller ikke
        print("\n Generasjon: ", self._gen, end=" - ") #viser hvor mange generasjoner som har gått

    def oppdatering(self): #metode for oppdateringskoden
        DoedtilLevende = [] #tom liste for doede celler som skal bli levende
        LevendetilDoed = [] #motsatte av det jeg skrev over

        rad = -1 #setter rad til -1 slik at den starter på 0 senere
        for celler in self._rutenett: #sjekker hver cellerad i rutenettet
            rad +=1 #plusser rad med 1 slik at den går gjennom hver rad
            kol =- 1 #starter kolonne på -1 for samme grunn som rad
            for cell in celler: #sjekker hver celle i kolonnene
                kol += 1 #plusser den med en slik at den går gjennom hver kolonne
                cellLiv=cell.erLevende() #sjekker om cellen er levende
                LevendeNabo = 0 #har verdien for levende naboer her
                Naboer = self.finnNabo(rad, kol) #lager en liste for hvor mange naboer som er i nærheten av self i den nåværende raden og kolonnen
                for nabo in Naboer: #for hver nabo i kolonnen
                    if nabo.erLevende() == True: #om naboen er levende...
                        LevendeNabo += 1 #øk levende nabo med 1
                if cellLiv == True: #hvis cellen lever
                    if LevendeNabo < 2 or LevendeNabo > 3: #sjekk om det er mindre enn 2 eller mer enn 3 naboer
                        LevendetilDoed.append(cell) #om den har for mange eller for lite naboer, så blir den sendt til lista for cellene som skal dø
                if  cellLiv == False: #om cellen er doed
                    if LevendeNabo == 3: #og den har 3 levende naboer
                        DoedtilLevende.append(cell) #så skal den doede cellen bli blassert i denne lista
        for Lcell in LevendetilDoed:#for hver verdi i lista
            Lcell.settDoed()#skal gå gjennom metoden for å doed
        for Dcell in DoedtilLevende: #for hver doede celle i lista
            Dcell.settLevende() #skal gå gjennom metoden for å leve
        self._gen += 1 #øker generasjonsnummeret med 1

    def finnAntallLevende(self):#ny metode for å finne antall levende celler i rutenettet
        antLeve = 0 #setter verdien til 0
        for celler in self._rutenett: #for hver liste i rutenettet
            for cell in celler:#for hver objekt i lista
                if cell.erLevende() == True: #hvis den lever
                    antLeve += 1 #legg den til i lista
        return antLeve #returner antall levende


    def _generer(self): #ny metode for å generere rutenettet
        for i in self._rutenett: #for hver liste i rutenett
            for j in i: #for hver objekt i i
                random = randint(0,2) #ny verdi som blir enten 0, 1 eller 2
                if random == 0: #hvis random blir 0
                    j.settLevende() #så skal den cellen bli levende

    def finnNabo(self, rad, kol): #ny metode for å finne naboer, tar imot rad og kol som parametre
        naboliste = []#tom nabolite
        for i in range(-1,2): #for verdi mellom -1 og 2
            for j in range(-1,2): #for verdi mellom -1 og 2
                naborad = rad + i #går til nabo verdi
                nabokol = kol + j #går til nabo verdi
                gyldig = True #sjekker om det er en gyldig nabo (altså, at den finnes)
                if naborad == rad and nabokol == kol: #sjekker om den ser på segselv
                    gyldig = False #man er ikke en gyldig nabo til seg selv
                if naborad >= self._rader or naborad < 0: #om naboraden er større er rutenettet eller mindre enn null
                    gyldig = False#så finnes det ikke nabo der
                if nabokol >= self._kolonner or nabokol < 0:#samme som over, men for kolonner
                    gyldig = False
                if gyldig: #ellers, så er det en gydlig nabo
                    naboliste.append(self._rutenett[naborad][nabokol])#legger posisjonene inn i en liste
        return naboliste #returnerer lista
