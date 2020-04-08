from Domain.entity import *


class Observatie(Entity):
    def __init__(self, theId, idExaminare, descriere, penalizare):
        super().__init__(theId)
        self.__penalizare = penalizare
        self.__idExaminare = idExaminare
        self.__descriere = descriere

    def getIdExaminare(self):
        return self.__idExaminare

    def getDescriere(self):
        return self.__descriere

    def getPenalizare(self):
        return self.__penalizare

    def __str__(self):
        return "{},{},{},{}".format(
            self.getId(),
            self.__idExaminare,
            self.__descriere,
            self.__penalizare
        )
