# Day 32 of 100 Days of Code
## Automated Birthday Message Sender

Today I learnt how to send emails using python, which is very exciting! We used *smtplib* to do this:

```python
import smtplib as s
with s.SMTP("smtp.gmail.com") as connection:
    connection.starttls() #make it secure
    connection.login(user = my_email, password = my_password)
    connection.sendmail(from_addr = my_email, to_addrs = "example@gmail.com", msg = "Subject: Hi \n\nThis is the message.")
```

I find it amazing that it's possible to do this, and so easily!

We also learnt how to use *datetime* - another smart module.

```python
import datetime as dt

# Use the current datetime object
now = dt.datetime.now()
year = now.year
month = now.month
week_day = now.weekday()
print(year)

# Create your own datetime object
date_of_birth = dt.datetime(year = 2000, month = 1, day = 1) # hours and minutes etc can be set, default is 0
```
Using these skills, the project of the day was to create a program that automatically sends birthday message emails. The program checks users in *bithdays.csv* to see if today is a particular person's birthday. If it is a birthday, it will choose a random letter from the *letters* folder, replace [NAME] with their name and send them an email wishing them a happy birthday.

This was a really fun project and I thouroughly enjoyed learning these skills.