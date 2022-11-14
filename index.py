
import requests
from bs4 import BeautifulSoup
import os

url = url='https://www.imdb.com/india/top-rated-indian-movies/'

def movies_detail():
    data = requests.get(url)
    if data.status_code ==200:
        soup=BeautifulSoup(data.text ,"html.parser")
        tbody=soup.find('tbody',class_='lister-list')
        trs=tbody.find_all('tr')
        movie_name=[]
        movie_url=[]
        for tr in trs:
            name=tr.find('td',class_='titleColumn').a.get_text()
            movie_name.append(name)
            link=tr.find("td",class_='titleColumn').a['href']
            linked=url[0:21]+link
            movie_url.append(linked)
            if  len(movie_name)==10:
                break
        release_date=[]

        def release(url):
            page= requests.get(url)
            soup=BeautifulSoup(page.text,"html.parser")
            release=soup.find("li",attrs={"data-testid":"title-details-releasedate"}).text
            return (release.split("(")[0][12:])
            
        for i in movie_url:
            x=release(i)
            release_date.append(x)

        detail = {"movie_name":"","release_date":""}
        movie_det=[]
        for i in range(len(movie_name)):
            detail["movie_name"]=movie_name[i]
            detail["release_date"]=release_date[i]
            movie_det.append(detail)
            detail = {"movie_name":"","release_date":""}
        return movie_det
    else:
        print(f"your url status code is {data.status_code} since your url is not correct")

os.environ = movies_detail()
