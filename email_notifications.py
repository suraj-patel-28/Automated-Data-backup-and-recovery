import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body, to_email):
    # Email configuration
    sender_email = 'your_email@gmail.com'
    sender_password = 'your_email_password'
    
    # Create the MIME object
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = to_email
    message['Subject'] = subject
    
    # Attach the email body
    message.attach(MIMEText(body, 'plain'))
    
    # Connect to the SMTP server
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        
        # Send the email
        server.sendmail(sender_email, to_email, message.as_string())

# Usage example:
# send_email('Backup Status', 'The backup was successful.', 'recipient@example.com')
