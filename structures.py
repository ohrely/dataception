"""Inception, represented through data structures in python.

For fun and practice.
"""

from model import connect_to_db, db
from model import Level, Player, PlayerLevel
import doctest


def intception():
    """Prints sequence of numbers from the film.

    >>> intception()
    528 491
    """
    dream = 528
    team = 491

    return dream, team


def stringception():
    """Fun with .join() and .split()

    >>> stringception()
    'a dream within a dream within a dream within a dream'
    """
    paradox = "a dream within a dream"

    plot = paradox.join(paradox.split("a dream"))

    return plot


def listception(level):
    """Creates a list of the team members at the given level.

    >>> listception(1)
    [u'Ariadne', u'Arthur', u'Dom', u'Eames', u'Fischer', u'Saito', u'Yusuf']
    """
    level_players = db.session.query(PlayerLevel.player).filter(PlayerLevel.level_num == level).all()

    level_list = []

    for player in level_players:
        level_list.append(player[0])

    return level_list


def tupception():
    """DB query of levels.

    >>> tupception()
    [(0, u'Reality', u''), (1, u'Warehouse', u'Yusuf'), (2, u'Hotel', u'Arthur'), (3, u'Fortress', u'Eames'), (4, u'Limbo', u'')]
    """

    level_tups = db.session.query(Level.level_num, Level.level_name, Level.dreamer).order_by(Level.level_num).all()

    return level_tups


class LevelObj(object):
    """More modular alternative to tupception."""

    def __init__(self, level_num):
        self.level_num = level_num
        self.get_attributes()
        self.get_players()

    def get_attributes(self):
        self.level_name, self.dreamer = db.session.query(Level.level_name, Level.dreamer).filter(Level.level_num == self.level_num).one()

    def get_players(self):
        self.players_list = listception(self.level_num)

    def __repr__(self):
        return "<LevelObj level_num={} level_name={}>".format(self.level_num, self.level_name)


def setception(level):
    """Use set math with listception to find which players stop at a level.

    >>> setception(2)
    set([u'Arthur'])
    """
    this_level = set(listception(level))
    next_level = set(listception(level + 1))

    stays_behind = this_level.difference(next_level)

    return stays_behind


def dictception(mind_dict=None, levels=None):
    """Nested dictionary model of dream(ers) within a dream(er).

    # each team member is a key in the base dict.
    # at each level, the dreamer's value is a dict of the team members on that level.
    # build recursively?

    >>> dictception()

    """
    # setup
    if not mind_dict:
        mind_dict = {}

    if not levels:
        levels = tupception()

    # base case
    if len(levels) == 1:
        pass

    # recursive call
    if len(levels) > 1:
        this_level = levels[0]
        next_level = levels[1]

        level_num = this_level[0]
        dreamer = next_level[2]

        for player in listception(level_num):
            mind_dict[player] = None

        mind_dict[dreamer] = {}

        print mind_dict

    return mind_dict


def graphception():
    """map who knows who - will need another association table.

    >>> graphception()

    """
    pass


class PlayerObj(object):
    """"""
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "PlayerObj name={}".format(self.name)


class DreamerObj(PlayerObj):
    """Sub-class of PlayerObj for working just with characters who dream."""

    def __init__(self):
        # TODO: look up __init__ collisions
        pass


def treeception():
    """Tree of player participation in each others' minds.

    >>> treeception()

    """

    pass


def stackception(dreamer):
    """Dreamers' experience of dream order.

    some variable better be named non_rien_nest_rien.

    >>> stackception("Arthur")

    """
    pass


def queueception():
    """
    >>> queueception()

    """

    pass


class DoubLinkCeption(object):
    """Doubly-linked layer list."""

    def __init__(self):
        pass


def linkception():
    """Given dream layer, returns list of layers that lead to it.  Doubly-linked list of dream order.

    why doubly linked?  because dreamers have to kick back out of the dreams in order.

    >>> linkception()

    """
    dreams = None

    return dreams


if __name__ == "__main__":
    from server import app
    connect_to_db(app)
    print "Connected to DB."

    doctest.testmod(verbose=True)
