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
        DoedtilLevende = [] #tom liste for døde celler som skal bli levende
        LevendetilDoed = [] #motsatte av det jeg skrev over

        rad = -1 #starter rad på -1, slik at den er på null når den blir plusset med en lenger ned
        kol = -1 #starter kol på -1, samme grunn som over
        for cell in self._rutenett: #sjekker hver objekt innenfor rutenettet
            rad += 1 #plusser rad med 1
            kol = -1 #gjør kolonne om til -1
            for i in cell: #for hver verdi innenfor cell
                LN = 0#tom verdi for levende naboer
                DN = 0#tom verdi for døde naboer
                kol += 1#plusser kolonne med 1
                CellLiv = i.erLevende()#sjekker om cellen er levende
                Nx = self.finnNabo(rad,kol)#verdi for hvor mange naboer som er rundt vellen
                for j in Nx:#for hver nabo ved cellen
                    if j != None: #om det er naboer...
                        if j.erLevende() == True:#ser om de er levende
                            LN += 1#øker levende nabo liste med 1
                        elif j.erLevende() == False:#om de er døde
                            DN += 1#øker død naboliste med 1
                if CellLiv == True:#hvis cellen er levende
                    if LN < 2 or LN >3:#og det er mindre enn 2, eller mere enn 3 naboer
                        LevendetilDoed.append(i) #som skal den bli sendt til lista for celler som skal dø
                elif CellLiv == False:#om cellen er død
                    if LN == 3:#men har 3 levende naboer
                        DoedtilLevende.append(i) #så skal den bli sendt til lista av celler som lever

        for Lcell in LevendetilDoed:#for hver verdi i lista
            Lcell.settDoed()#skal gå gjennom metoden for å død
        for Dcell in DoedtilLevende: #for hver døde celle i lista
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


""" kode som jeg brukte tidligere (funker også, men den over var mye mindre)
        if rad-1 <= -1:
            n1 = None
            n2 = None
            n3 = None

        else:
            if kolonne-1 <= -1:
                n1 = None
            else:
                n1 = self._rutenett[rad-1][kolonne-1]

            n2 = self._rutenett[rad-1][kolonne-1]

            if kolonne+1 > self._kolonner-1:
                n3 = None
            else:
                n3 = self._rutenett[rad-1][kolonne+1]

        if kolonne -1 <= -1:
            n4 = None
        else:
            n4 = self._rutenett[rad][kolonne-1]

        if kolonne+1 > self._kolonner-1:
            n5 = None
        else:
            n5 = self._rutenett[rad][kolonne+1]

        if rad+1 > self._rader-1:
            n6 = None
            n7 = None
            n8 = None

        else:
                if kolonne-1 <= -1:
                    n6 = None
                else:
                    n6 = self._rutenett[rad+1][kolonne-1]

                n7 = self._rutenett[rad+1][kolonne]

                if kolonne +1 > self._kolonner-1:
                    n8 = None
                else:
                    n8 = self._rutenett[rad+1][kolonne+1]

        naboliste.append(n1)
        naboliste.append(n2)
        naboliste.append(n3)
        naboliste.append(n4)
        naboliste.append(n5)
        naboliste.append(n6)
        naboliste.append(n7)
        naboliste.append(n8)
        return naboliste
"""
