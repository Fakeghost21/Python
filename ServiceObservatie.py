class ServiceObservatie:
    def __init__(self, repository, validator, repoExaminare):
        """
        desc:initializeaza clasa Service1
        :param repository:
        """
        self.__repo = repository
        self.__valid = validator
        self.__repoExaminari = repoExaminare

    def create1(self, obj):
        """

        :param obj:
        :return:
        """
        self.__valid.validate(obj)
        self.__repo.create(obj)

    def update1(self, obj):
        c = self.__repo.read(obj.getId())
        self.__repo.update(obj)

    def delete1(self, id_obj):
        clients = self.__repo.read()
        for client in clients:
            if client.getId() == id_obj:
                self.__repo.delete(id_obj)
                return

    def read1(self, obj_id=None):
        return self.__repo.read(obj_id)

    def examinareRezultat(self, idExaminare):
        observatii = self.__repo.read()
        penalizari = 0
        for o in observatii:
            if idExaminare == o.getIdExaminare():
                penalizari += int(o.getPenalizare())
        return penalizari

    def creazaDictionar(self):
        examinari = self.__repoExaminari.read()
        dict = {}
        for e in examinari:
            dict[e.getId()] = self.examinareRezultat(e.getId())
        return dict

    def ordonare(self):
        examinari = self.__repoExaminari.read()
        dict = self.creazaDictionar()
        matrice = sorted(dict.items(), key=lambda a: (a[1], a[0]))
        nr = len(list(dict.keys()))
        listaExaminari = []
        for i in range(nr):
            listaExaminari.append(matrice[i][0])
        return listaExaminari

    def setExaminatori(self):
        setul = []
        examinari = self.__repoExaminari.read()
        for e in examinari:
            if e.getNumeExaminator() not in set(setul):
                setul.append(e.getNumeExaminator())
        return setul

    def dictionarPenalizari(self):
        dict = {}
        listaExaminatori = self.setExaminatori()
        examinari = self.__repoExaminari.read()
        for e in listaExaminatori:
            dict[e] = 0
            for ex in examinari:
                if ex.getNumeExaminator() == e:
                    dict[e] += self.examinareRezultat(ex.getId())
        return dict

    def ordonare2(self):
        dict = self.dictionarPenalizari()
        matrice = sorted(dict.items(), key=lambda tractor: (tractor[1], tractor[0]), reverse=True)
        nr = len(list(dict.keys()))
        listaTractoare = []
        for i in range(nr):
            listaTractoare.append(matrice[i][0])
        return listaTractoare




