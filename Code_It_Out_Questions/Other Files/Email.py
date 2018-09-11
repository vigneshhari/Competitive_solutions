

# import time
# a=time.time()

import smtplib
import csv

fromaddr = 'vigneshhari@ieee.org'			#Enter your from address here


with open('at.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    temp = 0
    for row in spamreader:
        if(row[0].strip() == "Timestamp"):continue
        print("yes " + row[1] + " " + str(temp))
        toaddrs  = row[2]		#Enter recepient address here
        name = row[1]
        psswd = row[5]
        msg ="""Subject: Code It Out

        
Hello There, {},

Thanks for Registering for Code it Out Online Programming Competition

The competition is scheduled for Sunday 7th January 2018 from (6 PM to 9 PM) Duration 3Hrs

Your Login Credentials are as follows
    
    Website : www.cleverhires.com

    Username : {}

    Password : {}

    Your login portal will be opened close to the competition start time at www.cleverhires.com

The Accepted Languages for the Competition are Python3, Python2, Java, C, C++ , Go

There will be points awarded for partial completition of test cases 

Solving any Probelem ( Even Partially ) will make you eligible for a Participation Certificate

The Program is hosted as a part of Magnum 2018 by the IEEE SB Computer Society Chapter, College of Engineering Chengannur
Please do visit out TechFest To be held on January 12-14 2018, For more Details visit cecmagnum.com

The technology partner for the event is Cleverhires , Special Thanks to Them !

We wish you the best of luck for the event and may the odds be ever in your favor

Please reply to this email thread for any issues or Queries
Or contact me at +91 9562854642 ( Whatsapp Preferred )

Thank you,

Vignesh Hari
​Regional Student Ambassador | IEEE Computer Society,
Vice Chairman | IEEE SB College Of Engineering Chengannur,
Web Team Lead | Student Activities Committee | IEEE Computer Society India Council
        """.format(name,toaddrs,psswd).encode('utf-8').strip()
        print(msg)
        try:
            username = fromaddr
            password = 'vEnter Password'					#Enter your password here
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.starttls()
            server.login(username,password)
            server.sendmail(fromaddr, toaddrs, msg)
            server.quit()
        except():
            print("Error at id " + name)
        # print time.time() - a
     