class Movie:

    def __init__(self, title, poster_image_url, trailer_youtube_url):

        """
        :param title: Readable string that gives title of movie
        :param poster_image_url: Image that depicts the movie cover
        :param trailer_youtube_url: Video that gives preview of movie
        """
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
