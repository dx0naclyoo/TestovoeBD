import datetime
from sys import argv

from faker import Faker

from ServiceEmployee import EmployeeDirectory
from data import POSTGRES_DATABASE, POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_HOST, POSTGRES_PORT
from models import Employee

try:
    param = argv[1]
    database = EmployeeDirectory(dbname=POSTGRES_DATABASE,
                                 user=POSTGRES_USER,
                                 password=POSTGRES_PASSWORD,
                                 host=POSTGRES_HOST,
                                 port=POSTGRES_PORT)

    match int(param):
        case 1:
            print("Выполняется 1 метод")
            database.create_table_employee()
        case 2:
            print("Выполняется 2 метод")
            full_name = argv[2]
            birthday_date = argv[3]
            gender = argv[4]

            employee = Employee(fullname=full_name, birth_date=birthday_date, gender=gender)

            database.add_employee(employee)

        case 3:
            print("Выполняется 3 метод")
            uniq_employees = database.fetch_unique_employees()
            count_uniq = 0
            for row in uniq_employees:
                print(row)
                count_uniq += 1
            print("Всего уникальных пользователей: ", count_uniq)
        case 4:
            print("Выполняется 4 метод")
            fake = Faker()

            data = [(fake.name(),
                     fake.date_of_birth(),
                     fake.random_element(elements=('Male', 'Female'))) for x in range(10000)]
            database.add_list_employees(data)

        case 5:
            print("Выполняется 5 метод")
            employees = database.fetch_f_male()
            count = 0
            start = datetime.datetime.now()
            for empl in employees:
                print(empl)
                count += 1
            finish = datetime.datetime.now() - start
            print("Число сотрудников F Male", count)
            print("Время выполнянеия ", finish)

except Exception as ex:
    print("Возникла ошибка", ex)
    raise ex
