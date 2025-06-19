import sys
import os
import time
import psutil
import smtplib
from email.message import EmailMessage

def procInfoLog():

    listofProcess = []

    for proc in psutil.process_iter():
        Dict1 = proc.as_dict(attrs=['name','pid','username'])
        listofProcess.append(Dict1)

    return listofProcess

def sendMail(path):

    # Email credentials
    sender_email = "sahilassignment2@gmail.com"
    sender_password = "ylrb fadz eifl qqge"  # Use app password if using Gmail with 2FA
    receiver_email = "Marvellousinfosystem@gmail.com"

    # Create the email message
    msg = EmailMessage()
    msg['Subject'] = 'Log File Attached'
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg.set_content('Hi Sir \n Please find the log file attached.')

    # Attach the log file
    log_file_path = path
    with open(log_file_path, 'rb') as file:
        file_data = file.read()
        file_name = file.name

    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

    # Send the email via SMTP (Gmail example)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender_email, sender_password)
        smtp.send_message(msg)

    print("Email sent successfully!")

def createDirectory(Dirname):

    if not os.path.exists(Dirname):
        os.mkdir(Dirname)

    timestamp = time.ctime()

    timestamp = timestamp.replace(" ","_")
    timestamp = timestamp.replace(":","_")
    timestamp = timestamp.replace("-","_")

    Filename = "Marvellous%s.log" %(timestamp)

    Filename = os.path.join(Dirname,Filename)

    fobj = open(Filename,"w")

    data = procInfoLog()

    for value in data:
        fobj.write("%s \n\n" %(value))

    sendMail(Filename)

def main():

    createDirectory(sys.argv[1])

if __name__ == "__main__":
    main()