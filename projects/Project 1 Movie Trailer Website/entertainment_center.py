'''Stores details of movies and displays to a webbrowser.'''

import fresh_tomatoes
import media

'''Creates six Movie objects, initialising these objects with title,
storyline,poster image link and youtube video trailer link'''
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/\
                        Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org\
                     /wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")


avengers = media.Movie("Avengers",
                       "The Avengers and their allies must\
                       be willing to sacrifice all in an \
                       attempt to defeat the powerful Thanos\
                       before his blitz of devastation and \
                       ruin puts an end to the universe.",
                       "https://upload.wikimedia.org/wikipedia\
                       /en/4/4d/Avengers_Infinity_War_poster.jpg",
                       "https://www.youtube.com/watch?v=QwievZ1Tx-8")

thor = media.Movie("Thor",
                   "The powerful, but arrogant god Thor,\
                   is cast out of Asgard to live amongst \
                   humans in Midgard (Earth), where he\
                   soon becomes one of their finest defenders.",
                   "https://upload.wikimedia.org/wikipedia\
                   /en/f/fc/Thor_poster.jpg",
                   "https://www.youtube.com/watch?v=ue80QwXMRHg")

antman = media.Movie("Ant-Man",
                     "Armed with a super-suit with the \
                     astonishing ability to shrink in scale\
                     but increase in strength, cat burglar\
                     Scott Lang must embrace his inner hero \
                     and help his mentor, Dr. Hank Pym, plan\
                     and pull off a heist that will save the world.",
                     "https://upload.wikimedia.org/wikipedia\
                     /en/7/75/Ant-Man_poster.jpg",
                     "https://www.youtube.com/watch?v=ue80QwXMRHg")

deadpool = media.Movie("DEADPOOL",
                       "A fast-talking mercenary with a morbid\
                       sense of humor is subjected to a rogue\
                       experiment that leaves him with accelerated\
                       healing powers and a quest for revenge.",
                       "https://upload.wikimedia.org/wikipedia/\
                        en/4/46/Deadpool_poster.jpg",
                       "https://www.youtube.com/watch?v=\
                        8nbUIqrrrZE")


# Store the Movie objects in a list.
movies = [toy_story, avatar, avengers, thor, antman, deadpool]
# Open the movie website in the browser,
# featuring the movies above displayed in the list.
fresh_tomatoes.open_movies_page(movies)
