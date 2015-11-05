from . import db
from datetime import datetime

class Host(db.Model):
	__tablename__ = 'hosts'
	id = db.Column(db.Integer, primary_key=True)
	ip = db.Column(db.String(15), primary_key=True)
	alias = db.Column(db.String(20))
	description = db.Column(db.Text())
	status = db.Column(db.Integer)
	enabled =  db.Column(db.Boolean)
	jobs = db.relationship('Job', backref='host', lazy='dynamic')

class Job(db.Model):
	__tablename__ = 'jobs'
	id = db.Column(db.Integer, primary_key=True)
	content = db.Column(db.Text())
	result = db.Column(db.Text())
	status = db.Column(db.Integer)
	exec_start = db.Column(db.DateTime(), default=datetime.utcnow)
	exec_end = db.Column(db.DateTime(), default=None)
	host_id = db.Column(db.Integer, db.ForeignKey('hosts.id'))






