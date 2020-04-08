class ObservatieException(Exception):
    pass


class Verif:
    def __init__(self, repoExaminare):
        self.__repo = repoExaminare

    def validate(self, examinare):
        erori = []
        if self.__repo.read(examinare.getIdExaminare()) is None:
            erori.append("Nu exista aceasta examinare.")
        if examinare.getDescriere() == "":
            erori.append("Stringul descrierii trebuie sa fie nenul")
        try:
            p = int(examinare.getPenalizare())
        except ValueError:
            erori.append("Examinarera trebuie sa fie un numar intreg.")
        if erori:
            raise ObservatieException(erori)
