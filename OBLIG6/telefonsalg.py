score = {} #lager en tom dict
lesinn = open("salgstall.txt", "r") #åpner og leser hva som er inni salgstall.txt

def innlesing(filnavn): #lager en ny prosedyre som har parameteret filnavn
    for ord in lesinn: #for løkke som går gjennom variabelen lesinn
        splitta = ord.split(" ") #splitter det som er inni text filen
        navn = splitta[0] #lager variable basert på første ord i linja
        salg = int(splitta[1]) #lager variabel basert på andre ord i linja
        score[navn]=salg #gjør variabel navn om til key og salg om til value
    return score #returnerer dict

def maanedensSalgsperson(ordbok): #lager ny prosedyre, bruker ordbok som parameter
    supersalg = max(ordbok.values()) #supersalg sjekker etter den største verdien
    supersalgsperson = max(ordbok, key = ordbok.get) #så ser den etter hvilken key verdien hører til
    print("personen som solgte mest var ", supersalgsperson, " som solgte ", supersalg) #printer ut hvem det var som solgte mest, og hvor mye de solgte

def totaltAntallSalg(ordbok): #lager ny prosedyre, bruker ordbok som parameter
    summen = sum(ordbok.values()) #summen er sum av alle verdiene
    return summen #summen blir returnert

def gjennomsnittSalg(ordbok): #lager ny prosedyre, med en parameter
    summen = sum(ordbok.values()) #summen er sum av alle verdiene
    gj = summen/len(ordbok.values()) #gj er gjennomsnittet av alle summene. (sum delt på lengden av dict)
    return gj #returnerer gjennomsnittet

def antallSelgere(ordbok): #ny prosedyre med ordbok som parameter
    antallpersoner = len(ordbok) #ny variabel som er det samme som lengden av ordboka
    return antallpersoner #returnerer verdien av variabelen

def hovedprogram(): #ny prosedyre som ikke tar imot parameter
    print(innlesing(lesinn)) #printer ut prosedyren innlesing med lesinn som parameter
    pers = antallSelgere(score) #lager ny variabel med resultatet av å kjøre prosedyren med score som variabel
    maanedensSalgsperson(score) #kjører prosedyren maanedensSalgsperson med score som variabel
    print("antall aktive selgere denne maaneden: ", pers) #printer ut str med pers
    print("totalt antall salg er ", totaltAntallSalg(score)) #printer ut hvor mange salg som var
    print("gjennomsnittelig salg per salgsperson: ", gjennomsnittSalg(score)) #printer ut gjennomsnittet

hovedprogram() #kaller programmet
