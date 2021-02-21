from bs4 import BeautifulSoup
import datetime
import time
import random
import re

from urllib.request import urlopen



urls = { "https://www.meetup.com/AWS-Munich/",
         "https://www.meetup.com/Big-Data-Munich/",
         "https://www.meetup.com/Spark-Munich/"
        }



def getMembers (url):

    webpage = urlopen(url)
    soup = BeautifulSoup( webpage.read(), features="lxml")
    tag = soup.find(id="members")

    attendees = re.sub('\D', '', tag.get_text())
    today = datetime.date.today()
    print(f"{today}\t\t{url}\t\t{attendees} ")
    time.sleep(random.randint(1,5))



print(f"#date\t\tmeetupURL\t\tattendees")
for i in urls:
    getMembers(i)

