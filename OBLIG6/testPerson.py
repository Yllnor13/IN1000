from person import Person #importerer klasse fra annen fil

def hovedprogram(): #starter def som heter hovedprogram
    body1 = Person("Jonas", 16, 80) #registrerer person gjennom klassen

    body1.informasjon() #kjører informasjons prosedyren skrevet i person.py, men bruker inforen fra body1

    body1.kalk(30) #kjører kalk prosedyren fra person.py, men bruker infoen fra body1

    body1.spis(2) #kjører spis prosedyren fra person.py, men bruker infoen fra body1

    body1.brenn(3) #kjører brenn prosedyren fra person.py, men bruker infoen fra body1

hovedprogram() #kaller koden
