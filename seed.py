from model import Player, Level, PlayerLevel
from model import connect_to_db, db
import doctest


def add_players(player_data):
    """Seed players from csv to db."""

    print("Players")

    Player.query.delete()

    for row in open(player_data):
        row = row.rstrip()
        row = row.split(",")

        name = row[0]

        player = Player(name=name)

        db.session.add(player)

    db.session.commit()


def add_levels(level_data):
    """Seed levels from csv to db."""

    print("Levels")

    Level.query.delete()

    for row in open(level_data):
        row = row.rstrip()
        row = row.split(",")

        level_num = row[0]
        level_name = row[1]
        dreamer = row[2]

        level = Level(level_num=level_num, level_name=level_name, dreamer=dreamer)

        db.session.add(level)

    db.session.commit()


def add_playerlevels(playerlevel_data):
    """Seed player levels from csv to db."""

    print("PlayerLevels")

    PlayerLevel.query.delete()

    for row in open(playerlevel_data):
        row = row.rstrip()
        row = row.split(",")

        level_num = row[0]
        player = row[1]

        playerlevel = PlayerLevel(level_num=level_num, player=player)

        db.session.add(playerlevel)

    db.session.commit()


if __name__ == "__main__":

    from server import app
    connect_to_db(app)

    doctest.testmod(verbose=True)

    add_players("data/players.txt")
    add_levels("data/levels.txt")
    add_playerlevels("data/playerlevels.txt")
