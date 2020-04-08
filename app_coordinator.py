from UI.Console import *
from Repository.GenericRepo import *
from Service.ServiceExaminare import *
from Service.ServiceObservatie import *


def main():
    repoExaminare = GenericFileRepository("Examinare.txt")
    repoObservatie = GenericFileRepository("Observatie.txt")
    serviceExaminare = ServiceExaminare(repoExaminare)
    validatorObservatie = Verif(repoExaminare)
    serviceObservatie = ServiceObservatie(repoObservatie, validatorObservatie, repoExaminare)
    dr = Console(serviceExaminare, serviceObservatie)
    dr.run_console()


main()
