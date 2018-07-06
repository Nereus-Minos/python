import urllib

from bs4 import BeautifulSoup

import time

response = urllib.urlopen("https://www.panda.tv/cate/yzdr?pdt=1.24.s1.4.7jsrdbdh4mu")

html = response.read()

images = []

for temp in BeautifulSoup(html).select("a .video-img"):
	images.append(temp['data-original'])


i = 0
for image in images:
	name = "/home/zhaohang/images/"+str(i)+".jpg"
	urllib.urlretrieve(image, filename =name )
	i += 1
	time.sleep(1)  

