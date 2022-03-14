"""
egen oppgave
lag et system som lar brukeren legge til navna på vennene sine og når de har bursdag
"""

venner = int(input("hvor mange venner har du? (skriv som tall)\n"))

vennerzero = 0

venneliste = {}

while vennerzero < venner:
    leggtilvenn = input("skriv navnet til vennen din her\n")
    venneliste[leggtilvenn] = input("skriv bursdagen dems her (dd/mm/yyyy)\n")
    vennerzero += 1

for w,i in venneliste.items():#w og i tar plassen til key og value
    print("din venn, ", w, ", har bursdag den ", i) #skriver ut keyen og verdien som tilhører den
