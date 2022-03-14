måned1=int(input("skriv nummer på måned her (bruk tall)\n"))
dato1=int(input("skriv dato her\n"))

måned2=int(input("skriv nummer på måned her (bruk tall)\n"))
dato2=int(input("skriv dato her\n"))

if måned1<måned2:
    print("riktig rekkefølge")
elif måned1==måned2:
    if dato1<dato2:
        print("riktig rekkefølge")
    elif dato1==dato2:
        print("samme dato")
else: print("feil rekkefølge")

"""
Brukte måned og dato som variabler, fordi det er greit å huske.
gjorde variablene om til int, slik at folk ikke skrev navna på månedene istedenfor datoen
"""
