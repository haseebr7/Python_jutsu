import smtplib
from datetime import *

# email = "h.urreyan@gmail.com"
# password = "qujv buku aimu dasx"
#
# server = smtplib.SMTP("smtp.gmail.com", 587)
# server.starttls()
# server.login(email, password)
# server.sendmail(from_addr=email,to_addrs="acheee85@gmail.com",msg="Bro Hru")
# server.close()

current_time_day = datetime.now()
current_day = current_time_day.weekday()


if current_day == 4:
    with open(file="quotes") as file:
        quotes = file.read()
        print(quotes)


print(current_day)