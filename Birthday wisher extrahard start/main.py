##################### Extra Hard Starting Project ######################
import random
from datetime import *
import pandas
import smtplib

email = "h.urreyan@gmail.com"
password = "qujv buku aimu dasx"
# 1. Update the birthdays.csv
#
# 2. Check if today matches a birthday in the birthdays.csv
today = datetime.now()
date = today.day
mon = today.month

birthdays = pandas.read_csv("birthdays.csv")
single_date = birthdays.to_dict(orient="records")
for i in single_date:

    if mon == i["month"] and date == i["day"]:
        name = i["name"]

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        choice_letter = random.randint(1,3)

        with open(f"letter_templates/letter_{choice_letter}.txt", "r") as letter:
            letter_context = letter.read()
            letter_context1 = letter_context.replace("[NAME]", f"{name}",1)


# 4. Send the letter generated in step 3 to that person's email address.

            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(email, password)
                connection.sendmail(from_addr=email,to_addrs=i["email"],msg=f"subject:Happy Birthday\n\n{letter_context1}")


