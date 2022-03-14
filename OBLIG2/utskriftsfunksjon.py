#oppgave 1a
navn=input("hva heter du?\n")#\n er her for å ha linjeskifte
hvor=input("hvor kommer du fra?\n")

hilsen=("hei " + navn + "! du er fra " + hvor + ".")

print(hilsen, "\n")

#oppgave 1b

def spoerreundersoekelse(): #prosedyre, om jeg bruker den igjen, så trenger jeg ikke å skrive koden på nytt igjen.
    navn=input("hva heter du?\n")
    hvor=input("hvor kommer du fra?\n")

    hilsen=("hei " + navn + "! du er fra " + hvor + ".")

    print(hilsen,"\n")

spoerreundersoekelse()
spoerreundersoekelse()
spoerreundersoekelse()
