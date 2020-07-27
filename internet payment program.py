#!/usr/bin/env python3
# Here i am importing all needed modules
import subprocess # this module for os commands excute for
#import smtp.lib # This module for sending sms to Dhritics to notify work is done.

# Here i am making variable
# This is for login information
username = input(" username > ")#here user will input the username
password = input(" password > ")#here user will input the password

#Here i am excuting commands
subprocess.call("firefox https://www.dhritics.com/dashboard/login.php", shell=True)#this for excute commands
