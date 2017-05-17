import bs4 as bs
import urllib.request

def get_movies():
    start = "http://www.imdb.com/movies-in-theaters"
    page = urllib.request.urlopen(start).read()
    soup = bs.BeautifulSoup(page, "lxml")
    movies = soup.find_all("div", class_="list_item")

    all_movie_data = []

    for n in range(0,6):

        title_target = movies[n].find("h4", itemprop="name")
        imdb_title = title_target.find("a").get("title")
        title = imdb_title.split("(")[0]
        release_date = imdb_title.split("(")[1][0:4]
        synopsis = movies[n].find("div", class_="outline").contents[0]

        print (title)
        print (release_date)
        print ("")

        movie_page = "http://www.imdb.com" + movies[n].find("a").get("href")
        page = urllib.request.urlopen(movie_page).read()
        soup = bs.BeautifulSoup(page, "lxml")
        poster_page = "http://www.imdb.com" + soup.find("div", class_="poster").find("a").get("href")
        page = urllib.request.urlopen(poster_page).read()
        poster_id = poster_page.split("/")[6].split("?")[0]
        page = page.decode().split(poster_id)[1]
        poster_link = page[0:300].split('"')[6]

        imdb_title_split = imdb_title.split(" ")
        search_title = ""
        for word in imdb_title_split:
            if search_title == "":
                search_title += word
            else:
                search_title += "+" + word
        youtube_search = "https://www.youtube.com/results?search_query=" + search_title + "+trailer+1"
        #The read was missing on the next line and things didn't appear to be broken
        page = urllib.request.urlopen(youtube_search).read()
        soup = bs.BeautifulSoup(page, "lxml")
        trailer_youtube_url = "https://www.youtube.com" + soup.find("div", class_="yt-lockup-content").find("a", class_="yt-uix-tile-link").get("href")

        movie_data = {
            "title": title,
            "release_date": release_date,
            "synopsis": synopsis,
            "poster_link": poster_link,
            "trailer_youtube_url": trailer_youtube_url
        }

        all_movie_data.append(movie_data)

    return all_movie_data
