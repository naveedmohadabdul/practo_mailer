from bottle import *
import httplib2
import json
from HtmlStripper import strip_tags
import datetime
import smtplib
import pymongo


def noticeEmail(usr, psw, fromaddr,toaddrlst,sub,msg1):
    """
    Sends an email message through GMail once the script is completed.  
    Developed to be used with AWS so that instances can be terminated 
    once a long job is done. Only works for those with GMail accounts.
 
    usr : the GMail username, as a string
 
    psw : the GMail password, as a string 
    
    fromaddr : the email address the message will be from, as a string
    
    toaddr : a email address, or a list of addresses, to send the 
             message to
    """
    
    # Initialize SMTP server
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    try:
	server.login(usr,psw)
    except smtplib.SMTPHeloError:
	return "The server didn't properly reply to HELO greeting."
    except smtplib.SMTPAuthenticationError:
	return "The server didn't accept the proper username password combination"
    except  smtplib.SMTPException:
	return "No suitable authentication method was found." 
    # Send email
    senddate=datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d')
    subject=" "+sub
    msg=''' '''+msg1
    for toaddr in toaddrlst:
	m="Date: %s\r\nFrom: %s\r\nTo: %s\r\nSubject: %s\r\nX-Mailer: My-Mail\r\n\r\n" % (senddate, fromaddr, toaddr, subject)
	server.sendmail(fromaddr, toaddr, m+msg+msg1)
    server.quit()
    return " "

def insert_data(uid,to_UID,sub,msg):
	'''
	Connect's to the Mongo Database and Insert's collection into the database...
	uid	: User Id of the person who has Mailed
	to_UID  : List of the person to mail 
	msg	: Message
	'''
	try:
		connection = pymongo.MongoClient("mongodb://localhost")
	except Exception:
		err = "Problem connecting to the databse"
		template('except',{'err':'err'})
	db = connection.practo
	people = db.mailer
	dat_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	mass_mail = {'uid':uid,'to_UID':to_UID,'sub':sub,'msg':msg,'dat_time':dat_time}
	try:
		people.insert(mass_mail)
	except Exception:
		err = "Problem inserting the collection"
		template('except',{'err':'err'})
	return 

	
@route('/')
def home_page():
	h = httplib2.Http(".cache")
	h.add_credentials('user', 'pass')
	#Pulling data from the apiary.io api
	try :
	   r, content = h.request("https://patients.apiary.io/patients", "GET")
	   #Loading json's content 
	   data = json.loads(content)
	except httplib2.ServerNotFoundError:
                return template("except",{"err":"Site is Down"}) 
        except Exception:
                return template("except",{"err":"Json's format is not right"}) 
	return template('app',{'items':data})

@post('/body_filter')
def body_filter():
	#Script for retrieving the body of the post  
	body =  request.body.readlines()
	#Filtering the body's  request as Bottle does not provide access to multivalued attributes. 
	body = body[0].replace('%40','@').replace('email=','').replace('&submit=Submit','').replace('Mail=Mail','').split('&')
	if body[0]=='':
		err = "Patients not Selected"
		return template("except",{"err":err})
	emails = {}
	#creating a dictionary with name as key and email as value
	for i in body:
		c = i.split('XXX')
		if c[0]!="":
			emails[c[1]] = c[0]
	return template("mail",{"emails":emails})
	
@post('/mass_mail')
def mass_mail():
	# Requesting the entered data
	try:
	   name = strip_tags(request.forms.get("name"))
	   password= strip_tags(request.forms.get("password"))
	   fromaddr=strip_tags(request.forms.get("fromaddr"))
	   to_email= strip_tags(request.forms.get("P_Email")).split(',')
	   to_UID= strip_tags(request.forms.get("P_UID")).split(',')
	   sub= strip_tags(request.forms.get("subject"))
	   msg= strip_tags(request.forms.get("message"))
	except:
	       err = "Please enter all the requestef field's"
	       template("except",{'err':err})
	err = noticeEmail(name,password,fromaddr,to_email,sub,msg)
	if err!=" ":
		#Handling erros
		return template("except",{"err":err})
	else:	
		# Inserting data into the database
		insert_data(name,to_UID,sub,msg)
		return template("sucess")


@route('/emails/sent')
def emails_sent():
	connection = pymongo.MongoClient('mongodb://localhost')
	db = connection.practo
	post = db.mailer
	return template("mail_blog",{'mailer':post})

@error(404,err='')
def error404(error):
    err =  'Nothing here, sorry'
    return template('except',{'err':err})

debug(True)
run(host='localhost',port=8080)
