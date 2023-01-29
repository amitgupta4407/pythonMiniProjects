# import nest_asyncio
# nest_asyncio.apply()
# df.write('We will be seeing an interated printing of numbers between 0 to 10\n')
# exit()
from requests_html import HTMLSession
print('start')
session = HTMLSession()
url = "https://pixela.ai"
r = session.get(url)
r.html.render(sleep = 5, keep_page = True, scrolldown = 30)
# print(r.text)
photos = r.html.find('.photo')
# print(photos.find('.photo'))
# print(photos)
# lsAlt = []
# lsImg = []
df=open('textfile.txt','w')
for item in photos:
    img = (item.xpath('//img'))
    for i in img:
        # print(i.attrs['src'])
        df.write(i.attrs['src'] + "   ")
        df.write(i.attrs['alt'][:-4])
        df.write('\n')
        # lsImg.append(i.attrs['src'])
        # lsAlt.append(i.attrs['alt'])
df.close()
# print(len(lsImg),len(lsAlt))


# this code will provide about 200 results for more increase scrolldown to 50 or more
