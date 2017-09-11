# ChronQC CronGen

## Requirements
- ChronQC
- Python 2.6 and above

## Description
Automates the generation of one or more ChronQC plots, using a .ini input file as configuration. An email notification will be send out to users once generation has complete. A log file will also be generated to record the ChronQC commands that has been used.

To run it, execute the command below:

```python 
python chronqc_crongen.py <.ini configuration file>
```

## .ini file sample format
The headers and parameters shown below are mandatory.   

For [iomanip] section, "DISPLAY_DESTINATION" can be used when transfering the plots to a mounted Windows drive from a Linux system. This is so that the email notification that shows up on a Window user's computer will be valid and understandable by Windows explorer.   

```
[path] 
LOG = <log file location> 

[email] 
TO = <email 1>, <email 2>
HOST = <from email address> 
CC = <cc email 1>, <cc email 2>
SMTP_SERVER = <smpt server ip address>

[template] 
SUBJECT = [ Monthly QC statistics ] Month of %s 
NOTICE = <br>Dear Users,</br> <p><br>ChronQC plots are ready for viewing in:  <br>%s</br></br></p><br>Thank you.</br><br>*** This is an automated mail, please do not reply ***</br> 

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
```
