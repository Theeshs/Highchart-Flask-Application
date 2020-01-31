from .models import Students
from application import app
from config import Config
from flask import request, jsonify
from .models import Students, Marks, Subjects
from statistics import mean

config = Config()
from .hub import session

# dashboard routes
"""

"""


@app.route('/', methods=['GET'])
@app.route('/get-filter-data', methods=['GET'])
# @jwt_required
def dashboard():
    students = [{'id': student.StudentID, 'name': student.StudentName} for student in Students.query.all()]

    subjects = [{'id': subject.SubjectID, 'name': subject.Subject} for subject in Subjects.query.all()]

    # print(subjects)

    return jsonify({
        "subjects": subjects,
        "students": students
    })


@app.route('/get-marks')
def get_marks():
    student = request.args.get('student_id')
    subject = request.args.get('subject_id')
    year = request.args.get('year')
    grade = request.args.get('grade')
    maths = []
    science = []
    it = []
    music = []
    labels = []
    ylabes = []
    if student == 'all' and subject == 'all':
        # print('1')
        maths = [mark.Mark for mark in Marks.query.filter_by(SubID=1, CalenderYear=str(year), Grade=int(grade)).all()]
        science = [mark.Mark for mark in Marks.query.filter_by(SubID=2, CalenderYear=str(year), Grade=int(grade)).all()]
        it = [mark.Mark for mark in Marks.query.filter_by(SubID=3, CalenderYear=str(year), Grade=int(grade)).all()]
        music = [mark.Mark for mark in Marks.query.filter_by(SubID=4, CalenderYear=str(year), Grade=int(grade)).all()]
        labels = ['Maths', 'Science', 'IT', 'Music']
        ylabes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    if subject == 'all' and student != 'all':
        # print('2')
        maths = [mark.Mark for mark in
                 Marks.query.filter_by(StdID=int(student), SubID=1, CalenderYear=str(year), Grade=int(grade)).all()]
        science = [mark.Mark for mark in
                   Marks.query.filter_by(StdID=int(student), SubID=2, CalenderYear=str(year), Grade=int(grade)).all()]
        it = [mark.Mark for mark in
              Marks.query.filter_by(StdID=int(student), SubID=3, CalenderYear=str(year), Grade=int(grade)).all()]
        music = [mark.Mark for mark in
                 Marks.query.filter_by(StdID=int(student), SubID=4, CalenderYear=str(year), Grade=int(grade)).all()]
        labels = ['Maths', 'Science', 'IT', 'Music']
        ylabes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    if student == 'all' and subject != 'all':
        # print('here')
        # print('3')
        data = [mark.Mark for mark in
                Marks.query.filter_by(SubID=int(subject), CalenderYear=str(year), Grade=int(grade)).all()]

        if int(subject) == 1:
            maths = data

        if int(subject) == 2:
            science = data

        if int(subject) == 3:
            it = data

        if int(subject) == 4:
            music = data

    if student != 'all' and subject != 'all':
        # print('4')
        data = [mark.Mark for mark in
                Marks.query.filter_by(StdID=int(student), SubID=int(subject), CalenderYear=str(year),
                                      Grade=int(grade)).all()]
        if int(subject) == 1:
            maths = data

        if int(subject) == 2:
            science = data

        if int(subject) == 3:
            it = data

        if int(subject) == 4:
            music = data

    return jsonify({
        'maths': sorted(list(set(maths)), reverse=True)[3:8],
        'science': sorted(list(set(science)), reverse=True)[1:6],
        'it': sorted(list(set(it)), reverse=True)[:5],
        'music': sorted(list(set(music)), reverse=True)[4:9],
    })


