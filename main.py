import smtplib

MY_EMAIL = "" # The email address you want to send from
PASSWORD = "" # the PASSWORD for the email address that you generated under your email account settings in security settings

def send_email(recipient, subject, body):
    global MY_EMAIL, PASSWORD
    try:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls() # How we connect to email server
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=f"{recipient}", msg=f"{subject}\n\n{body}")
    except(smtplib.SMTPException, OSError) as e:
        print(f"Email failed to send: Error - {e}")

print("Welcome to the email sender program!\n")
email_recipient = input("Who do you want to send an email to? \n")
email_subject = input("What is the subject of the email? \n")
contents_of_email = input("What is the message would you like to send? \n")

send_email(recipient=email_recipient, subject=email_subject, body=contents_of_email)