import requests

def download_file(image_url):
    fileName = new_name(image_url)
    r = requests.get(image_url)
    path = "D:/up-scaled_img/day4"
    with open(path+'/'+ fileName ,'wb') as f:
        f.write(r.content)
    f.close()
def new_name(image_url, user_name = "styler_9784-834_"):
    s = len(user_name)
    return image_url.split("/")[6][s:]
download_file("https://cdn.discordapp.com/attachments/1068564090563334288/1070052876849795102/styler_9784-834_a_view_of_love_in_the_mountains_from_the_top_of_58ffe3b2-85b5-4097-86a1-8220a2237126.png")














"""
image_url = "https://www.python.org/static/community_logos/python-logo-master-v3-TM.png"
  
# URL of the image to be downloaded is defined as image_url
r = requests.get(image_url) # create HTTP response object
  
# send a HTTP request to the server and save
# the HTTP response in a response object called r
path = "D:/up-scaled_img/day4"
with open(path+'/'+"python_logo.png",'wb') as f:
  
    # Saving received content as a png file in
    # binary format
  
    # write the contents of the response (r.content)
    # to a new file in binary mode.
    f.write(r.content)
f.close()
"""