@app.route('/get-marks-column')
def get_marks_columns():
    student = request.args.get('student_id')
    subject = request.args.get('subject_id')
    year = request.args.get('year')
    grade = request.args.get('grade')
    maths = []
    science = []
    it = []
    music = []

    return_array = []
    if student == 'all' and subject == 'all':
        # print('1')
        maths = [mark.Mark for mark in Marks.query.filter_by(SubID=1, CalenderYear=str(year), Grade=int(grade)).all()]
        science = [mark.Mark for mark in Marks.query.filter_by(SubID=2, CalenderYear=str(year), Grade=int(grade)).all()]
        it = [mark.Mark for mark in Marks.query.filter_by(SubID=3, CalenderYear=str(year), Grade=int(grade)).all()]
        music = [mark.Mark for mark in Marks.query.filter_by(SubID=4, CalenderYear=str(year), Grade=int(grade)).all()]

        return_array.append(max(maths))
        return_array.append(max(science))
        return_array.append(max(it))
        return_array.append(max(music))
    if subject == 'all' and student != 'all':
        maths = [mark.Mark for mark in
                 Marks.query.filter_by(StdID=int(student), SubID=1, CalenderYear=str(year), Grade=int(grade)).all()]
        science = [mark.Mark for mark in
                   Marks.query.filter_by(StdID=int(student), SubID=2, CalenderYear=str(year), Grade=int(grade)).all()]
        it = [mark.Mark for mark in
              Marks.query.filter_by(StdID=int(student), SubID=3, CalenderYear=str(year), Grade=int(grade)).all()]
        music = [mark.Mark for mark in
                 Marks.query.filter_by(StdID=int(student), SubID=4, CalenderYear=str(year), Grade=int(grade)).all()]
        labels = ['Maths', 'Science', 'IT', 'Music']
        ylabes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

        return_array.append(max(maths))
        return_array.append(max(science))
        return_array.append(max(it))
        return_array.append(max(music))

    if student == 'all' and subject != 'all':
        # print('3')
        data = [mark.Mark for mark in
                Marks.query.filter_by(SubID=int(subject), CalenderYear=str(year), Grade=int(grade)).all()]

        if int(subject) == 1:
            maths = data

            if len(maths) != 0:
                return_array.append(max(maths))

        if int(subject) == 2:
            science = data

            if len(science) != 0:
                return_array.append(0)
                return_array.append(max(science))

        if int(subject) == 3:
            it = data

            if len(it) != 0:
                return_array.append(0)
                return_array.append(0)
                return_array.append(max(it))

        if int(subject) == 4:
            music = data

            if len(music) != 0:
                return_array.append(0)
                return_array.append(0)
                return_array.append(0)
                return_array.append(max(music))

    if student != 'all' and subject != 'all':
        # print('4')

        data = [mark.Mark for mark in
                Marks.query.filter_by(StdID=int(student), SubID=int(subject), CalenderYear=str(year),
                                      Grade=int(grade)).all()]
        # print(data)
        if int(subject) == 1:
            maths = data
            if len(maths) != 0:
                return_array.append(max(maths))

        if int(subject) == 2:
            science = data
            if len(science) != 0:
                return_array.append(0)
                return_array.append(max(science))
                return_array.append(0)
                return_array.append(0)

        if int(subject) == 3:
            it = data
            if len(it) != 0:
                return_array.append(0)
                return_array.append(0)
                return_array.append(max(it))
                return_array.append(0)

        if int(subject) == 4:
            music = data
            if len(music) != 0:
                return_array.append(0)
                return_array.append(0)
                return_array.append(0)
                return_array.append(max(music))
    # print(return_array)
    # exit()
    return jsonify({
        'data': return_array,
        'average': [average(maths), average(science), average(it), average(music)]

    })


@app.route('/all_sub_student_sem_1')
def get_all_sub_student_sem_1():
    student_id = int(request.args.get('student_id'))

    maths_sem1 = sorted(list(
        set([mark.Mark for mark in Marks.query.filter_by(StdID=int(student_id), SubID=1, Semester="Semester 1")])))[
                 -11:]
    science_sem1 = sorted(list(
        set([mark.Mark for mark in Marks.query.filter_by(StdID=int(student_id), SubID=2, Semester="Semester 1")])))[
                   2:13]
    it_sem1 = sorted(list(
        set([mark.Mark for mark in Marks.query.filter_by(StdID=int(student_id), SubID=3, Semester="Semester 1")])))[
              1:12]
    music_sem1 = sorted(
        list(set([mark.Mark for mark in Marks.query.filter_by(StdID=int(student_id), SubID=4, Semester="Semester 1")])),
        reverse=True)[-11:]

    return jsonify({
        'maths': maths_sem1,
        'science': science_sem1,
        'it': it_sem1,
        'music': music_sem1

    })


@app.route('/all_sub_student_sem_2')
def get_all_sub_student_sem_2():
    student_id = int(request.args.get('student_id'))

    maths_sem2 = sorted(list(
        set([mark.Mark for mark in Marks.query.filter_by(StdID=int(student_id), SubID=1, Semester="Semester 1")])))[
                 2:13]
    science_sem2 = sorted(list(
        set([mark.Mark for mark in Marks.query.filter_by(StdID=int(student_id), SubID=2, Semester="Semester 1")])))[
                   -11:]
    it_sem2 = sorted(list(
        set([mark.Mark for mark in Marks.query.filter_by(StdID=int(student_id), SubID=3, Semester="Semester 1")])))[
              -11:]
    music_sem2 = sorted(
        list(set([mark.Mark for mark in Marks.query.filter_by(StdID=int(student_id), SubID=4, Semester="Semester 1")])),
        reverse=True)[1:12]

    return jsonify({
        'maths': maths_sem2,
        'science': science_sem2,
        'it': it_sem2,
        'music': music_sem2

    })


def average(array):
    try:
        return round(sum(array) / len(array), 2)
    except Exception as e:
        # print(array)
        return 0
