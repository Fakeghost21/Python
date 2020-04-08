from Domain.examinare import *
from Domain.observatie import *
from Domain.observatieValidator import *


class Console:

    def __init__(self, examinareService, observatieService):
        self.__examinare_service = examinareService
        self.__observatie_service = observatieService

    def __show_menu(self):
        print('1. Adaugare examinare.')
        print("a1. Afisare examinare")
        print('2. Adaugare observatie')
        print("a2. Afisare observatie")
        print('3. Afisare examinarile cu rezultatele.')
        print("4. Afișarea tuturor examinărilor ordonate crescător după cea mai mare penalizare existentă")
        print("5. Afișarea examinatorilor ordonați descrescător după suma penalizărilor acordate")
        print('x. Exit')

    def run_console(self):
        while True:
            self.__show_menu()
            op = input("Optiune")
            if op == "1":
                self.__handle_addExaminare()
            elif op == "2":
                self.__handle_addObservatie()
            elif op == "3":
                self.__examinariRezultat()
            elif op == "a1":
                self.__show_list(self.__examinare_service.read1())
            elif op == "a2":
                self.__show_list2(self.__observatie_service.read1())
            elif op == "4":
                self.__show_list3(self.__observatie_service.ordonare())
                #self.__observatie_service.creazaDictionar()
            elif op == "5":
                print(self.__observatie_service.ordonare2())
            elif op == "x":
                break

    def __handle_addExaminare(self):
        try:
            id = input('ID-ul: ')
            numeElev = input('Numele elevului: ')
            numeExaminator = input('Numele examinatorului: ')
            c = Examinare(id, numeElev, numeExaminator)
            self.__examinare_service.create1(c)
            print('Examinarea a fost adaugata!')
        except ValueError as ve:
            print('Erori:')
            for error in ve.args[0]:
                print(error)

    def __handle_addObservatie(self):
        try:
            id = input('ID-ul: ')
            isExaminare = input('Id examinare: ')
            descriere = input('Descriere: ')
            penalizare = input("Penalizare: ")
            r = Observatie(id, isExaminare, descriere, penalizare)
            self.__observatie_service.create1(r)
            print('Atacul a fost adaugat!')
        except ObservatieException as e:
            print(e)
        except ValueError as ve:
            print('Erori:')
            for error in ve.args[0]:
                print(error)

    def __show_list(self, objects):
        for obj in objects:
            print(obj)

    def __show_list2(self, objects):
        for obj in objects:
            c = self.__examinare_service.read1(obj.getIdExaminare())
            print(c.getNumeElev(), obj, sep=" ")

    def __show_list3(self, objects):
        examinari = self.__examinare_service.read1()
        for obj in objects:
            for e in examinari:
                if e.getId() == obj:
                    print(e)

    def __examinariRezultat(self):
        examinari = self.__examinare_service.read1()
        for e in examinari:
            admis = "Respins"
            if self.__observatie_service.examinareRezultat(e.getId()) < 50:
                admis = "Admis"
            print(e, admis, sep=" : ")


