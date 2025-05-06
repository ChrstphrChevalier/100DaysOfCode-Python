from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

# url = "https://appbrewery.github.io/instant_pot/"
# Live Site
url = "https://www.amazon.fr/VALVE-Steam-Deck-512gb-Console/dp/B0CP2YVFD4/ref=sr_1_6?__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3002YEG9VNL30&dib=eyJ2IjoiMSJ9.qMde-bWIiQz_ki5GD3pcNQRi6sPQgqnYOl9XTJl7lQoxDrALWFGZaId9j4X7FaGDEgTlQWu6nd3m-YfoNpqHfFK4v7Pt9gYL7FKf8EdYq2XiSHaGa8H6GQhynbvEouin56CgJBaxNsMbfFVuDrB7sEJ72gXPJNN9Im6OeOAMtiXMYsu8LavT3lKcJnI5MGA4dSeFXF7fDu_Ya8r2g4aew_aPxQ3t_6TsnYTwqePTvjno5VTxXEJEEeHJR8I8UTxFaeC4caI-yWwVTTTg3emy-GSaZjPHpUQJAFDoUGX7JH0.7Badss7ubM1qnkkZdX8KG9n088VBhOcaOiMjoF-WKKg&dib_tag=se&keywords=steam+deck+oled&qid=1744997125&sprefix=steam+deck+ole%2Caps%2C285&sr=8-6"

# ====================== Add Headers to the Request ===========================

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "html.parser")
print(soup.prettify())

price = soup.find(class_="a-offscreen").get_text()

price_without_currency = price.split("$")[1]

price_as_float = float(price_without_currency)
print(price_as_float)

title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 70

if price_as_float < BUY_PRICE:
    message = f"{title} is on sale for {price}!"

    # ====================== Send the email ===========================

    with smtplib.SMTP(os.environ["SMTP_ADDRESS"], port=587) as connection:
        connection.starttls()
        result = connection.login(os.environ["EMAIL_ADDRESS"], os.environ["EMAIL_PASSWORD"])
        connection.sendmail(
            from_addr=os.environ["EMAIL_ADDRESS"],
            to_addrs=os.environ["EMAIL_ADDRESS"],
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )