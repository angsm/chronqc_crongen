"""
@author: Shimin
"""

from datetime import date, timedelta
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json

import ConfigParser


def json_to_dict(config_json):
        '''
        Read the configuration json file
        :param config_json : Path of the configuration file
        '''
        json_data = open(config_json)
        data = json.loads(json_data.read())
        json_data.close()

        return data

def send_email(TO, FROM, TEXT, SUB, smtp_server, CC=[]):
        '''
        Creates a HTML-based email with clickable link and send it out using sendmail
        '''

        ## make text MIME format
        msg = MIMEMultipart('alternative')
        body = MIMEText(TEXT, 'html')
        msg.attach(body)

        ## for displaying only
        msg['Subject'] = SUB
        msg['From'] = ','.join(FROM)

        ## list to string, check if its a string first
        msg['To'] = ','.join(TO)
        msg['Cc'] = ','.join(CC)

        email_addresses = TO + CC

        ## real address that sendmail module use shld be a list
        ## Send the message via our own SMTP server, but don't include the envelope header
        s = smtplib.SMTP( smtp_server )
        s.sendmail(msg['from'], email_addresses, msg.as_string())
        s.quit()

def read_ini():

	## Read config and get default parameters
	sdir = op.dirname(op.abspath('__file__'))
	config_file = op.join(sdir, 'config', 'chronqc.conf')
	Config.read(config_file)
    	# [ignore_columns]
	ignore_columns = Config.get('ignore_columns', 'columns').split(',')
	ignore_columns = [s.strip() for s in ignore_columns]
	logger.info("Finished reading parameters from config file for generating chronqc db and json")

class custparser(ConfigParser.ConfigParser):
	def as_dict(self):

		d = dict(self._sections)
		for k in d:
			d[k] = dict(self._defaults, **d[k])
			d[k].pop('__name__', None)

		return d
