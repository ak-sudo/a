import smtplib as s

object=s.SMTP("smpt.gmail.com", 587)
object.starttls()
object.login("itzakshat706@gmail.com","akshatkala1@")
print("what should be the subject")
subject=input(" ")
print("what should i mail")
body=input(" ")
print("to whome i should send this mail?")
to=input(" ")
message="subject:{}\n\n{}".format(subject, body)
object.sendmail("itzakshat706@gmail.com", to, message)
print("mail successfully sent...")