import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


with open('/home/ubuntu/environment/huntsman_scholar_final_proj/results.txt','r') as f:
    content = f.readlines()
contents = ''.join(content)

s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()
 
# Authentication
s.login("usu.resource@gmail.com", "slphpctqfnnzlfph")

# message to be sent
message = '''Thank you for reaching out to ask about the USU resources available to you, '''+ first_name + '''. Your results are below. \n\n
''' + contents + '''
'''

 
# sending the mail
s.sendmail("usu.resource@gmail.com", "ironman7699@gmail.com", message)
 
print('Email Sent.')
# terminating the session
s.quit()