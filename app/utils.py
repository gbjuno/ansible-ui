import logging

from flask import render_template
from subprocess import call

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(filename)s %(levelname)s %(message)s', datefmt='%a, %d %b %Y %H %M %S', filename='app.log', filemod='a')

class Command(object):

	def __init__(self):
		super(Command, self).__init__()

	@staticmethod
	def execute(command):
		call(command, shell=True)
		logging.info(command)

def abort(statusCode):
	return render_template('error/404.html')