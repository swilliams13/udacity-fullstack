# Tournament Results
by Samantha Williams, Project 2 in [Udacity's Full Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004).

###Overview
The purpose of this project is to write a Python module that uses the PostgreSQL database to keep track of players and matches in a game tournament. It was designed to teach how to create and use databases through the use of database schemas and how to manipulate the data inside the database. This project has two parts: 
- Defining the database schema (SQL table definitions) in tournament.sql
- Writing code that will use it to track a Swiss tournament in tournament.py.


### Purpose of each file
####tournament.sql
this file is used to set up the database schema

####tournament.py
this file is used to provide access to the database via a library of functions which can add, delete or query data in your database to another python program (a client program)

####tournament_test.py
a client program to test the implementation of functions in tournament.py


###Creating Your Database
Before you can run your code or create your tables, you'll need to use the create database command in psql to create the database. Use the name tournament for your database.

Then you can connect psql to your new database and create your tables from the statements you've written in tournament.sql. You can do this in either of two ways:

- Paste each statement in to psql.
- Use the command \i tournament.sql to import the whole file into psql at once.

Remember, if you get your database into a bad state you can always drop tables or the whole database to clear it out.

###Functions in tournament.py

####registerPlayer(name)

Adds a player to the tournament by putting an entry in the database. The database should assign an ID number to the player. Different players may have the same names but will receive different ID numbers.

####countPlayers()

Returns the number of currently registered players. This function should not use the Python len() function; it should have the database count the players.

####deletePlayers()

Clear out all the player records from the database.

reportMatch(winner, loser)

Stores the outcome of a single match between two players in the database.

####deleteMatches()

Clear out all the match records from the database.

####playerStandings()

Returns a list of (id, name, wins, matches) for each player, sorted by the number of wins each player has.

####swissPairings()

Given the existing set of registered players and the matches they have played, generates and returns a list of pairings according to the Swiss system. Each pairing is a tuple (id1, name1, id2, name2), giving the ID and name of the paired players. For instance, if there are eight registered players, this function should return four pairings. This function should use playerStandings to find the ranking of players.