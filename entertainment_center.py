from media import Movie

# movie objects instantiated from the Movie class
star_wars = Movie("Star Wars: The Force Awakens",
    "https://vignette2.wikia.nocookie.net/starwars/images/f/fd/Star_Wars_Episode_VII_The_Force_Awakens"
    ".jpg/revision/latest?cb=20151018162823",
    "https://www.youtube.com/watch?v=sGbxmsDFVnE")

pirates_1 = Movie("Pirates of the Caribbean: Curse of the Black Pearl",
    "https://i.jeded.com/i/pirates-of-the-caribbean-1-the-curse-of-the-black-pearl.12323.jpg",
    "https://www.youtube.com/watch?v=naQr0uTrH_s")

lotr = Movie("Lord of The Rings: The Two Towers",
    "https://upload.wikimedia.org/wikipedia/en/a/ad/Lord_of_the_Rings_-_The_Two_Towers.jpg",
    "https://www.youtube.com/watch?v=LbfMDwc4azU")

cap_1 = Movie("Captain America: The First Avenger",
    "https://upload.wikimedia.org/wikipedia/en/3/37/Captain_America_The_First_Avenger_poster.jpg",
    "https://www.youtube.com/watch?v=JerVrbLldXw")

avengers_2 = Movie("Avengers: Age of Ultron",
    "https://upload.wikimedia.org/wikipedia/en/1/1b/Avengers_Age_of_Ultron.jpg",
    "https://www.youtube.com/watch?v=tmeOjFno6Do")

thor_3 = Movie("Thor: Ragnarok",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMjMyNDkzMzI1O"
    "F5BMl5BanBnXkFtZTgwODcxODg5MjI@._V1_UY1200_CR90,0,630,1200_AL_.jpg",
    "https://www.youtube.com/watch?v=ue80QwXMRHg")


movie_list = list()

# adding movies to a list to be used by fresh_tomatoes
movie_list.append(star_wars)
movie_list.append(pirates_1)
movie_list.append(lotr)
movie_list.append(cap_1)
movie_list.append(avengers_2)
movie_list.append(thor_3)
