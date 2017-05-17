import media
import fresh_tomatoes
import scraper

movies = []

all_movie_data = scraper.get_movies()

# print (all_movie_data[0]["title"])

# movies.append(media.Movie(all_movie_data[0]["title"], all_movie_data[0]["trailer_youtube_url"], all_movie_data[0]["synopsis"], all_movie_data[0]["poster_link"]))

for n in range(0,len(all_movie_data)):

    print ("Looping: " + str(n+1))
    movies.append(media.Movie(all_movie_data[n]["title"], all_movie_data[n]["trailer_youtube_url"], all_movie_data[n]["synopsis"], all_movie_data[n]["poster_link"]))



fresh_tomatoes.open_movies_page(movies)
