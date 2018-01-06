import smtplib

smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
print(type(smtpObj))
print(smtpObj.ehlo())
print(smtpObj.login('xxx@gmail.com', 'xxx'))
smtpObj.sendmail('switchvov@gmail.com', 'switchvov@163.com',
                 'Subject: So long.\nDear Alice, so long and thanks for all the fish. Sincerely,Bob')
print(smtpObj.quit())
