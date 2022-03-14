def minFunksjon():
    for x in range(2):
        c = 2
        print(c)
        c += 1
        b = 10
        b += a
        print(b)
    return(b)

def hovedprogram():
    a = 42
    b = 0
    print(b)
    b = a
    a = minFunksjon()
    print(b)
    print(a)

hovedprogram()

"""
først, så blir funksjonen minFunksjon definert (uten parametre), og etter det, så blir hovedprogram definert (også uten parametre).
så blir prosedyren "hovedprogram" kalt.
variabelen a blir opprettet med verdien 42 inni prosedyren, så blir b opprettet som 0.
etter det, så blir variabelen b printet. deretter, så blir verdien til b erstattet med a.
det betyr at b blir lik 42.
a blir så om til hva minFunksjon blir.
minFunksjon oppretter en for løkke, hvor argumentet er x in range 2.
innenfor løkka, blir variabelen c, med verdien 2 definert. deretter blir c (som er 2) printet.
deretter blir verdien til c økt med, så c blir lik 3.
deretter blir variabelen b definert som 10.
deretter så blir b addert med a, som fører til en error, siden a ikke er definert innenfor løkka.
"""
