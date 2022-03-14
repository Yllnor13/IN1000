"""
lag ei ordbok med land og hovedstader
Gjør det slikt at brukeren kan skrive inn navnet på landet, og få ut navnet på presidenten/statsministeren
om de ikke vet hvilke land som er på lista, la dem skrive inn noe som forteller dem dette
gi brukeren evnen til å legge til et nytt land
om de skriver navnet galt, så skal programmet fortelle det til dem
"""

#løsning
land_og_statsoverhode={"Japan":"Shinzo Abe", "USA":"Donald John Trump", "Norge":"Kong Harald", "Frankrike":"Emmanuel Macron", "England":"Boris Johnson"}#navn på land og statsoverhoder

def statsoverhodesjekk():#lagde en def av denne slik at den kan bli brukt på nytt
    land=input("\nskriv navnet på landet her, husk stor forbokstav (USA er forkortet)\n\nskriv 1 om du vil legge til ny land\n\nOm du vil se alle land og statsoverhoder på lista, skriv 2. (du blir sendt tilbake til begynnelsen igjen)\n\nOm du vil avslutte, skriv AVSLUTT\n")#gir brukeren mange valg her.
    if land in land_og_statsoverhode:#sjekker om det landet de skrev er på lista
        print("statsoverhodet er ", land_og_statsoverhode[land])
        proevpaanytt()
    elif land=="1":#om de vil legge til land
        leggtilland()
    elif land=="2":#om de vil se hvilke land som er her allerede
        print(land_og_statsoverhode)
        proevpaanytt()
    elif land=="AVSLUTT":#om de vil gå ut av programmet
        print("porgrammet er avsluttet, start den på nytt om du vil :)")#siden det ikke er noe mer som skal kjøre etter dette, så avslutter programmet seg
    else:
        print("\nlandet ditt er ikke på lista, prøv igjen, enten det, eller så skrev du navnet ikke riktig\n")
        proevpaanytt()

def proevpaanytt():#lagde en def av denne slik at den kan bli brukt på nytt
    statsoverhodesjekk()

def leggtilland():#lagde en def av denne slik at den kan bli brukt på nytt
    nyland=str(input("\nskriv inn navnet på landet her\n"))#de skriver inn et nytt land her
    land_og_statsoverhode[nyland]=str(input("\nskriv in nanvet på statsoverhodet her\n\n etter dette så vil du bli spurt om å skrive inn land igjen.\n"))#og så lenker de statsoverhodet til det landet de skrev her
    statsoverhodesjekk()#går tilbake til steg en for brukeren

statsoverhodesjekk()#må bare bruke en prosedyre, siden de andre prosedyrene er inni denne også
