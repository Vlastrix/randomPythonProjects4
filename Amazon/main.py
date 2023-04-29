from bs4 import BeautifulSoup
import requests
import smtplib

PRODUCT_URL = "https://www.amazon.com/dp/B087H24T6G/ref=cm_sw_r_tw_dp_R5239MXN844T34GG4FF6?_encoding=UTF8&psc=1"
MY_EMAIL = "YOUR EMAIL"
MY_PASSWORD = "YOUR PASS"


header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,"
              "image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
    "X-Forwarded-For": "190.186.23.2",
    "X-Http-Proto": "HTTP/1.1",
}

response = requests.get(PRODUCT_URL, headers=header)
response.raise_for_status()
product_page = response.text

soup = BeautifulSoup(product_page, "html.parser")
price = soup.select_one('#priceblock_ourprice').text
product_title = soup.select_one('#productTitle').text
product_title = product_title.split("\n")[8]


price = float(price.split("$")[1])

if price <= 260:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject: Amazon Price Alert!\n\n{product_title} is now ${price}\n{PRODUCT_URL}"
        )
