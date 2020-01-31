from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Students(db.Model):
    __table_name__ = '__students__'
    StudentID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    StudentName = db.Column(db.String)
    StdRelation = db.relationship('Marks', backref='students', lazy=True)

    def __init__(self, StudentName):
        self.StudentName = StudentName

    def __repr__(self):
        return '<Students %r>' % self.StudentID

    def get_id(self):
        return str(self.StudentID)

    def add(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()


class Marks(db.Model):
    __table_name__ = '__marks__'
    MarkID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    StdID = db.Column(db.Integer, db.ForeignKey('students.StudentID', ondelete='CASCADE'))
    SubID = db.Column(db.Integer, db.ForeignKey('subjects.SubjectID', ondelete='CASCADE'))
    Semester = db.Column(db.String)
    CalenderYear = db.Column(db.String)
    Mark = db.Column(db.Integer)
    Grade = db.Column(db.Integer)

    def __init__(self,StdID, SubID, Semester, CalenderYear, Mark, Grade):
        self.StdID = StdID,
        self.SubID = SubID,
        self.Semester = Semester
        self.CalenderYear = CalenderYear
        self.Mark = Mark
        self.Grade = Grade

    def __repr__(self):
        return '<Marks %r>' % self.MarkID

    def get_id(self):
        return str(self.MarkID)

    def add(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def bulk_insert(self, obj):
        db.session.bulk_save_objects(obj)

    def flush(self):
        db.session.flush()


class Subjects(db.Model):
    __table_name__ = '__subjects__'
    SubjectID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Subject = db.Column(db.String)
    SubRelation = db.relationship('Marks', backref='subjects', lazy=True)

    def __init__(self, Subject):
        self.Subject = Subject

    def __repr__(self):
        return '<Subjects %r>' % self.SubjectID

    def get_id(self):
        return str(self.SubjectID)

    def add(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()
