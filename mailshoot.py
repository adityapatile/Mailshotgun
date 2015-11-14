	import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from passcode import pwd
import csv
#message= "Hello this is written by code, happy that you got the message please whatsapp me"

#Mapping = {'aditya':'adityafool@gmail.com','manoj':'manoj.p.gudi@gmail.com','pinjali':'pranju20@gmail.com','batlu':'saurabh1292@gmail.com','adityaoff':'aditya.patil@housing.com'}


""" Defining Dictionary """
sheet = open('bande.csv','r')
p = csv.reader(sheet)
Mapping = {l[0]:l[1] for l in p}

""" Input from user for mail content """
sub = raw_input("Subject >_")
message = raw_input("Please Write Message Body>_")
kisko=raw_input("Mail send to ?")
k=Mapping[kisko]
print "Sending message to %s with %s subject line and body as %s" %(k,sub,message)
frm = "adityafool@gmail.com"


server = smtplib.SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()
server.ehlo()
server.login("adityafool@gmail.com",pwd("adityafool@gmail.com"))

msg = MIMEMultipart()
msg['From']= frm
msg['To'] =k
msg['Subject'] = sub
msg.attach(MIMEText(message,'plain'))
text=msg.as_string()


server.sendmail(frm,k,text)
server.close()
print "Mail sent" 
