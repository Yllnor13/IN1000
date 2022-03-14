def antall_bokstaver(ord):#prosedyre som skal bli kjørt igjen
    return len(str(ord)) #len sjekker hvor mange symboler som er i verdiern.


brukerinputord=str(input("skriv et ord her\n"))#ber brukeren om å skrive inn et ord her

ordlengde=antall_bokstaver(brukerinputord)#kjører prosedyren med verdien fra hva brukeren skrev

print("det er ", ordlengde, " bokstaver i det ordet du skrev")#tar resultatet fra

antall_bokstaver(brukerinputord)#prosedyren blir kjørt, og den vil vise hvor mange symboler det er i brukerens ord


tekst = str(input("skriv in en setning her."))#starten av del oppgave 2, brukeren skal skrive inn en setning her

setning = {}#her lager jeg bare en tom dict

splittetsetning = tekst.rstrip().split()#her blir ordene i setningen splittet basert på om det er mellomrom mellom dem

for word in splittetsetning:#her sjekker den for hvert ord i den splittede setningen som ble lagt
    if word in setning:#her ser den om det er et ord som blir brukt flere ganger
        setning[word] += 1 #og den blir brukt mer enn en gang, så er det den verdien den hadde +1 som blir lagret
    else:#hvis det bare er ett av det ordet, så kjører denne koden
        setning[word] = 1#her så gir den keyen verdien 1, fordi den kommer bare opp en gang

def antall_bokstaver_ver2(ord): #ny prosedyre, ser akkurat ut som den forrige, har bare forandret på hva slags tekst som blir skrevet
    print("og ordet inneholder ", len(str(ord)), " bokstaver")#sjekk forklaringa på forrige prosedyre


for w,i in setning.items():#w og i tar plassen til key og value
    print("ordet ", w, " kommer opp ", i, " ganger") #skriver ut keyen og verdien som tilhører den
    antall_bokstaver_ver2(w)#kjører prosedyren jeg har lagd over


#kilde som hjalp veldig, https://www.youtube.com/watch?v=lLbyEYjU55A&t=517s
