#!/usr/bin/python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys, time
from getpass import getpass

eServices = ["smtp.gmail.com",
             "smtp.mail.yahoo.com",
             "smtp-mail.outlook.com"]

b, r, w, y, p, g, bld, z = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[1m', '\033[0m'


animation = (g +'——►'+ g, '»—————►')  
for i in range(15):
    sys.stdout.write('\b\b\b')
    sys.stdout.write(animation[i % len(animation)])
    sys.stdout.flush()
    time.sleep(0.04)
print (' 100%')
time.sleep(1)
sys.stdout.write('\x1b[1A')
sys.stdout.write('\x1b[2K')

sys.stdout.write(g + (" " * 76) + """
    ________         _____                   ______  ___      ___________            
    __  ___/__      ____(_)____________      ___   |/  /_____ ___(_)__  /____________
    _____ \__ | /| / /_  /___  __ \  _ \     __  /|_/ /_  __ `/_  /__  /_  _ \_  ___/
    ____/ /__ |/ |/ /_  / __  /_/ /  __/     _  /  / / / /_/ /_  / _  / /  __/  /    
    /____/ ____/|__/ /_/  _  .___/\___/      /_/  /_/  \__,_/ /_/  /_/  \___//_/     
                      /_/                                                            
    """ + z + b +
    '\n' + '{}Email Marketing sender ({}Swipe Mailer{}){}'.format(y, r, y, b).center(108) +
     'Made With <3 by: {0}Mahmoud Hamdi ({1}(Mxhmovd){2}) '.format(y, r, y).center(101) +
     'Version: {}0.1{} \n'.format(y, z).center(97))


sys.stdout.write("%-6s \n" % (""))


username = input("{}E-mail: ".format(bld))
password = getpass('Password:')

domain = username.split('@')[-1]
if  domain == "gmail.com":
    host, port = eServices[0], 587
elif domain == "yahoo.com":
    host, port = eServices[1], 587
else:
    an = input ("Are you using Microsoft outlook? (y/n)")
    if an.lower()=="y":
        host, port = eServices[2], 587
    else:
        print(bld +r +domain + " is NOT supported yet")
        exit()


a=[]
for i in list(username.split('@')[0]):
    if ord(i)>=97 and ord(i)<=122 or ord(i)>=65 and ord(i)<=90:
        a.append(i)
print ("Hello, " +"".join(a)+r +" \u2665"+ r+" Enjoy!")
time.sleep(2)
sys.stdout.write('\x1b[1A')
sys.stdout.write('\x1b[2K')

class emailHandler():
    userEmail = []

    def addUser(self, email):
        self.userEmail.append(email)

    def getUser(self):
        return self.userEmail

    def connect(self):
        connect = smtplib.SMTP(host, port)
        connect.ehlo()
        connect.starttls()
        try:
            connect.login(username, password)
        except:
            print(r+bld+'Wrong E-mail/password')
            exit()
        return connect

    def testConnect(self):
        try:
            self.connect()
        except smtplib.SMTPException:
            return False
        return True

    def sendEmail(self, choice):
        for i in range(len(self.userEmail)):
            try:
                Message = MIMEMultipart("alternative")
                Message['Subject'] = msgSubject
                if choice==1:
                    content = MIMEText(wholeMessage, 'html')
                else:
                    content = MIMEText(wholeMessage, 'plain')
                Message.attach(content)

                self.connect().sendmail(username, self.userEmail[i], Message.as_string())
            except smtplib.SMTPException:
                return False
        self.connect().quit()
        return True

def exit():
    print ("Exiting ...")
    time.sleep(0.8)
    sys.exit(0)


obj = emailHandler()

if obj.connect():
    print(y+bld+'\nConnection Successfully established !'+z)
else:
    print(r+bld+'Error connecting !'+z)
    exit()

print(w+bld+"\n******** MESSAGE ********"+z)
msgSubject = input( g+"[+]"+g  +  w+bld+"Message subject: "+z )
print(g+"[+]"+g+  w+bld+"Format of the message? "+z)
print ("1.HTML      2.Plain")
formatChoice = int(input())
print ("1.Load File     2.Write it here")
operationChoice = int(input())

if operationChoice == 1:
    try:
        direc = input(bld+"Path of the message. For ex. /home/Messages/message.txt/html : "+z)
        f2=open(direc, "r")

        wholeMessage = f2.read()
        f2.close()
    except IOError:
        print(r+bld+'File NOT found')
        exit()

elif operationChoice == 2:

    print(bld+"Enter/Paste your message. Ctrl+D or Ctrl+Z to save it."+z)
    contents = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        contents.append(line)
    wholeMessage = "\n".join(contents)


    if "<html>" not in wholeMessage:
        if formatChoice == 1:
            print(r+bld+'You choosed "HTML", but wrote in "Plain"')
            exit()
    if "<html>" in wholeMessage:
        if formatChoice == 2:
            print(r+bld+'You choosed "Plain", but wrote in "HTML"')
            exit()
else:
    print(r+bld+'Choose 1 or 2')
    exit()

print(bld+"\n******** E-mail Address ********")
print ("1.Load File     2.Write it here")
operationChoice2 = int(input())
if operationChoice2 == 1:
    try:
        direc2 = input("Path of the E-mail list. For ex. /home/E-mail/emailList.txt : ")
        with open(direc2) as f: 
            for email in f:
                obj.addUser(email)
    except IOError:
        print(bld+r+'File NOT found')
        exit()

elif operationChoice2 == 2:
    print("How many Addresses you want to add?")
    addressChoice=int(input())
    for i in range(addressChoice):
        email=input("Email no.{0}: ".format(i+1))
        obj.addUser(email)
else:
    print(bld+r+'Choose 1 or 2')
    exit()

if obj.sendEmail(formatChoice):
    print(bld+g+'E-mail Successfully sent !')
else:
    print(bld+r+'Error sending the message !')
    exit()

#MVX