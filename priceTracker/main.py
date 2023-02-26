import requests
from bs4 import BeautifulSoup
import smtplib

header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.50", 
              "Accept-Language":"en-US,en;q=0.9,tr;q=0.8"
              }
URL="https://www.amazon.com/dp/B0B727YMJT/ref=sbl_dpx_kitchen-electric-cookware_B08GC6PL3D_0"
response=requests.get(URL, 
                      headers=header)

# print(response.text)

soup = BeautifulSoup(response.text, "lxml")
# print(soup.prettify())

price = soup.find(name="span", class_="a-offscreen").getText()
title = soup.find(name="span", id="productTitle").getText().strip()
# print(price)
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)
print(title)

message = f"The product you are following:\n{title}\nnow has desired price as {price}. You may find the product at following link:\n{URL}"

my_email = "eboran01@gmail.com"
passwd="towvgdljehbgmwrb"
receiver="eboran_01@hotmail.com"
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=passwd)
    connection.sendmail(from_addr=my_email, 
                        to_addrs=receiver,
                        msg=f"Subject:Price Alert!!!\n\n{message}"
                        )