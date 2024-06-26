# import the necessary components first
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

port = 587

sender_email = "jjmaus2401@gmail.com"
receiver_email = "helmut.janknecht@googlemail.com"
message = MIMEMultipart("alternative")
message["Subject"] = "Automatic python gmail"
message["From"] = sender_email
message["To"] = receiver_email


text = """\
Das hier ist eine gmail von einem python Bot, die zb für das MamaDoo programm verwendet werden könnte!!
"""



# convert both parts to MIMEText objects and add them to the MIMEMultipart message
part1 = MIMEText(text, "plain")
message.attach(part1)

# send your email
with smtplib.SMTP("smtp.gmail.com", "587") as smtpserver:
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo()
    smtpserver.login("jjmaus2401@gmail.com","oxzl fkoy titd wuco")
    smtpserver.sendmail(
        sender_email, receiver_email, message.as_string()
    )

print('Sent')