Telegram_API_key = "SAMPLE_KEY"
def get_art_gal_img_prompt():
  URL = "https://www.midjourney.com/showcase/recent/"
  response = requests.get(URL)
  soup = BeautifulSoup(response.content, "html.parser")
  obj = soup.find(id = "__NEXT_DATA__").get_text()
  # print(type(soup.find(id = "__NEXT_DATA__").get_text()))
  json_obj = json.loads(obj)

  jobs_obj = json_obj["props"]["pageProps"]["jobs"]

  img_prompts = []
  img_urls = []
  def length(i):
      if i:
          return len(i)
      return 0
  for img_obj in jobs_obj:
      # print("imgPrompts",length(img_obj["event"]["imagePrompts"]))
      # print("img_obj",length(img_obj["event"]["textPrompt"]))
      # img_prompts.append(img_obj["event"]["textPrompt"][0])
      # img_urls.append(img_obj["event"]["seedImageURL"])
      img_prompts.append(img_obj["full_command"])
      # print("imgPath",length(img_obj["image_paths"][0]))
      img_urls.append(img_obj["image_paths"][0])
  return zip(img_urls,img_prompts)


def send_photo_using_url(photo_url,prompt):
  base_url = "https://api.telegram.org/"+Telegram_API_key
  parameters = {
      "chat_id" : "-1001821634556", 
      "photo" : photo_url,
      "caption": prompt
  }
  resp = requests.get(base_url + "/sendPhoto", data = parameters)
  print(resp.text)
for photo_url,prompt in get_art_gal_img_prompt():
  #to avoid request cooldown
  time.sleep(5)
  send_photo_using_url(photo_url,prompt)
