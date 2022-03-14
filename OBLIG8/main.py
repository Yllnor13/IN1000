from spillebrett import Spillebrett #importerer spillebrett

def main(): #ny metode main
    rader = input("Skriv rader i tall: ") #lar brukeren skrive inn rader
    kolonner = input("Skriv kolonner i tall: ") #lar brukeren skrive inn kolonner
    spill = Spillebrett(int(rader),int(kolonner)) #lagrer et brett med så mange rader og kolonner som ble spesifisert
    spill.tegnBrett() #tegner det
    print("Antall levende celler: ", spill.finnAntallLevende())# viser hvor mange levende celler som er der
    ans = "" #ny svar verdi
    while ans != "q":#om brukeren ikke skriver 1 for quit
        if ans == "":#hvis bruker klikker enter
            spill.oppdatering()#oppdaterer brettet
            spill.tegnBrett() #tegner brettet
            print("Antall levende celler: ", spill.finnAntallLevende())# viser hvor mange levende celler som er der
        if ans != "q" and ans != "":#om de ikke skriver q eller enter
            print("ugyldig")#ugyldig svar
        ans = input("vil du avslutte? isåfall, press q. Ellers, press enter \n")#spør om de vil fortstteette
    # starte hovedprogrammet

main()#kaller programmet
