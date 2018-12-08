import fresh_tomatoes
import media
ToyStory = media.Movie ("Toy Story",
					   "A story about a boy and his toys that come to live.",
					   "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
					   "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print (ToyStory.title)
#print(ToyStory.storyline)
Avatar = media.Movie ("Avatar",
					  "A marine on an alien planet.",
					  "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
					  "https://www.youtube.com/watch?v=5PSNL1qE6VY")
#print(Avatar.title)
#print(Avatar.storyline)
#Avatar.show_trailer()

Moana = media.Movie("Moana",
					"A story about Moana and Maui's adventure.",
					"https://upload.wikimedia.org/wikipedia/en/2/26/Moana_Teaser_Poster.jpg",
					"https://www.youtube.com/watch?v=GBPymoyCjjc")
#print(Moana.title)
#print(Moana.storyline)
#Moana.show_trailer()
Coco = media.Movie ("Coco",
					"A story about a little boy's adventure in the underworld.",
					"https://upload.wikimedia.org/wikipedia/en/9/98/Coco_%282017_film%29_poster.jpg",
					"https://www.youtube.com/watch?v=Ga6RYejo6Hk")

LeapYear = media.Movie ("Leap year",
						"A story about a girl who trys to propose to her boyfriend.",
						"https://upload.wikimedia.org/wikipedia/en/d/da/Leap_year_poster.jpg",
						"https://www.youtube.com/watch?v=HrlQBsd8LsE")

BeforeSunrise = media.Movie("Before sunrise",
							"A story about a man and a woman falling in love in Vienna.",
							"https://upload.wikimedia.org/wikipedia/en/d/da/Before_Sunrise_poster.jpg",
							"https://www.youtube.com/watch?v=25v7N34d5HE")
movies = [ToyStory, Avatar, Moana, Coco, LeapYear, BeforeSunrise]
fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
#print(media.Movie.__doc__)