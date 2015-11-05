from . import main
from ..models import Host, Job
from ..utils import abort, Command
from flask import render_template
from flask.ext.login import login_required
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, ValidationError
from wtforms.validators import Required, Regexp, IPAddress

class AdhocForm(Form):
	ip = StringField("ipaddress", validators=[Required(), IPAddress()])
	module = StringField("module", validators=[Required()])
	arguments = StringField("arguments", validators=[Required()])

	def validate_ip(self, field):
		if Host.query.filter_by(ip=field.data).first():
			raise ValidationError('host does not exist! Please check again!')

	def validate_module(self, field):
		pass

@main.route('/')
def index():
	return render_template('index.html')

@main.route('/ad_hoc', methods=['GET','POST'])
def ad_hoc():
	form = AdhocForm()
	if form.validate_on_submit():
		ip = form.ip.data
		module = form.module.data
		arguments = form.arguments.data
		command = "ansible {ip} -m {shell} -a \"{arguments}\"".format({"ip":ip, "module":module, "arguments":arguments})
		host = Host.query.filter_by(ip=ip).first()
		job = Job(content=command, host_id=host.id)
		Command.execute(command)
		return redirect(url_for('get_job', id=job.id))
	return render_template('ad_hoc.html', form=form)

@main.route('/job')
def get_job_list():
	jobs = Job.query.order_by("exec_start").all()
	return render_template('get_job_list.html', jobs=jobs)

@main.route('/job/<id>')
def get_job(id):
	job = Job.query.filter_by(id=id).first()
	if job is None:
		abort(404)
	return render_template('get_job.html', job=job)

@main.route('/host')
def get_host_list():
	hosts = Host.query.order_by("ip").all()
	return render_template('get_host_list.html', hosts=hosts)

@main.route('/host/<id>')
def get_host(id):
	host = Host.query.filter_by(id=id).first()
	if host is None:
		abort(404)
	return render_template('get_job.html', host=host)