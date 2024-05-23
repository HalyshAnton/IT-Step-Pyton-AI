from sqlalchemy import create_engine, MetaData, func, and_, or_
from sqlalchemy.orm import sessionmaker
import json


with open('config.json', 'r') as f:
    data = json.load(f)
    db_user = data['user']  # postgres
    db_password = data['password']

db_url = f'postgresql+pg8000://{db_user}:{db_password}@localhost:5432/hospital'
engine = create_engine(db_url)

metadata = MetaData()
metadata.reflect(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()


docs = metadata.tables['doctors']
specs = metadata.tables['specializations']
docsspecs = metadata.tables['doctorsspecializations']


def report_doctor_specializations():
    result = session.query(docs.c.name.label('doctorname'),
                           docs.c.surname,
                           specs.c.specialization_name) \
             .join(docsspecs, docsspecs.c.doctor_id == docs.c.id) \
             .join(specs, docsspecs.c.specialization_id == specs.c.id).all()

    if result:
        for row in result:
            print(f"{row.doctorname} {row.surname} with specialization {row.specialization_name}")

    # and - &
    # or - |
    # (name == 'hjk') & (salary > 20)

def report_doctors_salary_not_on_vacation():
    pass


def report_wards_depatment():
    pass


def repor_donation_of_last_mounth():
    pass


def report_departaments_donation():
    pass


while True:
    print("1. Вивести повні імена лікарів та їх спеціалізації")
    print("2. Вивести прізвища та зарплати лікарів, які не перебувають у відпустці")
    print("3. Вивести назви палат, які знаходяться у певному відділенні;")
    print("4. Вивести усі пожертвування за вказаний місяць у вигляді: відділення, спонсор, сума пожертвування, дата пожертвування;")
    print("5. Вивести назви відділень без повторень, які спонсоруються певною компанією.")

    print("0. Вийти")
    choice = input("Оберіть опцію: ")

    if choice == "1":
        report_doctor_specializations()
    elif choice == "2":
        report_doctors_salary_not_on_vacation()
    elif choice == "3":
        report_wards_depatment()
    elif choice == "4":
        repor_donation_of_last_mounth()
    elif choice == "5":
        report_departaments_donation()

    elif choice == "0":
        break
    else:
        print("Невірний вибір. Будь ласка, оберіть знову.")

# Закриваємо сесію
session.close()

