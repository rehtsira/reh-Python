import os, re #loads the os and regex module
import smtplib #loads smtplib for the extra credit bit 
from email.message import EmailMessage
import ssl

def faileduserlist(): 
    readfile = open("secure-error-log.txt","r") #sets the file as a variable to read the contents of the text file
    tfile = readfile.read() #sets the variable above so that you can read the contents by just printing 'tfile'

    failedusers = re.findall('Failed password for invalid user\s(\w+)',tfile) #searches for all invalid users and capturing their username

    deduplication = list(dict.fromkeys(failedusers)) #changes the list of failed users into a dictionary to remove duplicates
    print('Please name the text file you want to save the failed usernames to') #takes the user input for name of new text file
    textfile = input()

    f = open(textfile,"w") #creates a new textfile based on user input in the same directory
    
    for files in deduplication: #use a for loop to put all the values in the list into the new text file separated by new line
        f.write(files+'\n') 
    f.close()
    return textfile #returns the value of 'textfile' to be used for by another function

#faileduserlist()  #calls the function faileduserlist
def Error1():
    raise Exception("Should have inputted [yes] or [no]") #just a simple debugging tool for if a user inputted something other than a 'yes' or 'no'

def mayday():
    print('Would you like to know if there were multiple failed attempts in the log file you provide?')
    yesno = input() 
    if yesno == 'yes':
        try: #try and except if the inputted log file cannot be found
            print('Please type the name of the log file')
            logfile = input()
            yourfile = open(logfile,"r")
            yourlogfile = yourfile.read() #reads the user-inputted log file
            print(yourlogfile)
            attempts = re.findall('Failed password for invalid user\s\w+',yourlogfile)
            print(attempts)
            if len(attempts) > 3: #checks if there were more than 3 matches for 'Failed password for invalid user'
                print('Uh oh, there were more than three failed password attempts at your file: ' + logfile)
        except:
            print('Sorry, we could not find your file: ' + logfile)
            quit()
    elif yesno == 'no':
        print('Ahh, okay then...')
        quit()
    else:
        Error1() #calls the raise exception function


hah = '''
…………………………………………. ………………………………….,-~~”””’~~–,,_
………………………………………….. …………………………….,-~”-,:::::::::::::::::::”-,
………………………………………….. ………………………..,~”::::::::’,::::::: :::::::::::::|’,
………………………………………….. ………………………..|::::::,-~”’___””~~–~”’:}
………………………………………….. ………………………..’|:::::|: : : : : : : : : : : : : :
………………………………………….. ………………………..|:::::|: : :-~~—: : : —–: |
………………………………………….. ……………………….(_”~-’: : : : : : : : :
………………………………………….. ………………………..”’~-,|: : : : : : ~—’: : : :,’–never gonna
………………………………………….. ……………………………|,: : : : : :-~~–: : ::/ —–give you up!
………………………………………….. ……………………….,-”\’:\: :’~,,_: : : : : _,-’
………………………………………….. ………………….__,-’;;;;;\:”-,: : : :’~—~”/|
………………………………………….. ………….__,-~”;;;;;;/;;;;;;;\: :\: : :____/: :’,__
………………………………………….. .,-~~~””_;;;;;;;;;;;;;;;;;;;;;;;;;’,. .”-,:|:::::::|. . |;;;;”-,__
…………………………………………../;;;;;;;;;;;;;;;;;;;;;;;;;;;;,;;;;;;;;;\. . .”|::::::::|. .,’;;;;;;;;;;”-,
…………………………………………,’ ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;|;;;;;;;;;;;\. . .\:::::,’. ./|;;;;;;;;;;;;;|
………………………………………,-”;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;\;;;;;;;;;;;’,: : __|. . .|;;;;;;;;;,’;;|
…………………………………….,-”;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;’,;;;;;;; ;;;; \. . |:::|. . .”,;;;;;;;;|;;/
……………………………………/;;;;;;;;;;;;;;;;;;;;;;;;;;|;;;;;;;;;;;;;;\;;;;;;;; ;;;\. .|:::|. . . |;;;;;;;;|/
…………………………………./;;,-’;;;;;;;;;;;;;;;;;;;;;;,’;;;;;;;;;;;;;;;;;,;;;;;;; ;;;|. .\:/. . . .|;;;;;;;;|
…………………………………/;;;;;;;;;;;;;;;;;;;;;;;;;;,;;;;;;;;;;;;;;;;;;;;;;; ;;;;;;;”,: |;|. . . . \;;;;;;;|
………………………………,~”;;;;;;;;;; ;;;;;;;;;;;,-”;;;;;;;;;;;;;;;;;;;;;;;;;;\;;;;;;;;|.|;|. . . . .|;;;;;;;|
…………………………..,~”;;;;;;;;;;;;;; ;;;;;;;;,-’;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;’,;;;;;;| |:|. . . . |\;;;;;;;|
………………………….,’;;;;;;;;;;;;;;;;; ;;;;;;;/;;;,-’;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,;;;;;| |:|. . . .’|;;’,;;;;;|
…………………………|;,-’;;;;;;;;;;;;;;;;;;;,-’;;;,-’;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,;;;;| |:|. . .,’;;;;;’,;;;;|_
…………………………/;;;;;;;;;;;;;;;;;,-’_;;;;;;,’;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;|;;; ;|.|:|. . .|;;;;;;;|;;;;|””~-,
………………………./;;;;;;;;;;;;;;;;;;/_”,;;;,’;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; ,;;| |:|. . ./;;;;;;;;|;;;|;;;;;;|-,,__
……………………../;;;;;;;;;;;;;;;;;,-’…|;;,;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; ;;;;;| |:|._,-’;;;;;;;;;|;;;;|;;;;;;;;;;;”’-,_
……………………/;;;;;;;;;;;;;;;;,-’….,’;;,;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; ;;;;;;;;|.|:|::::”’~–~”’||;;;;;|;;;;;;;;;;,-~””~–,
………………….,’;;;;;;;;;;;;;;;;,’……/;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; ;;|.|:|::::::::::::::|;;;;;’,;;;;;;;;;”-,: : : : : :”’~-,:”’~~–,
…………………/;;;;;;;;;;;;;;;,-’……,’;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; ;;;;;;;;;;;;|:|:|::::::::::::::’,;;;;;;|_””~–,,-~—,,___,-~~”’__”~-
………………,-’;;;;;;;;;;;;;;;,’……../;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; ;;;;|:|:|:::::::::::::::|;;;;;;|……………… …”-,\_”-,”-,”~'''

def send_email(textfile): #function to send an email to an inputted recipient using smtp with an attached file of the faileduserlist function showing the failed usernames
    context =ssl.create_default_context()
    message = EmailMessage()
    message["From"] = 'your-email-here'
    message["Subject"]= "Failed Users Log Report"
    print('Please type where you want the email of failed users to go')
    recipient = input()
    message["To"] = recipient
    message.set_content("Here are your reports, rickroller" + hah)
    thefile = open(textfile,"r")
    readme = thefile.read()
    message.add_attachment(readme, filename="hah.txt")
    smtp_server = smtplib.SMTP_SSL("smtp.gmail.com",465,context=context)
    smtp_server.login('your-email-here' , <totallycleartextpassword>)
    smtp_server.send_message(message)
mayday()
send_email(faileduserlist())

