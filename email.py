import imaplib
email_user = 'krishna.vaddepalli@aeromon.fi'
email_pass = 'K2!$hn@6794'


mailcheck = imaplib.IMAP4_SSL('imap-mail.outlook.com', 993)
mailcheck.login(email_user, email_pass)
mailcheck.select()

type, num = mailcheck.search(None, 'ALL') 

last = num[0].split()[-1] #Read last email
type, data = mailcheck.fetch(last, '(RFC822)')
output = data[0][1]
print(output)

mailcheck.close()
mailcheck.logout()