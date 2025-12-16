import smtplib
import datetime as dt
import random

MY_EMAIL = 'pomvaul@gmail.com'
PWD = 'atpf cxyo usdw qouv'

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 4: # 0= 월요일
    with open("quotes.txt", mode='r') as quote:
        quotes = quote.readlines()  # 파일 내용을 한 번만 읽기
        quote = random.choice(quotes)

    with smtplib.SMTP("smtp.gamil.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PWD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=f"Subject:Monday Motivation\n\n {quote}")

