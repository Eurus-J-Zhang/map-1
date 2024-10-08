from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Data(db.Model):
    number = db.Column(db.Integer, primary_key=True)
    id= db.Column(db.String(20))
    gender=db.Column(db.String(1))
    age = db.Column(db.Integer)

    emo1_competence = db.Column(db.Integer)
    emo1_joy = db.Column(db.Integer)
    emo1_pride = db.Column(db.Integer)
    emo1_boredom = db.Column(db.Integer)
    emo1_irritation = db.Column(db.Integer)
    emo1_anxiety = db.Column(db.Integer)
    emo1_shame = db.Column(db.Integer)

    emo2_competence = db.Column(db.Integer)
    emo2_joy = db.Column(db.Integer)
    emo2_pride = db.Column(db.Integer)
    emo2_boredom = db.Column(db.Integer)
    emo2_irritation = db.Column(db.Integer)
    emo2_anxiety = db.Column(db.Integer)
    emo2_shame = db.Column(db.Integer)

    feedback1 = db.Column(db.Text)
    feedback2 = db.Column(db.Text)
    station_track = db.Column(db.String(500), nullable=True)
    result = db.Column(db.String(50), nullable=True)

    reflection = db.Column(db.Text)

