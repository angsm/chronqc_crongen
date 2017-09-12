ChronQC CronGen
=================
Automates the generation of one or more ChronQC plots, using a .ini input file as configuration. An email notification will be send out to users once generation has complete. A log file will also be generated to record the ChronQC commands that has been used.

Requirements
============
* `ChronQC 1.0.4 and above <https://github.com/nilesh-tawari/ChronQC>`_
* `ChronQC json files <http://chronqc.readthedocs.io/en/latest/plots/plot_options.html>`_
* Python 2.6 and above
* crontab `configuration <https://crontab.guru/>`_


Execute it
==========

To run it, execute the command below:

.. code-block:: shell
 
 python chronqc_crongen.py <.ini configuration file>

..

To run it on crontab scheduler (etc. every month):

.. code-block:: 
 0 0 1 * * python chronqc_crongen.py <.ini configuration file>
..

.ini Configuration File
=======================

The headers and parameters shown below are mandatory.   

*For [iomanip] section, "DISPLAY_DESTINATION" can be used when transfering the plots to a mounted Windows drive from a Linux system. This is so that the email notification that shows up on a Window user's computer will be valid and understandable by Windows explorer.*  

.. code-block:: ini

 [path] 
 LOG = <log file location> 

 [email] 
 TO = <email 1>, <email 2>
 HOST = <from email address> 
 CC = <cc email 1>, <cc email 2>
 SMTP_SERVER = <smpt server ip address>

 [template] 
 SUBJECT = [ Monthly QC statistics ] Month of %s 
 NOTICE = <br>Dear Users,</br> <p><br>ChronQC plots are ready for viewing in:  <br>%s</br></br></p><br>Thank you.</br><br>*** This is an  automated mail, please do not reply ***</br> 

 [chronqc] 
 JSON_DIR = ./CONFIG/JSON 
 DATABASE = ./DATABASE/statsplot.sqlite 
 GEN_CMD = chronqc plot -db %s -json %s -panel %s -f 
 
 [chronqc_json] 
 <panel name 1> = <panel 1>.json 
 <panel name 2> = <panel 2>.json 
 
 [iomanip] 
 DESTINATION = <ChronQC output directory> 
 DISPLAY_DESTINATION = <directory displayed in email>

..
