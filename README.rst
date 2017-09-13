ChronQC CronGen
=================
Can be used for the automation of generation of ChronQC plots from a ChronQC statistics database (chronqc.stats.sqlite) or custom SQLite database. The database must contain information on sequencing runs, run dates, and laboratory or bioinformatics QC metrics. The settings for generating ChronQC plot can be specified in a configuration file (.ini). An email notification will be send out to users once generation has complete. Generates a log event file as well, to record the ChronQC commands that has been used and its run date.

Edit the configuration file with the panel name and json file name to generate ChronQC plots.

.. contents:: **Table of Contents**


Requirements
============
* Python 2.6 and above
* `ChronQC 1.0.3 and above <https://github.com/nilesh-tawari/ChronQC>`_
* `ChronQC json file <http://chronqc.readthedocs.io/en/latest/plots/plot_options.html>`_
* crontab `configuration <https://crontab.guru/>`_

Execute it
==========

To run it, execute the command below:

.. code-block:: shell
 
 python chronqc_crongen.py <.ini configuration file>

..

To run it on crontab scheduler periodically (etc. every month):

.. code-block:: 
 0 0 1 * * python chronqc_crongen.py <.ini configuration file>
..

I / O
=====
INPUT: CronGen .ini Configuration File
--------------------------------------

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

OUTPUT: Dated folder
--------------------
A output folder named based on the date format: 'DD_MON_YYYY' will be created in the directory specified by "iomanip"'s DESTINATION tag in the .ini config file::

 [iomanip] 
 DESTINATION = <ChronQC output directory>
 
The output ChronQC HTML files are stored in this the folder.
