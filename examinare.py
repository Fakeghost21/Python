from Domain.entity import *


class Examinare(Entity):
    def __init__(self, theId, numeElev, numeExaminator):
        super().__init__(theId)
        self.__elev = numeElev
        self.__examinator = numeExaminator

    def getNumeElev(self):
        return self.__elev

    def getNumeExaminator(self):
        return self.__examinator

    def __str__(self):
        return "{},{},{}".format(
            self.getId(),
            self.__elev,
            self.__examinator
        )