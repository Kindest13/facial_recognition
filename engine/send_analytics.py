import os
import smtplib
import imghdr
from email.message import EmailMessage

def sendAnalytics(emailDir, email):
    gmailUser="..."
    gmailPassword="..."
    # Create the container email message.
    msg = EmailMessage()
    msg['Subject'] = 'Analytics'
    msg['From'] = gmailUser
    msg['To'] = [email]
    msg.preamble = 'You will not see this in a MIME-aware mail reader.\n'

    # Open the files in binary mode.  Use imghdr to figure out the
    # MIME subtype for each specific image.

    images = [f.name for f in os.scandir(emailDir) if f.is_file()]

    for file in images:
        filePath = os.path.join(emailDir, file)
        with open(filePath, 'rb') as fp:
            imgData = fp.read()
        msg.add_attachment(imgData, maintype='image', subtype=imghdr.what(None, imgData), filename=file)


    # Send the email via our own SMTP server.
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmailUser, gmailPassword)
        server.send_message(msg)
    except:
        print('Something went wrong...')
