from hund import Hund #importerer klassen Hund fra hund.py

def hovedprogram(): #starter ny prosedyre
    hund1 = Hund(10, 4) #lager ny variabel og setter inn vekt og alder inn i klassen

    hund1.spring() #kjører spring prosedyren med informasjonen fra hund1
    hund1.spis(2)#kjører spis prosedyren med informasjonen fra hund1, og metthet øker med 2
    hund1.vektogalder()#kjører vektogalder prosedyren med informasjonen fra hund1

    hund1.spis(2)#kjører spis prosedyren med informasjonen fra hund1, og metthet øker med 2 igjen.
    hund1.spring()#kjører spring prosedyren med informasjonen fra hund1
    hund1.vektogalder()#kjører vektogalder prosedyren med informasjonen fra hund1

hovedprogram() #kaller prosedyren
