import cloudscraper #This is to bypass cloudflare and firewalls
from flask import Flask, render_template #will be used to display the webscraped html file.
from urlextract import URLExtract #used to extract urls 
#htptx is used to scrape aswell, alternative since it uses http2 which is modern.
import httpx
#Used to fake the browser in headers for httpx
from fake_useragent import UserAgent

# set UA to useragent var
ua = UserAgent()

#Payload being sent for httpx, Makes the request seem more real.
xheaders = {  
      "Accept":"*/*",    
			"Accept-Encoding":"gzip, deflate, br",
			"Accept-Language":"en-US,en;q=0.9",
			"Connection":"keep-alive",
			"Referer":"https://www.google.com/",
			"Sec-ch-perfers-color-scheme":"light",
			"Sec-Ch-Ua-Mobile": "?0", 
			"Sec-Fetch-Dest":"document",
			"Sec-Fetch-Mode":"navigate",
			"Sec-Fetch-Site":"none",
			"Sec-Fetch-User": "?1", 
			"Upgrade-Insecure-Requests":"1",
			"User-Agent":str(ua.chrome)
}

#set client as http2 for httpx
client = httpx.Client(http2=True)
#set extractor to url extract       
extractor = URLExtract()

#set up path to HTML file where data will be stored using flask
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('site.html')

#Require user input for the URL

ssearch = input("Scrape search? [Y/N] ")
ssearch = ssearch.lower()
if ssearch == "y":
  what = input("What do you want to search? ")
  #replace spaces with + as google uses that
  what = what.replace(" ", "+")
  #replace modified google search with input
  base = f"http://www.google.com/search?q={what}&gws_rd=ssl"
  #request site with url and headers
  http2 = client.get(base,headers=xheaders)
  #save google results to html file
  with open('./templates/site.html', 'w') as f:
      f.write(http2.text)
  urls = extractor.find_urls(http2.text)
  #save links to file
  with open('./templates/links.txt', 'w') as f:
      f.write(str(urls))
  #run site on port 8080
  app.run('0.0.0.0',8080)
# if search option is no, ignore
elif ssearch == "n":
  pass
#make sure input it Y and N only
else:
  print("Y or N only!")
  
url = input("URL: ")

#Set the webscaper headers to a iphone chrome browser user agent, makes it seem real aswell. Also disable brotli, a compression system by cloudflare, makes the results less pretty so its disabled. ecdhCurve is setting the algorithm thats used for the blocking by clouflare, its currently set to a harder version incase the site your scraping is diffcult to scrape.
scraper = cloudscraper.create_scraper(
    browser={
      'browser': 'chrome',
      'platform': 'ios',
      'desktop': False
    },
    allow_brotli=False,
    ecdhCurve='secp384r1'
)


#Gives option to use httpx2 or cloudscraper, if input is 1 it runs httpx2 if 2 it uses cloudscraper

print("httpx2 uses modern http2 requests and seems realistic, cloudscraper is used to bypass cloudflare and bypass anti-bot + decompress brotli")
print(" ")
h2orcf = input("httpx2 [1] or cloudscraper? [2]: ")
if h2orcf == "1":
  print("Scraping site...[May take a bit]")
  try:
    http2 = client.get(url,headers=xheaders)
  except:
    print("An error occured")
    pass
    #save data to site.html
  with open('./templates/site.html', 'w') as f:
      f.write(http2.text)
  #extract links from html
  urls = extractor.find_urls(http2.text)
  #save the links to file
  with open('./templates/links.txt', 'w') as f:
      f.write(str(urls))
  print("Links saved to links.txt")
  print("HTML saved to site.html")
  #run site on port 8080
  app.run('0.0.0.0',8080)

elif h2orcf == "2":
  print("Scraping site...[May take a bit]")
  try:
    cf = scraper.get(url)
  except:
    print("An error occured")
    pass
  #save data to site.html
  with open('./templates/site.html', 'w') as f:
      f.write(cf.text)
  #extract links from html
  urls = extractor.find_urls(cf.text)
  #save the links to file
  with open('./templates/links.txt', 'w') as f:
      f.write(str(urls))
  print("Links saved to links.txt")
  print("HTML saved to site.html")
  #run site on port 8080
  app.run('0.0.0.0',8080)
else:
  print("Select 1 or 2 only!")

#annnnd were done! here it is, the webscraper that scrapes a site, downloads the data, bypasses cloudflare, decompresses it, runs it as html file, extracts and links and saves, then gives preview of the site you just scraped!

# A powerful yet simple web scraper able to bypass Cloudflare, uses HTTP 2.0 and headers to emulate real person, also serve's the saved HTML file and stores the links.
