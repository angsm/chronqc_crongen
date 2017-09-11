"""
@author: Shimin
"""

import subprocess
import sys
from shutil import copyfile
from subprocess import Popen, PIPE, STDOUT
import time
import os
import chronqc
import datetime
import argparse
import logging
import time

import traceback

try:
	from . import utils
except:
	import utils

try:
    import configparser
    config = configparser.SafeConfigParser()  # ver. < 3.0
except:
    import ConfigParser
    config = ConfigParser.SafeConfigParser()


def check_argument():
	'''
	Checks this script's input and provide prompt if necessary
	'''

	global args

	parser = argparse.ArgumentParser(description='Generates ChronQC commands and runs them. An email will be sent when generation complates')
	parser.add_argument('config_file', help='path of configuration file for this script', type=str)

	args = parser.parse_args()

def call_plots( to_directory ):
	'''
	Make a directory, run the ChronQC plot(s) command and copy them over
	'''

	logging.info( 'START generating ChronQC commands:')

        json_dict = config_data["chronqc_json"]
        json_dir = config_data["chronqc"]["json_dir"]
        database = config_data["chronqc"]["database"]
	cmd = config_data["chronqc"]["gen_cmd"]

        os.system("sudo mkdir " +  to_directory)

        ## generate and call Chronqc commands
        link_dict = {}
        for j in json_dict.keys():
                command = cmd % ( database, json_dir + "/" + json_dict[j], j.upper())
		print command

                logging.info( command )

		try:
               		p = Popen(command, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
                	data = p.communicate()[0].split()

		except:
			logging.error( 'Plot could not be generated, check json file path' )		

                filename = (data[-1].split("/"))[-1]

                ## copy to directory
                os.system("sudo cp " + data[-1] + " " + to_directory + "/" + filename)
                link_dict[j] = filename

	return link_dict

def compose_mail( link_dict, display_directory ):
	'''
	Gathers email required variables, compose mail and send it out
	'''

        notice_pts = ""

        to_arr = config_data["email"]["to"].split(',')
        from_arr = config_data["email"]["host"].split(',')
        test_arr = config_data["email"]["test"].split(',')
        subject = config_data["template"]["subject"] % ( datetime.datetime.now().strftime("%B %Y"))

        email_notice = config_data["template"]["notice"]
	smtp_server = config_data["email"]["smtp_server"]

        for l in link_dict.keys():
                windows_link = display_directory + "\\" + link_dict[l]
                notice_pts += "<br><b>" + l.upper() + "</b>:</br>"
                notice_pts += "<a href=" + windows_link  + ">" + windows_link  + "</a>\n\n"

        email_notice = email_notice % (notice_pts)
        utils.send_email(test_arr, from_arr, email_notice, subject, smtp_server)

def main():

	global config_data
	now = time.strftime("%c")

	## parse input arguement
	check_argument()

        # read the config file
	file = utils.custparser()
	file.read(args.config_file)
	config_data = file.as_dict()

	logging.basicConfig(filename=config_data["path"]["log"],level=logging.DEBUG)
	logging.info('STARTED crongen on %s' % now)

	try:

		## set output directory and directory to be displayed in email
		to_directory = config_data["iomanip"]["destination"]
		display_directory = ""
		if ("dislay_destination" in config_data["iomanip"].keys()) and (config_data["iomanip"]["display_destination"] != "")  :
			display_directory = config_data["iomanip"]["display_destination"]
		else:
			display_directory = to_directory

		## make directory for this month
		curr_date = time.strftime("%d_%b_%Y")
		to_directory += "/" + curr_date
		display_directory += "/" + curr_date
	
		link_dict = call_plots( to_directory )

		## email users
		compose_mail( link_dict, display_directory )

	except Exception:
		print traceback.format_exc()
		logging.error(traceback.format_exc())

	logging.info('FINISHED without issues\n\n')

if __name__ == "__main__":
	main()
