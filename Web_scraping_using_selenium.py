"""
Write a python program to Scrape the below-mentioned site and bring in the list of the first 5 postings under the "Search Postings" heading containing the following fields: Est. Value Notes, Description, Closing Date https://qcpi.questcdn.com/cdn/posting/?group=1950787&provider=1950787 Please give a link to your code and mention any pip install requirements with it.
"""
"""
requriments : pandas and selenium
pip command: pip install pandas && pip install selenium
"""
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
url = 'https://qcpi.questcdn.com/cdn/posting/?group=1950787&provider=1950787'
driver = webdriver.Chrome()
driver.get(url)

# driver.implicitly_wait(5)
time.sleep(5)

table = driver.find_element(By.ID,"table_id")
rows = table.find_elements(By.TAG_NAME, "tr")

col_name = ["Post Date", "Quest Number", "Category Code", "Bid/Request Name", "Bid Closing Date", "City" ,"County", "State", "Owner" ,"Solicitor",  "Posting Type"]
data = {i:[] for i in col_name}

for row in rows:
    # print("row_text", row.text)
    cols = row.find_elements(By.TAG_NAME,'td')

    #print("row", row.text)
    # print("cols",cols)
    for lable,col in zip(col_name,cols):
        data[lable].append(col.text)

df = pd.DataFrame(data).head()
df.to_csv('data.csv')
driver.quit()

"""
output data.csv
,Post Date,Quest Number,Category Code,Bid/Request Name,Bid Closing Date,City,County,State,Owner,Solicitor,Posting Type
0,05/12/2023,8526724,Street/Roadway Reconstruction,"Key No. 22408 3000 E & FOOTHILL RD CURVE, TWIN FAL...",06/06/2023 02:00 PM MDT,N/A,Twin Falls,ID,Idaho Transportation...,Idaho Transportati...,Construction Project
1,05/16/2023,8529878,Traffic Control Devices (Signa...,"Key No. 24192 SH-75, Ohio Gulch Road Intersection",06/06/2023 02:00 PM MDT,N/A,Blaine,ID,Idaho Transportation...,Idaho Transportati...,Construction Project
2,05/18/2023,8534098,Roadway Pavement Markings,Key No. 23815 FY24 D6 STRIPING,06/06/2023 02:00 PM MDT,N/A,"Bonneville, Fremont,...",ID,Idaho Transportation...,Idaho Transportati...,Construction Project
3,05/19/2023,8536176,Roadway Pavement Markings,"Key No. 21842, I-84, FY23 D4 Interstate Striping",06/06/2023 02:00 PM MDT,N/A,Various,ID,Idaho Transportation...,Idaho Transportati...,Construction Project
4,05/22/2023,8539402,Seal Coating,"Key No. 20592 / 20482 SH-3, CDA RV BR to I-90, SH-...",06/06/2023 02:00 PM MDT,N/A,Kootenai,ID,Idaho Transportation...,Idaho Transportati...,Construction Project
"""
