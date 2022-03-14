from motorsykkel import Motorsykkel #importerer klassen Motorsykkel fra filen motorsykkel

def hovedprogram(): #lager definisjon av hovedprogram med ingen parametere
    motorsykkel1 = Motorsykkel("honda", "1993", 14578) #ny variabel som skaper en objekt av klassen Motorsykkel, med 3 argumenter
    motorsykkel2 = Motorsykkel("VW", "19933", 41353) #gjorde det samme som over
    motorsykkel3 = Motorsykkel("waKanda", "12993", 1293) #gjorde det samme som over

    motorsykkel1.skrivUt() #bruker skrivut prosedyren fra klassen Motorsykkel
    motorsykkel2.skrivUt() #samme som over
    motorsykkel3.skrivUt() #samme som over

    motorsykkel3.kjor(10) #kaller funksjon kjør, og bruker 10 som parameter
    print (motorsykkel3.hentKilometerstand()) #printer ut hva resultatet av funksjonen "hentKilometerstand" blir med motorsykkel3 variabelen

hovedprogram() #kaller prosedyren "hovedprogramm" som er definert over
