class Motorsykkel: #skaper klassen "Motorsykkel"
    def __init__(self, merke, registreringsnummer, kilometerstand): #konstruktør med merke, registreringsnummer og kilometerstand
        self._merke=str(merke) #self._merle blir om til det man skriver inn som argument for merke
        self._registreringsnummer=str(registreringsnummer) #self._registreringsnummer blir om til argumentet for registreringsnummer
        self._kilometerstand=int(kilometerstand) #self._kilometerstand blir om til det man skriver som argument for kilometerstand

    def kjor(self, kilometerstand): #instansmetode med kilometerstand som parameter
        self._kilometerstand = self._kilometerstand + kilometerstand #øker self._kilometerstand med hvor mange kilometer so mer lagt til

    def hentKilometerstand(self): #instansmetode som ikke har noen parametere (utenom self)
        return self._kilometerstand #returnerer verdien av self._kilometerstand

    def skrivUt(self): #instansmetode som har self som parameter
        print(self._registreringsnummer, self._merke, self._kilometerstand) #printer ut registreringsnummer, merke og kilometerstand
