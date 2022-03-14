class fag:
    def __init__(self, navn, liste):
        self._navn = navn
        self._liste = []

    def leggTilStudent(self, student):
        self._liste.append(student)

    def hentAntallStudenter(self):
        return range(self._liste)

    def hentFagNavn(self):
        return self._navn

    def hentStudenterVedFag(self):
        print("fag: ", self._navn, "og her er studentene:")
        for i in self._liste:
            print i

class student:
    def __init__(self, navn):
        self._navn = navn
        self._fagliste = []

    def leggTilFag(self, fag):
        self._fagliste.append(fag)

    def hentAntallFag(self):
        return range(self._fagliste)

    def hentStudentNavn(self):
        return self._navn

    def skrivFagPaaStudent(self):
        print("studenten heter: ", self._navn)
        for i in self._liste:
            print(i)

def hovedprogram():
    student1
