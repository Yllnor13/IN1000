#oppgave 3.1
beboer={"Johnathan Andersen":"yoghurt, egg, pølse", "Kari Nordmann":"brød, egg, pølse", "Mikael Yakson":"pepsi, ris, pizza"} #valgte tilfeldige navn og mat de spiste.

#oppgave 3.2

def beboersjekk(): #prosedyren
    navn_på_beboer=str(input("skriv hele navnet til beboeren her (husk stor forbokstar)\n"))#her skal brukeren skrive nanvet til beboeren. Minner dem også om stor forbokstav
    if navn_på_beboer in beboer:#sjekker om navnet de skrev er i ordboka
        print(beboer[navn_på_beboer])#den skriver ut bare informasjonen til beboeren som blir spurt etter
    else:#hvis ikke, så kjører koden her
        print("navnet er ikke i vårt system")

beboersjekk()#bruker prosedyren en gang, fordi oppgaven spør ikke om mer

#oppgave 3.3
"""
a, Føler at det beste hadde vært en vanlig liste, siden man skal bare ha liste med navn og ikke noe annet.
b, dict føler jeg hadde vært best her, siden man skal ha nøkkel (brukernavn), og antall poeng de fikk.
c, vanlig liste her og, siden det bare skal være navn.
d, hadde brukt mengde her om man skulle bare ha hva folk er allergisk mot. da kan man for eksempel sjekke hvor mange er det som er allergisk mot gluten (gjennom å sjekke len), så får man opp et tall av hvor mange som er allergiske mot det
Derimot, om man skal sjekke hva spesifikke personer er allergisk mot, så burde man ha ordbok, slik at man kan søke opp navnet, så få en liste med allergier.
"""
