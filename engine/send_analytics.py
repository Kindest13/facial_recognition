import os
# Import smtplib for the actual sending function
import smtplib

# And imghdr to find the types of our images
import imghdr

# Here are the email package modules we'll need
from email.message import EmailMessage

# Create the container email message.
msg = EmailMessage()
msg['Subject'] = 'Analytics'
# me == the sender's email address
# family = the list of all recipients' email addresses
msg['From'] = "..."
msg['To'] = ["..."]
msg.preamble = 'You will not see this in a MIME-aware mail reader.\n'

# Open the files in binary mode.  Use imghdr to figure out the
# MIME subtype for each specific image.

origin_dir = './email'
images = [f.name for f in os.scandir(origin_dir) if f.is_file()]
print(images)

for file in images:
    file_path = os.path.join(origin_dir, file)
    with open(file_path, 'rb') as fp:
        img_data = fp.read()
    msg.add_attachment(img_data, maintype='image',
                                 subtype=imghdr.what(None, img_data))


gmail_user="..."
gmail_password="..."
# Send the email via our own SMTP server.
try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.send_message(msg)
except:
    print('Something went wrong...')