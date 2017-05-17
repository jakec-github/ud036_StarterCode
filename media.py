import webbrowser


class Movie:

    def __init__(self, title, trailer, synopsis, poster):
        self.title = title
        self.trailer_youtube_url = trailer
        self.synopsis = synopsis
        self.poster_image_url = poster
