import media
import fresh_tomatoes

# Create a instance of movie with the movies details
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Sto"
                        "ry.jpg", "http://www.youtube.com/watch?v=vwyZH85NQC4",
                        "Tom Hanks,Tim Allen,Don Rickles", "11/22/1995")

avatar = media.Movie("Avatar", "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Ava"
                     "tar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY",
                     "Sam Worthington, Zoe Saldana, Sigourney Weaver",
                     "12/18/2009")

school_of_rock = media.Movie("School of Rock",
                             "Using rock music to learn",
                             "https://upload.wikimedia.org/wikipedia/en/thumb/"
                             "1/11/School_of_Rock_Poster.jpg/220px-School_of_R"
                             "ock_Poster.jpg",
                             "https://www.youtube.com/watch?v=XCwy6lW5Ixc",
                             "Jack Black, Mike White, Joan Cusack",
                             "10/3/2003")

ratatouille = media.Movie("Ratatouille", "A rat is a chef in Paris",
                          "https://upload.wikimedia.org/wikipedia/en/thumb/5/"
                          "50/RatatouillePoster.jpg/220px-RatatouillePoster."
                          "jpg",
                          "https://www.youtube.com/watch?v=uVeNEbh3A4U",
                          "Brad Garrett, Lou Romano, Patton Oswalt",
                          "6/29/2007")

midnight_in_paris = media.Movie("Midnight in Paris",
                                "Going back in time to meet authors",
                                "https://upload.wikimedia.org/wikipedia/en/"
                                "thumb/9/9f/Midnight_in_Paris_Poster.jpg/215px"
                                "-Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=FAfR8omt-CY",
                                "Owen Wilson, Rachel McAdams, Kathy Bates",
                                "6/10/2011")

hunger_games = media.Movie("Hunger Games", "A really real reality show",
                           "https://upload.wikimedia.org/wikipedia/en/thumb/4/"
                           "42/HungerGamesPoster.jpg/220px-HungerGamesPoster."
                           "jpg",
                           "https://www.youtube.com/watch?v=4S9a5V9ODuY",
                           "Jennifer Lawrence, Josh Hutcherson, Liam "
                           "Hemsworth", "3/23/2012")

love_and_bball = media.Movie("Love and Basketball",
                             "Two childhood friends who love basketball "
                             "players begin to fall for each other",
                             "https://upload.wikimedia.org/wikipedia/en/0/02/"
                             "LBmoviePoster.jpg",
                             "https://www.youtube.com/watch?v=Ur83i6_BjbE",
                             "Sanaa Lathan, Omar Epps", "4/21/2000")

up = media.Movie("Up", "An old man travels to Paradise Falls in his home "
                 "equipped with balloons, inadvertently taking a young "
                 "stowaway.",
                 "https://upload.wikimedia.org/wikipedia/en/thumb/0/05/Up_%2820"
                 "09_film%29.jpg/220px-Up_%282009_film%29.jpg",
                 "https://www.youtube.com/watch?v=pkqzFUhGPJg",
                 "Edward Asner, Jordan Nagai, John Ratzenberger", "5/29/2009")


# Add all insances to movie array to be passed to web site
movies = [toy_story, avatar, school_of_rock,
          ratatouille, midnight_in_paris, hunger_games, love_and_bball, up]

# Pass movies to script that builds out HTML structure
fresh_tomatoes.open_movies_page(movies)
