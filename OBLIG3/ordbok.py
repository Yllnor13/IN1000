varer={"melk":14.90, "brød":24.90, "yoghurt":12.90, "pizza":39.90}#ordboka

print(varer)#printer ut alt som er inni ordboka

varer_lagt_til=0#ny variabel som jeg kan bruke på en while løkke

while varer_lagt_til<2:#while løkke slik at koden kjører bare 2 ganger
    leggtilvare=str(input("skriv den nye varen her\n"))
    varer[leggtilvare]=float(input("legg til pris til den nye varen her\n"))
    varer_lagt_til+=1#legger til +1 verdi på variabelen slik at while løkka ikke går foralltid

print(varer)
#videokilde for koden jeg brukte https://www.youtube.com/watch?v=kiTh-YgzzPo
