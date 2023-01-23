import smtplib
import random
import datetime as dt
import pandas as pd 
# def send_mail(quote):
#     my_email = "eboran01@gmail.com"
#     with  smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(user=my_email, password="towvgdljehbgmwrb")
#         connection.sendmail(from_addr=my_email, 
#                             to_addrs="eboran_01@hotmail.com", 
#                             msg=f"Subject:Motivation\n\n{quote}"
#                             )

# # year = now.year
# # month = now.month
# # date_of_birth = dt.datetime(year=1989, month=1, day=18)
# # print(date_of_birth)

# now = dt.datetime.now()
# day_of_week = now.weekday()

# with open("/home/beast/100Days/birthdaywisher/quotes.txt") as f:
#     quotes = f.readlines()
# quote = random.choice(quotes)

# if day_of_week == 5:#5 is saturday
#     send_mail(quote)
    
    
##################### Extra Hard Starting Project ######################
birthdays= pd.read_csv("/home/beast/100Days/birthdaywisher/birthdays.csv")
birthdays = birthdays.to_dict(orient="records")
now = dt.datetime.now()

for birthday in birthdays:
    if birthday["month"] == now.month and birthday["day"] == now.day: 
        name = birthday["name"]
        filename = f"letter_{random.randint(1,3)}.txt" 
        with open("/home/beast/100Days/birthdaywisher/letter_templates/" + filename) as f:
            letter = f.read()
            letter = letter.replace("[NAME]", name)
        my_email = "eboran01@gmail.com"
        passwd="towvgdljehbgmwrb"
        receiver="eboran_01@hotmail.com"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=passwd)
            connection.sendmail(from_addr=my_email, 
                                to_addrs=receiver,
                                msg=f"Subject:Happy Birthday!!!\n\n{letter}"
                                )
