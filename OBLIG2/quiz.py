"""
lag en flervalgsquiz hvor brukeren kan velge mellom flere svar.
Brukeren skal kunne forstå hva de skal gjøre for å komme seg fram til riktig svar.
Spørsmålene kan være hva du vil at de skal være.
gi hint til de vanskelige spørsmålene som ikke kan bli søkt opp på google.
"""

def spm1(): #gjorde denne om til prosedyre slik at jeg kunne bruke den igjen.
    print("skriv tallet bak svaret du vil velge")
    svar=int(input("Hva heter jeg, personen som skrev oppgaven?\n1. George Washington\n2. Erik Jensen\n3. Yllnor Rukovci\n4. hint\n")) #skrev at den bare kan bli brukt en gang, vil ikke at brukeren skal kunne bare stå stille på samme spm
    if svar==3:
        print("Riktig svar!")
    else:
        print("feil svar")

print("skriv tallet bak svaret du vil velge")
svar=int(input("Hva heter jeg, personen som skrev oppgaven?\n1. George Washington\n2. Erik Jensen\n3. Yllnor Rukovci\n4. hint (kan bare bli brukt en gang)\n"))

if svar==4:
    print("initialene mine er Y og R")
    spm1()
elif svar==3:
    print("Riktig svar!")
else:
    print("feil svar")

def spm2(): #gjorde denne om til prosedyre slik at jeg kunne bruke den igjen.
    print("skriv tallet bak svaret du vil velge")
    svar=int(input("Hvilket Universitet er det beste i Norge?\n1. Universitetet i Oslo\n2. Oslomet\n3. alle andre universiteter i byen\n4. hint (kan bare bli brukt en gang)\n")) #skrev at den bare kan bli brukt en gang, vil ikke at brukeren skal kunne bare stå stille på samme spm
    if svar==1: #satte if kode her slik at jeg kunne stille spørsmålet igjen om en person valgte svar 4 for å få hint
        print("Riktig svar!")
    else:
        print("feil svar")

spm2()

if svar==4:
    print("skolens logo har universitas osloensis som en del av logoen")
    spm2()
elif svar==1:
    print("Riktig svar!")
else:
    print("feil svar")

print("skriv tallet bak svaret du vil velge")
svar=int(input("hva er 2 pluss 1\n1. 3\n2. 3\n3. 2\n"))

if svar==2:
    print("Riktig svar!")
elif svar==1:
    print("Riktig svar!")
else:
    print("feil svar")

print("skriv tallet bak svaret du vil velge")
svar=int(input("hva heter USAs 45-te president?\n1. Barack Obama\n2. Donald Trump\n3. Yllnor Rukovci\n"))

if svar==2:
    print("Riktig svar!")
else:
    print("feil svar")
