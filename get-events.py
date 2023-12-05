
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import datetime
import time

channel_url = "https://www.youtube.com/playlist?list=PL2yQDdvlhXf93SMk5EpQVIq4kdWQhUcMV"

driver = webdriver.Chrome()
driver.get(channel_url)

# Wait for page to load
wait = WebDriverWait(driver, 50)
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

        # #scroll the video elemenet into view to help load images
        # driver.execute_script("arguments[0].scrollIntoView();",video)

        # #wait for short period to load image
        # time.sleep(0.01)

        last_height = driver.execute_script("return document.body.scrollHeight")

        while True:
            driver.execute_script("window.scrollTo(0, window.scrollY + 1000)")
            
            time.sleep(0.001)

            title= video.find_element(By.ID,"video-title").text
            views_line= video.find_element(By.ID,"video-info").text
            views_str= views_line[:views_line.find('views') +len('views')] if 'views' in views_line else ''
            views= convert_views_to_int(views_str)


            thumbnail_img= wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-thumbnail#thumbnail img")))
            thumb_url=thumbnail_img.get_attribute("src")

            url = video.find_element(By.ID,"video-title").get_attribute("href")

            video_data.append({"title":title, "views": views,"thumbnail":thumb_url,"url":url })

            print(thumb_url)
            
            # Check if page loaded
            if driver.execute_script("return document.readyState") == "complete":  
            
                new_height = driver.execute_script("return document.body.scrollHeight")
                if new_height == last_height:
                    break 
                
                last_height = new_height



sorted_by_views=sorted(video_data, key=lambda x: x['views'], reverse=True)

# Open file for writing 
with open('output.json', 'w') as f:
    # Convert Python array to JSON string
    json.dump({
            "snapshot_time": datetime.datetime.now().strftime("%d/%m/%Y - %I%p:%M:%S"),  
            "sorted_by_views": sorted_by_views
        }, f)

# for video in sorted_by_views:
#      print(video_data)

# closing the browser
driver.quit()

