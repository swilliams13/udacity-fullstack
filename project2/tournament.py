#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
@contextlib.contextmanager

def get_cursor():
    """ Helper function to get database cursor """
    conn = connect()
    c = conn.cursor()
    try:
        yield c
    except:
        raise
    else
        conn.commit()
    finally:
        c.close()
        conn.close()

def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    with get_cursor() as c:
        c.execute("delete from matches where id > 0;")
    
def deletePlayers():
    """Remove all the player records from the database."""
    with get_cursor() as c:
        c.execute("delete from players where id > 0;")
    
def countPlayers():
    """Returns the number of players currently registered."""
    with get_cursor() as c:
        c.execute("select count(*) as num from players;")
        count = c.fetchone()
    
    return count[0]


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    with get_cursor() as c:
        c.execute("insert into players (name) values (%s);", (name,))
    
    
def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a
    player tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    with get_cursor() as c:
        c.execute("select * from standings;")
        standings = list(c.fetchall())
    
    return standings


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    with get_cursor() as c:
        c.execute(
        "insert into matches (winner_id, loser_id) values (%s, %s)",
        (winner, loser))
    


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player
    adjacent to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    with get_cursor() as c:
        c.execute("select distinct a.id, a.name, b.id, b.name from standings as a,"
              "standings as b where a.wins=b.wins and a.id < b.id")
        standings = list(c.fetchall())
    
    return standings
