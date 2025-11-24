from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
db = SQLAlchemy()

class Club(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False, unique=True)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    members = db.relationship('Membership', back_populates='club', cascade='all, delete-orphan')
    events = db.relationship('Event', back_populates='club', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<Club {self.name}>"

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140), nullable=False)
    description = db.Column(db.Text)
    location = db.Column(db.String(200))
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    capacity = db.Column(db.Integer, default=0)
    club_id = db.Column(db.Integer, db.ForeignKey('club.id'))
    club = db.relationship('Club', back_populates='events')
    attendees = db.relationship('Registration', back_populates='event', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<Event {self.title}>\"

class Membership(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(50), default='member')
    club_id = db.Column(db.Integer, db.ForeignKey('club.id'))
    club = db.relationship('Club', back_populates='members')

    def __repr__(self):
        return f"<Membership {self.user_name} of club {self.club_id}>\"

class Registration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    attendee_name = db.Column(db.String(120), nullable=False)
    registered_at = db.Column(db.DateTime, default=datetime.utcnow)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'))
    event = db.relationship('Event', back_populates='attendees')

    def __repr__(self):
        return f"<Registration {self.attendee_name} for event {self.event_id}>\"
