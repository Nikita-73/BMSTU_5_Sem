from operator import itemgetter


class Emp:
    """Музыкант"""

    def __init__(self, id, fio, sal, dep_id):
        self.id = id
        self.fio = fio
        self.sal = sal
        self.dep_id = dep_id


class Dep:
    """Оркестр"""

    def __init__(self, id, name):
        self.id = id
        self.name = name


class EmpDep:
    """
    'Музыкант оркестр' для реализации
    связи многие-ко-многим
    """

    def __init__(self, dep_id, emp_id):
        self.dep_id = dep_id
        self.emp_id = emp_id


# Оркестры
deps = [
    Dep(1, 'симфонический оркестр'),
    Dep(2, 'эстрадный оркестр'),
    Dep(3, 'военный'),

    Dep(11, 'симфанический (другой) оркестр'),
    Dep(22, 'эстрадный (другой) оркестр'),
    Dep(33, '(другая) военный'),
]

# Музыканты
emps = [
    Emp(1, 'Артамонов', 25000, 1),
    Emp(2, 'Петров', 35000, 2),
    Emp(3, 'Иваненко', 45000, 3),
    Emp(4, 'Иванов', 35000, 3),
    Emp(5, 'Иванин', 25000, 3),
]

emps_deps = [
    EmpDep(1, 1),
    EmpDep(2, 2),
    EmpDep(3, 3),
    EmpDep(3, 4),
    EmpDep(3, 5),

    EmpDep(11, 1),
    EmpDep(22, 2),
    EmpDep(33, 3),
    EmpDep(33, 4),
    EmpDep(33, 5),
]


def main():
    """Основная функция"""

    # Соединение данных один-ко-многим
    one_to_many = [(e.fio, e.sal, d.name)
                   for d in deps
                   for e in emps
                   if e.dep_id == d.id]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(d.name, ed.dep_id, ed.emp_id)
                         for d in deps
                         for ed in emps_deps
                         if d.id == ed.dep_id]

    many_to_many = [(e.fio, e.sal, dep_name)
                    for dep_name, dep_id, emp_id in many_to_many_temp
                    for e in emps
                    if e.id == emp_id]

    print('\nЗадание E1')

    def taskone():
        b = []
        c = []
        for a in many_to_many:
            if "оркестр" in a[-1]:
                b.append(a[-1])
                c.append(a[0])
        print(b, '\n', c)

    taskone()

    print('\nЗадание E2')
    res_12_unsorted = []
    for d in deps:
        count = 0
        d_emps = list(filter(lambda i: i[2] == d.name, one_to_many))
        if len(d_emps) > 0:
            d_sals = [sal for _, sal, _ in d_emps]
            count += 1
            d_sals_sum = sum(d_sals)
            aver_sum = round(d_sals_sum / count, 2)

            res_12_unsorted.append((d.name, aver_sum))
    res_12 = sorted(res_12_unsorted, key=itemgetter(1))
    print(res_12)

    print('\nЗадание E3')

    for d in many_to_many:
        if d[0].find('А') == 0:
            a = []
            c = []
            a.append(d[0])
            c.append(d[-1])
            print(a, c)


if __name__ == '__main__':
    main()
