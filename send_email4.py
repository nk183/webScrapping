import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders



def main(email_send='varun.er13.6@gmail.com',filename='smile_baby.zip'):
	
	email_user='*********@gmail.com'

	email_password='********'
	
	subject = 'python'

	msg = MIMEMultipart()
	msg['From'] = email_user
	msg['To'] = email_send
	msg['Subject'] = subject

	body = 'Hi there, sending this email from Python!'
	msg.attach(MIMEText(body,'plain'))

	
	attachment  =open(filename,'rb')

	part = MIMEBase('application','octet-stream')
	part.set_payload((attachment).read())
	encoders.encode_base64(part)
	part.add_header('Content-Disposition',"attachment; filename= "+filename)

	msg.attach(part)
	text = msg.as_string()
	
	
	smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
	smtpserver.ehlo()
	smtpserver.starttls()

	smtpserver.login(email_user,email_password)



	smtpserver.sendmail(email_user,email_send,text)
	smtpserver.quit()
	
if __name__ == '__main__':
	main('varun.er13.6@gmail.com','pen.zip')
   # main(sys.argv[1], sys.argv[2])	
