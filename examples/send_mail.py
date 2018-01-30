# condig: utf-8

import smtplib
from email.mime.text import MIMEText
import textwrap

from datetime import datetime
import os

mail_server_address  = 'localhost'
mail_server_port     = 1025
mail_server_username = 'user1@example.com'
mail_server_password = 'pass1'
to_address           = 'to1@example.com'

eventname = 'PROCESS_STATE_XXX'
datetime_ = datetime.utcnow().isoformat() + 'Z'
region    = 'region1'
process   = 'process1'

body = """
event
{}

datetime
{}

region
{}

process
{}
""".format(eventname, datetime_, region, process)

msg = MIMEText(textwrap.dedent(body).strip())

msg['Subject'] = "{} {} {}".format(region, process, eventname)
msg['From']    = mail_server_username
msg['To']      = to_address

s = smtplib.SMTP(mail_server_address, mail_server_port)
s.ehlo('localhost')
s.login(mail_server_username, mail_server_password)
s.sendmail(mail_server_username, to_address, msg.as_string() )
s.close()

