Practo Mass Mailer
===================

This git repository helps you get up and running quickly  Practo's Mass Mailer
App.The Mass Mailer is written in Python-2.6 using the bottle web framework 
and Mongodb. Bottle is a fast, simple and lightweight WSGI micro web-framework 
for Python. It is distributed as a single file module and has no dependencies 
other than the Python Standard Library.MongoDB (from "humongous") is an open-source 
document database, and the leading NoSQL database written in C++.
Model view controller architecture is used for implementing the user-interfaces


Running on Linux or Mac
----------------------------

First download the mongodb. 

Download the latest release.
	In a system shell, download the latest release for 64-bit Linux.

    curl -O http://downloads.mongodb.org/linux/mongodb-linux-x86_64-2.4.8.tgz

Extract MongoDB From Archive
    
    tar -zxvf mongodb-linux-x86_64-2.4.8.tgz

Then install Pymongo.

    Driver for connection python application to the mongo database.
    
    sudo pip install pymongo

Clone this Application.

     git clone https://github.com/naveedmohadabdul/practo_mailer

The bottle web framework is provided along with the practo mass mailing application.

Then start the mongodb server 

    ./mongodb

Start the Application.
	
	python  practo-mailer.py	

You can now run your application

