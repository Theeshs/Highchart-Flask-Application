from .models import Students, Subjects, Marks
import random
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import json, csv
from datetime import datetime
import threading

Base = declarative_base()
conn_string = 'postgresql+psycopg2://postgres:admin@localhost:5432/assessment'
engine = create_engine(conn_string)
Base.metadata.create_all(engine)  # here we create all tables
Session = sessionmaker(bind=engine)
session = Session()


def execute_adding_data():
    # print("here")
    start = datetime.now()
    print("Started at", start)
    student_count = Marks.query.count()
    if student_count > 0:
        print('yes')
    else:
        # exit()
        student_names = ['Theesh', 'Supun', 'John', 'Doe', 'Nuwan', 'Chanux', 'Ratta', 'Chanaka', 'Raj', 'Hirantha',
                         'Janith', 'Nilaksha', 'Janidu', 'Prashanth', 'Mena', 'Melani', 'Harsha', 'Vishwa', 'Sajani',
                         'Hansika']

        subjects = ["Maths", "Science", "IT", "Music"]

        for student in student_names:
            new_student = Students(student)
            new_student.add()
        print('students_added')

        for subject in subjects:
            new_subject = Subjects(subject)
            new_subject.add()
        print('subjects added')

        student_ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        subject_ids = [1, 2, 3, 4]
        grade = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        marks = [23, 56, 13, 85, 84, 90, 99, 00, 78, 55, 86, 70, 34, 88]

        years = ["2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020"]

        semester = ['Semester 1', 'Semester 2']

        new_records = []
        counter = 1
        for i in range(0, 10000000):
            new_records.append(Marks(
                random.choice(student_ids),
                random.choice(subject_ids),
                random.choice(semester),
                random.choice(years),
                random.choice(marks),
                random.choice(grade)
            ))

            if len(new_records) % 1000000. == 0:
                print('added ' + str(counter))
                session.bulk_save_objects(new_records)
                session.commit()
                new_records = []
                counter += 1
        print('over')
        ended = datetime.now()
        print('Ended at', ended)

        print('Total time taken', ended - start)
