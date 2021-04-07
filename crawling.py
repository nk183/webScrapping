from selenium import webdriver
import os

searchterm = 'Okocha'#input your search item here
url = "https://www.google.co.in/search?q="+searchterm+"&source=lnms&tbm=isch"
browser = webdriver.Chrome()#insert path to chromedriver inside parentheses
browser.get(url)
img_count = 0
extensions = { "jpg", "jpeg", "png", "gif" }
if not os.path.exists(searchterm):
    os.mkdir(searchterm)

for _ in range(5):
    browser.execute_script("window.scrollBy(0,10000)")
    
html = browser.page_source.split('["')
imges = []
for i in html:
    if i.startswith('http') and i.split('"')[0].split('.')[-1] in extensions:
        imges.append(i.split('"')[0])
print(imges)