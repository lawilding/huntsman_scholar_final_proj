import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()
 
# Authentication
s.login("usu.resource@gmail.com", "slphpctqfnnzlfph")
 
# message to be sent
message = """\
<html>
  <body>
    <p>Hi,<br>
       How are you?<br>
       <a href="http://www.realpython.com">Real Python</a> 
       has many great tutorials.
    </p>
  </body>
</html>
"""
 
# sending the mail
s.sendmail("usu.resource@gmail.com", "ironman7699@gmail.com", message)
 
# terminating the session
s.quit()