import smtplib

targetAdresse = "jjmaus2401b@gmail.com"
fromAdresse = "jjmaus2401@gmail.com"
message = "fufu ist cool "

with smtplib.SMTP("smtp.gmail.com", "587") as smtpserver:
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo()
    smtpserver.login("jjmaus2401@gmail.com","oxzl fkoy titd wuco")
    msg = '''\
    ... From: Me@my.org
    ... Subject: testin'...
    ...
    ... This is a test '''
    for i in range(5):
        smtpserver.sendmail(fromAdresse, targetAdresse, msg)
        print(f"Gmail {i + 1} got send!")



