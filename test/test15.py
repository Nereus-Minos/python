import urllib

import re

import time

response = urllib.urlopen("https://www.panda.tv/cate/yzdr?pdt=1.24.s1.4.7jsrdbdh4mu")

html = response.read()

images = re.findall(r'data-original="(.*?\.(jpg|png))"', html)

print(images)

i = 0
for image in images:
	name = "/home/zhaohang/images/"+str(i)+".jpg"
	urllib.urlretrieve(image[0], filename =name )
	i += 1
	time.sleep(1)  
