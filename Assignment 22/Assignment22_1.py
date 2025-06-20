import sys
import os
import time
import CheckList
import hashlib
import schedule
import smtplib
from email.message import EmailMessage

def findchecksum(path,blocksize = 1024):

    fobj = open(path,'rb')

    hobj = hashlib.md5()

    buffer = fobj.read(blocksize)

    while(len(buffer) > 0):

        hobj.update(buffer)
        buffer = fobj.read(blocksize)

    return hobj.hexdigest()

def sendMail(Path, scannedCount, deleteCount, timeOfScan, receiversEmail):
    # Email credentials
    sender_email = "sahilassignment2@gmail.com"
    sender_password = "ylrb fadz eifl qqge"  # Use app password if using Gmail with 2FA
    receiver_email = receiversEmail

    # Create the email message
    msg = EmailMessage()
    msg['Subject'] = 'Log File Attached'
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg.set_content('Hi Sir\nPlease find the log file attached\n\nStaring Time of Scanning : %s' %(timeOfScan)+'\nTotal Number of file scanned : %s' %(scannedCount)+'\nTotal number of duplicate files found : %s' %(deleteCount))

    # Attach the log file
    log_file_path = Path
    with open(log_file_path, 'rb') as file:
        file_data = file.read()
        file_name = file.name

    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

    # Send the email via SMTP (Gmail example)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender_email, sender_password)
        smtp.send_message(msg)

    print("Email sent successfully!")

def createDirectory(DirName):

    if not os.path.exists(DirName):
        os.mkdir(DirName)

    DirName = CheckList.checkPath(DirName)

    DictDemo = {}

    for folders, subfolders, files in os.walk(DirName):
        for fname in files:
            fname = os.path.join(folders,fname)
            checksum = findchecksum(fname)
            
            if checksum in DictDemo:
                DictDemo[checksum].append(fname)
            else:
                DictDemo[checksum] = [fname]

    return DictDemo

def findDuplicate(path, email):

    Data = createDirectory(path)

    Result = list(filter(lambda x : len(x) > 1, Data.values()))

    timestamp = time.ctime()

    timestamp = timestamp.replace(" ","_")
    timestamp = timestamp.replace(":","_")
    timestamp = timestamp.replace("-","_")

    path = CheckList.checkPath(path)
    
    FileName = "Marvellous%s.log" %(timestamp)

    FileName = CheckList.checkPath(FileName)

    FileName = os.path.join(path,FileName)

    flag = os.path.exists(FileName)

    if flag == False:
        fobj = open(FileName,"w")
    else:
        fobj = open(FileName,"a")


    border = "-"*40
    fobj.write(border)
    fobj.write("\nThis File contains the details of Deleted File\n")
    fobj.write(border+"\n")

    count = 0
    for value in Data.values():
        count = count + len(value)

    cnt = 0
    deleteCount = 0

    scanTime = time.strftime("%H:%M:%S")

    for value in Result:
        for subvalue in value:
            cnt = cnt + 1
            if cnt > 1:
                fobj.write("Deleted File name is : "+subvalue+"\n")
                os.remove(subvalue)
                deleteCount = deleteCount + 1
        cnt = 0
    
    fobj.write("Total number of files scanned : %s" %(count)+"\n")
    fobj.write("Total number of files deleted : %s" %(deleteCount)+"\n")
    fobj.write(border+"\n")
    fobj.close()

    sendMail(FileName,count,deleteCount,scanTime, email)

def main():

    Border = "-"*49

    print(Border)
    print("-------------Marvellous Automation--------------")
    print(Border)

    if(len(sys.argv) == 2):
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This application is used to perform directory cleaning")
            print("This is the directory automation script")
            exit()

        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
                print("Used the given script as")
                print("ScripName.py then Enter")
                print("On new line Enter Name of the directory")
                print("After Directry name on new line enter receivers email id ")
                exit()

    if(len(sys.argv) == 1):
        FolderName = input()
        emailToSend = input()
        schedule.every(50).minutes.do(findDuplicate, FolderName, emailToSend)

        while(True):
            schedule.run_pending()
            time.sleep(1)

    print("------------------------------------------------")
    print("------------Thank you for using our script-----")
    print("------------Marvellous Infosystems-------------")
    print("------------------------------------------------")

    print(Border)

    

if __name__ == "__main__":
    main()