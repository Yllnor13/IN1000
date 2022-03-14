def addisjon(x,y):  #funksjon for addisjon blir definert
    return x + y    #den skal returnere verdien av x og y addert

def subtraksjon(x,y):   #funksjonen for sutraksjon blir definert
    return x-y          #den skal returnere verdien av x subtrahert med y

def divisjon(x,y):  #funksjon for divisjon blir definert
    return x/y      #den skal returnere verdien av x dividert med y

nysum = addisjon(3, 4)  #ny verdi blir definert, og den kaller på addisjons funksjonen

print(nysum)    #printer ut returnverdien

assert (addisjon(1,1)==2), "svaret skal bli 2"      #den asserter at addisjon mellom 1 og 1 blir 2
assert (addisjon(1,-1)==0), "svaret skal bli 0"     #den asserter at addisjon mellom 1 og -1 blir 0
assert (addisjon(-2,-2)==-4), "svaret skal bli -4"  #den asserter at addisjon mellom -2 og -2 blir -4

assert (subtraksjon(4,3)==1), "svaret skal bli 1"   #den asserter at subtraksjon mellom 4 og 3 er 1
assert (subtraksjon(-3,-2)==-1), "svaret skal bli -1"   #den asserter at subtraksjon mellom -3 og -2 er 1
assert (subtraksjon(-6,1)==-7), "svaret skal bli -7"    #den asserter at subtraksjon mellom -6 og 1 er -7

assert (divisjon(4,2)==2), "svaret skal bli 2"  #den asserter at divisjon mellom 4 og 2 er 2
assert (divisjon(-4,-2)==2), "svaret skal bli 2"    #den asserter at divisjon mellom -4 og -2 er 2
assert (divisjon(-4,2)==-2), "svaret skal bli -2"   #den asserter at divisjon mellom -4 og 2 er -2

def tommerTilCm(antallTommer):  #definerer funksjonen "tommerTilCm" med "antallTommer" som parameter
    assert (antallTommer)>0, "verdien skal være mer enn 0 cm lang"  #her asserterer den at parameteret ikke er under 0
    return antallTommer * 2.54  #her regner den ut hva antall tommer blir til Cm

print(tommerTilCm(2))   #her kaller jeg funksjonen via print.
                        #jeg printer ut hva tommerTilCm blir dersom parameteret er lik 2

def skrivBeregninger(): #definerer ny funksjon, "skrivBeregninger"
    tall1=float(input("skriv inn tall 1: "))    #brukerens input her blir verdien i variabel "tall1"
    tall2=float(input("skriv inn tall 2: "))    #brukerens input her blir verdien i variabel "tall2"

    print("\nresutlatet av summering: ", addisjon(tall1,tall2), "\n")   #den printer ut hva resultatet blir av addisjon mellom "tall1" og "tall2"
    print("resultatet av subtraksjon: ", subtraksjon(tall1,tall2), "\n")    #den printer ut hva resultatet blir mellom subtraksjon av "tall1" og "tall2"
    print("resultat av divisjon: ", divisjon(tall1,tall2), "\n")    #den printer ut hva divisjon blir mellom tall1 og tall2

    print("\nkonvertering fra tommer til cm")   #her printer jeg ut stringen "nkonvertering fra tommer til cm"
    tommer=float(input("skriv inn et tall: "))  #her lar jeg brukeren skrive inn hvor mange tommer de vil konvertere
    print("sultat", tommerTilCm(tommer))    #her kaller jeg inn funksjonen med det brukeren skrev som parameter

skrivBeregninger()  #her kaller jeg inn funksjonen "skrivBeregninger"
