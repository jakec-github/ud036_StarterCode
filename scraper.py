import bs4 as bs
import urllib.request

# Takes the top movies from imdb.com/movies-in-theaters and collects their data
# returns a list of dictionaries with the following keys:
# "title", "release_date", "synopsis", "poster_link", "trailer_youtube_url"
def get_movies():
    # Locates movie information on webpage
    start = "http://www.imdb.com/movies-in-theaters"
    page = urllib.request.urlopen(start).read()
    soup = bs.BeautifulSoup(page, "lxml")
    movies = soup.find_all("div", class_="list_item")

    all_movie_data = []
    # Loops through movies on the page starting at the top.
    # Number of movies can be adjusted by adjusting range. 15 movies max
    for n in range(0,4):
        # Retrieves title, release date and the synopsis
        title_target = movies[n].find("h4", itemprop="name")
        imdb_title = title_target.find("a").get("title")
        title = imdb_title.split("(")[0]
        release_date = imdb_title.split("(")[1][0:4]
        synopsis = movies[n].find("div", class_="outline").contents[0]

        print (title)
        print (release_date)
        print ("")

        # Retrieves poster
        homepage = "http://www.imdb.com"
        movie_page = homepage + movies[n].find("a").get("href")
        page = urllib.request.urlopen(movie_page).read()
        soup = bs.BeautifulSoup(page, "lxml")
        relative_link = soup.find("div", class_="poster").find("a").get("href")
        poster_page = homepage + relative_link
        page = urllib.request.urlopen(poster_page).read()
        poster_id = poster_page.split("/")[6].split("?")[0]
        page = page.decode().split(poster_id)[1]
        poster_link = page[0:300].split('"')[6]

        # Retrieves trailer url
        imdb_title_split = imdb_title.split(" ")
        search_title = ""
        for word in imdb_title_split:
            if search_title == "":
                search_title += word
            else:
                search_title += "+" + word
        base_url = "https://www.youtube.com/results?search_query="
        youtube_search = base_url + search_title + "+trailer+1"
        page = urllib.request.urlopen(youtube_search).read()
        soup = bs.BeautifulSoup(page, "lxml")
        video_target = soup.find("div", class_="yt-lockup-content")
        video = video_target.find("a", class_="yt-uix-tile-link").get("href")
        trailer_youtube_url = "https://www.youtube.com" + video

        movie_data = {
            "title": title,
            "release_date": release_date,
            "synopsis": synopsis,
            "poster_link": poster_link,
            "trailer_youtube_url": trailer_youtube_url
        }

        all_movie_data.append(movie_data)

    return all_movie_data
