
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

channel_url = "https://www.youtube.com/playlist?list=PL2yQDdvlhXf93SMk5EpQVIq4kdWQhUcMV"

driver = webdriver.Chrome()
driver.get(channel_url)

# Wait for page to load
wait = WebDriverWait(driver, 10)
#wait.until(EC.title_contains("YouTube"))

def convert_views_to_int(views_str):
    views_str = views_str.lower().replace(' views','').replace(',','')
    #print(views_str)
    if 'k' in views_str:
            return  int(float(views_str.replace('k',''))*1000)
    return int(views_str)

#Find all video elements in playlist
videos= driver.find_elements(By.CSS_SELECTOR, "ytd-playlist-video-renderer")

#Extract title and view count for each video
video_data = []
for video in videos:
        title= video.find_element(By.ID,"video-title").text
        views_line= video.find_element(By.ID,"video-info").text
        views_str= views_line[:views_line.find('views') +len('views')] if 'views' in views_line else ''
        views= convert_views_to_int(views_str)
        video_data.append({"title":title, "views": views})

        #print(video_data)

sorted_by_views=sorted(video_data, key=lambda x: x['views'], reverse=True)

# Open file for writing 
with open('output.json', 'w') as f:
    # Convert Python array to JSON string
    json.dump(sorted_by_views, f)

# for video in sorted_by_views:
#      print(video_data)

# closing the browser
driver.quit()