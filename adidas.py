import csv
import requests
from crontab import CronTab
my_cron=CronTab (url='https://www.amazon.in/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=adidas+shoes')
job=my_cron.new(command=python/home/anu/date.py)
for job in my_cron:
  job.day.every(1)
  my_cron.write()
  print job
  print job.frequency_per_day()
from BeautifulSoup import BeautifulSoup
url='https://www.amazon.in/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=adidas+shoes'
response=requests.get(url)
html=response.content
soup=BeautifulSoup(html)
item=soup.find('itdet')
list_of_names=[]
for name in item.find('in'):
  list_of_images=[]
  for image in name.find('ni'):
    list_of_descriptions=[]
    for des in image.find('id'):
      list_of_prices=[]
      for price in des.find('dp'):
        text=price.text.replace('&nbsp;',' ')
        list_of_prices.append(text)
      list_of_discriptions.append(list_of_prices)
    list_of_images.append(list_of_descriptions)
  list_of_names.append(list_of_images)  
outfile=open("./inmates.cv","wb")
writer=csv.writer(outfile)
writer=writenames(list_of_names)
