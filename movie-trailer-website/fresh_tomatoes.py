import webbrowser
import os
import re


# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Fresh Tomatoes!</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
       /* GLOBALS */
        body {
            background-color: steelblue;
            font-weight: 400;
            line-height: 1.8;
        }

        /* Headings */
        h1, h2, h3, h4, h5, h6 {
          line-height: 1;
          font-weight: 400; 
        }

        a {
          text-decoration: none;
          color: steelblue; 
        }

        a:hover {
          color: #315a7d; 
        }

        /* Template */
        #wrapper {
            width: 100%;
            margin: 0 auto; 
        }

        #main {
            background-color: #fff;
            padding: 30px 0; 
        }

        .container {
            width: 100%;
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 30px; 
        }

        /* Info Bar */
        #info-bar {
          background-color: #38678f; 
        }

        #info-bar a {
          color: white;
          font-size: 14px;
          text-transform: uppercase;
          display: inline-block;
          margin: 0;
          padding: 10px; 
        }

        #info-bar a:hover {
          background-color: #315a7d; 
        }

        span.back-to-home,
        span.back-to-gh {
          display: block;
          width: 50%; }

        span.back-to-home {
          float: left;
          text-align: left; }

        span.back-to-gh {
          float: right;
          text-align: right; }


        /* Header */
        header {
            padding: 30px 0;
        }

        #title {
            text-align: center;
        }
        #title h1 {
            color: #fff;
            font-size: 30px;
            margin-bottom: 10px;
        }
        #title h2 {
            color: #8db3d3;
            font-size: 20px;            
        }

        /* Footer */
        footer {
            padding: 30px 0;
            text-align: center; 
        }

        footer span {
            color: #fff; 
        }

        footer span a {
            color: #8db3d3;
        }


        /* Udacity */

        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .movie-tile:hover {
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }

        /** Figures **/
        figure {
            margin: 0;
            position: relative;
        }
        figure img {
            position: relative;
            z-index: 10;
            max-width: 100%;
            backface-visibility: hidden;
            transition: all 0.5s;
        }
        figure figcaption {
            display: block;
            position: absolute;
            z-index: 5;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: steelblue;
            text-align: center;
            backface-visibility: hidden;
            transform: rotateY(-180deg);
            transition: all 0.5s;
        }
        figure h3 {
            color: #fff;
            font-size: 22px;
            line-height: 1.2;
            font-weight: 700;
            margin-top: 25%
        }
        figure span {
            color: #b2cce1;
            display: block;
            line-height: 1.2;
        }
        figure:hover img,
        figure.hover img {
            transform: rotateY(180deg);
        }
        figure:hover figcaption,
        figure.hover figcaption {
            transform: rotateY(0);
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''


# The main page layout and title bar
main_page_content = '''
    <body>
        <div id="wrapper">
            <!-- Trailer Video Modal -->
            <div class="modal" id="trailer">
            <div class="modal-dialog">
            <div class="modal-content">
              <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
                <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
              </a>
              <div class="scale-media" id="trailer-video-container">
              </div>
            </div>
            </div>
            </div>

            <!-- Main Page Content -->
            <div id="info-bar">
                <div class="container">
                    <span class="back-to-home">
                        <a href="http://swilliams13.github.io"><- Back to Main Site</a>
                    </span>
                    <span class="back-to-gh">
                        <a href="https://github.com/swilliams13/udacity-fullstack/tree/master/project1">View on GitHub</a>
                    </span>
                </div>
            </div>
            <header>
                <div id="title" class="container">
                    <h1>Fresh Tomatoes Movie Trailers</h1>
                </div>
            </header>
            <div id="main">
                <div class="container">
                    {movie_tiles}
                </div>
            </div>
            <footer>
                <div class="container">
                    <span> &copy; 2015, Samantha Williams
                    <br>
                    <a href="http://swilliams13.github.io" target="_blank">swilliams13.github.io</a> </span>
                </div>
            </footer>
        </div>
    </body>
</html>
'''


# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <figure>
        <img src="{poster_image_url}" width="220" height="342">
        <figcaption>
            <h3>{movie_title}</h2>
            <span>Stars: {movie_stars}</span>
            <span>Release Date: {movie_release}</span>
        </figcaption>
    </figure>
</div>
'''


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            movie_stars=movie.actors,
            movie_release=movie.release_date
        )
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
