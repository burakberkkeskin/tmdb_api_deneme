import requests
import json
import os
import msvcrt as m




def menu():
    apitoken = "abd45a45ac4dd544c545bff58aba6d8a"
    os.system("cls")
    while(True):
        print("Dizi-Film Uygulamasına Hoş Geldin".center(50, "*"))
        selection = int(input("1-Film Arama\n2-Popular Filmler\n3-Vizyondaki Filmler\n4-Çıkış\nSeçiminiz: "))
        if selection == 1:
            searchFilm(apitoken)
        elif selection == 2:
            pFilms(apitoken)
        elif vFilms == 3:
            pass
        elif selection == 4:
            break
        else:
            menu()

def backtoMenu():
    print("Ana Menüye Dönmek İçin Herhangi Bir Tuşa Basınız")
    m.getch()
    menu()
  
def searchFilm(apitoken):
    os.system("cls")
    filmNames = []
    query = input("Aratmak İstediğiniz Kelimeyi Giriniz:")
    url = requests.get(f"https://api.themoviedb.org/3/search/keyword?api_key={apitoken}&query={query}")
    content = json.loads(url.text)
    for i in content["results"]:
        filmNames.append(i["name"])
    for i in filmNames:
        print(i)
    backtoMenu()

def pFilms(apitoken):
    os.system("cls")
    url = requests.get(f"https://api.themoviedb.org/3/movie/popular?api_key={apitoken}&language=tr-tr")
    content = json.loads(url.text)
    for i in content["results"]:
        print(f"\nFilm İsmi: {i['original_title']} Popülerlik Puanı {i['popularity']} Orjinal Dili {i['original_language']}  Çıkış Tarihi {i['release_date']} Yetişkin Filmi {i['adult']} \nFilm Açıklaması: {i['overview']} \n\n")

def vFilms(apitoken):
    print("Vizyondaki Filmlerin Apisini Bulamadım xD")



menu()