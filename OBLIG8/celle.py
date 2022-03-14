class Celle:#ny metode for celle
    def __init__(self):#konstruktøren
        self._status = "doed" #starter alltid med at cellen er doed

    def settDoed(self):#ny metode for settDoed
        self._status = "doed" #dreper cellen

    def settLevende(self): #ny metode settLevende
        self._status = "levende" #gjenoppliver cellen

    def erLevende(self): #ny metode for å se om cellen er levende
        if self._status == "levende": #hvis status er levende
            return True #returner sann
        return False #hvis ikke, fortsett og returner falsk

    def hentStatusTegn(self):#henter tegn for symbolet når den skal tegnes
        if self._status == "levende": #hvis statusen er levende
            return " O " #returner " O "
        return " . " #hvis ikke, returner "."
