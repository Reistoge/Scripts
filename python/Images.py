from bs4 import BeautifulSoup
import requests
import os
os.mkdir('images')
images=[]
url='https://muheroacademia.com/manga/boku-no-hero-academia-chapter-368/'
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36', 'Referer': 'https://www.google.com/', 'Sec-Fetch-Site': 'same-origin', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-User': '?1', 'Sec-Fetch-Dest': 'document', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8'}
cont=requests.get(url,headers=headers).content
soup=BeautifulSoup(cont,'html.parser')
imgall=soup.find_all('img')
for img in imgall:
    try:
        imgsrc=img['data-srcset']
    except:
        try:
            imgsrc=img['data-src']
        except:
            try:
                imgsrc=img['data-fallback-src']
            except:
                try:
                    imgsrc=img['src']
                except:
                    pass
    images.append(imgsrc)
imgsdownloaded=0
imgsnotdownloaded=0
for image in images:
    if '.svg' in image:
        imgsnotdownloaded=imgsnotdownloaded+1
    else:
     r=requests.get(image).content
     filename='images/image'+str(imgsdownloaded)+'.jpg'
     with open(filename,'wb+') as f:
        f.write(r)
     imgsdownloaded=imgsdownloaded+1
print(f'{imgsdownloaded} Images Downloaded')
print(f'{imgsnotdownloaded} Failed to download')