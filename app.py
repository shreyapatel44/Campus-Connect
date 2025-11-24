import os
from flask import Flask, render_template, redirect, url_for, flash, request
from config import Config
from models import db, Club, Event, Membership, Registration
from forms import ClubForm, EventForm, RegistrationForm
from datetime import datetime

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # ensure instance folder exists
    os.makedirs(os.path.join(app.root_path, 'instance'), exist_ok=True)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    @app.route('/')
    def index():
        clubs = Club.query.order_by(Club.created_at.desc()).all()
        events = Event.query.order_by(Event.start_time).limit(6).all()
        return render_template('index.html', clubs=clubs, events=events)

    # Clubs CRUD
    @app.route('/clubs')
    def clubs_list():
        clubs = Club.query.order_by(Club.name).all()
        return render_template('clubs.html', clubs=clubs)

    @app.route('/club/new', methods=['GET','POST'])
    def club_create():
        form = ClubForm()
        if form.validate_on_submit():
            club = Club(name=form.name.data.strip(), description=form.description.data.strip() if form.description.data else None)
            db.session.add(club)
            db.session.commit()
            flash('Club created', 'success')
            return redirect(url_for('clubs_list'))
        return render_template('club_form.html', form=form)

    @app.route('/club/<int:club_id>')
    def club_detail(club_id):
        club = Club.query.get_or_404(club_id)
        return render_template('club_detail.html', club=club)

    @app.route('/club/<int:club_id>/edit', methods=['GET','POST'])
    def club_edit(club_id):
        club = Club.query.get_or_404(club_id)
        form = ClubForm(obj=club)
        if form.validate_on_submit():
            club.name = form.name.data.strip()
            club.description = form.description.data.strip() if form.description.data else None
            db.session.commit()
            flash('Club updated', 'success')
            return redirect(url_for('club_detail', club_id=club.id))
        return render_template('club_form.html', form=form, club=club)

    @app.route('/club/<int:club_id>/delete', methods=['POST'])
    def club_delete(club_id):
        club = Club.query.get_or_404(club_id)
        db.session.delete(club)
        db.session.commit()
        flash('Club deleted', 'info')
        return redirect(url_for('clubs_list'))

    # Events CRUD
    @app.route('/events')
    def events_list():
        events = Event.query.order_by(Event.start_time.desc()).all()
        return render_template('events.html', events=events)

    @app.route('/event/new', methods=['GET','POST'])
    def event_create():
        form = EventForm()
        # populate clubs choices
        form.club_id.choices = [(c.id, c.name) for c in Club.query.order_by(Club.name).all()]
        if form.validate_on_submit():
            start = form.parse_dt(form.start_time.data)
            end = form.parse_dt(form.end_time.data)
            event = Event(title=form.title.data.strip(),
                          description=form.description.data.strip() if form.description.data else None,
                          location=form.location.data.strip() if form.location.data else None,
                          start_time=start,
                          end_time=end,
                          capacity=form.capacity.data or 0,
                          club_id=form.club_id.data or None)
            db.session.add(event)
            db.session.commit()
            flash('Event created', 'success')
            return redirect(url_for('events_list'))
        return render_template('event_form.html', form=form)

    @app.route('/event/<int:event_id>')
    def event_detail(event_id):
        event = Event.query.get_or_404(event_id)
        reg_form = RegistrationForm()
        return render_template('event_detail.html', event=event, form=reg_form)

    @app.route('/event/<int:event_id>/edit', methods=['GET','POST'])
    def event_edit(event_id):
        event = Event.query.get_or_404(event_id)
        form = EventForm(obj=event)
        form.club_id.choices = [(c.id, c.name) for c in Club.query.order_by(Club.name).all()]
        # prefill string datetime fields
        if request.method == 'GET':
            form.start_time.data = event.start_time.strftime('%Y-%m-%d %H:%M') if event.start_time else ''
            form.end_time.data = event.end_time.strftime('%Y-%m-%d %H:%M') if event.end_time else ''
            form.club_id.data = event.club_id
        if form.validate_on_submit():
            event.title = form.title.data.strip()
            event.description = form.description.data.strip() if form.description.data else None
            event.location = form.location.data.strip() if form.location.data else None
            event.start_time = form.parse_dt(form.start_time.data)
            event.end_time = form.parse_dt(form.end_time.data)
            event.capacity = form.capacity.data or 0
            event.club_id = form.club_id.data or None
            db.session.commit()
            flash('Event updated', 'success')
            return redirect(url_for('event_detail', event_id=event.id))
        return render_template('event_form.html', form=form, event=event)

    @app.route('/event/<int:event_id>/delete', methods=['POST'])
    def event_delete(event_id):
        event = Event.query.get_or_404(event_id)
        db.session.delete(event)
        db.session.commit()
        flash('Event deleted', 'info')
        return redirect(url_for('events_list'))

    @app.route('/event/<int:event_id>/register', methods=['POST'])
    def event_register(event_id):
        event = Event.query.get_or_404(event_id)
        form = RegistrationForm()
        if form.validate_on_submit():
            if event.capacity and len(event.attendees) >= event.capacity:
                flash('Event is full', 'warning')
            else:
                reg = Registration(attendee_name=form.attendee_name.data.strip(), event=event)
                db.session.add(reg)
                db.session.commit()
                flash('Registered!', 'success')
        else:
            flash('Failed to register', 'danger')
        return redirect(url_for('event_detail', event_id=event.id))

    return app
