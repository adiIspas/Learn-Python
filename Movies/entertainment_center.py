import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", "A story of a boy ...",
                        "https://goo.gl/DBTDda",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar", "A marine on an ...",
                     "https://goo.gl/F0PTg7",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

movies = [toy_story, avatar]
fresh_tomatoes.open_movies_page(movies)
print(media.Movie.__doc__)