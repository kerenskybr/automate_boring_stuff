import smtplib

conn = smtplib.SMTP('smtp.gmail.com', 587)

print(conn.ehlo())

print(conn.starttls())

#Connect to an account
conn.login('', '')

#To send an email
conn.sendmail('from', 'to', 'subject')

conn.quit()