from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests
import random
# https://html2canvas.hertzen.com/ use this to capture html to image

app = Flask(__name__)
@app.route("/", methods = ["GET", "POST"])
def index():

    url = "https://www.businesstoday.in/technology/news"

    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")

    outerData = soup.find_all("div", class_ ="widget-listing" ,limit=6)

    finalNews = ""
    for data in outerData:
        news = data.div.div.a["title"]
        finalNews += "\u2022 " + news +"\n"
    # print(finalNews)
    imgSrc =  "static/image/" + str(random.randint(1, 7)) + ".jpg"
    return render_template("index.html", News = finalNews, IMGsrc = imgSrc)
