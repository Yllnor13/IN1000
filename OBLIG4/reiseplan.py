steder = []

print("skriv sted du vil dra til her")

for i in range(5):
    steder.append(input("sted "))

plagg = []

print("skriv klesplagg du vil ha med her")

for i in range(5):
    plagg.append(input("klesplagg "))

avreisedatoer = []

print("skriv avreidedatoene her (yy/mm/dd)")

for i in range(5):
    avreisedatoer.append(input("avreisedato "))

reise = []

for i in range(5):
    reise.append([steder[i], plagg[i], avreisedatoer[i]])

print("her er stedene du valgte")

for i in range(5):#for løkke som sjekker tall i listen, og printer ut summen av talla
    print("sted: ", reise[i][0])
    print("klesplagg: ", reise[i][1])
    print("dato", reise[i][2])

print("har du lyst til å mixe og matche noen av reiseplanene?\n isåfall, så skal du skrive hvilket nummer reisen tilhører til her (1-5)")

i1=int(input("skriv første tallet her(1-5)"))-1
i2=int(input("skriv andre tallet her(1-5)"))-1

print("Element ", reise[i1][i2])
