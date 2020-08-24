import smtplib, os
from email.mime.text import  MIMEText
pw =  os.environ.get('EMAIL_PW')
print(os.environ.get('OS'))

# mailserver = smtplib.SMTP('smtp.office365.com', 587)
# mailserver.ehlo()
# mailserver.starttls()
# mailserver.login('dharmender.rawat@jktech.com', pw)
# mailserver.sendmail('dharmender.rawat@jktech.com', 'dharmender.rawat@jktech.com', 'python email')
# mailserver.quit()


# msg = MIMEText('Hello world body')
# msg['Subjet'] = "This is subject"
# msg['From'] = 'from@demo.com'
# msg['To'] = 'to@demo.com'
# mailserver = smtplib.SMTP('localhost', 25)
# #mailserver.set_debuglevel(2)
# mailserver.sendmail('dharmender.rawat@jktech.com', 'dharmender.rawat@jktech.com', msg.as_string())
# mailserver.quit()

sender = "noreply@blog.com"
receiver = "dsrawat123@gmail.com"

message = f"""\
Subject: Reset Password
To: {receiver}
From: {sender}

This is a test e-mail message to reset your password
"""

with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
    server.starttls()
    server.login("010c05e9d9680c", "46493b81fe388c")
    server.sendmail(sender, receiver, message)

print('Email sent!')