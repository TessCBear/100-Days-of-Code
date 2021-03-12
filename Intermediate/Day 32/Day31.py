import random
import smtplib as s
import datetime as dt
import pandas
import os

my_email = "<insert email here>"
my_password = "<insert password here>"


data = pandas.read_csv(".\Intermediate\Day 32\\birthdays.csv")
data_dict = data.to_dict(orient = "records")

now = dt.datetime.now()
month = now.month
day = now.day

for date in data_dict:
    if date["month"] == month and date["day"] == day:
        name = date["name"]
        letter = random.choice(os.listdir(".\Intermediate\Day 32\\letters"))
        with open(f".\Intermediate\Day 32\letters\{letter}", mode = "r") as starting_letter:
            chosen_letter = starting_letter.read()
            replaced = chosen_letter.replace("[NAME]", name)

        with s.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user = my_email, password = my_password)
            connection.sendmail(from_addr = my_email, to_addrs = date["email"], msg = f"Subject: Happy birthday {name} \n\n{replaced}")
