"""Inception, represented through data structures in python.

For fun and practice.
"""

from model import connect_to_db, db
from model import Level, Player, PlayerLevel
import doctest


def intception():
    """
    >>> intception()
    528 491
    """
    dream = 528
    team = 491

    print dream, team


def stringception():
    """

    >>> stringception()
    a dream within a dream within a dream within a dream
    """
    paradox = "a dream within a dream"

    plot = paradox.join(paradox.split("a dream"))

    print plot


def listception(level):
    """Creates a list of the team members at the given level.

    >>> listception(1)
    [u'Ariadne', u'Arthur', u'Dom', u'Eames', u'Fischer', u'Saito', u'Yusuf']
    """
    level_players = db.session.query(PlayerLevel.player).filter(PlayerLevel.level_num == level).all()

    level_list = []

    for player in level_players:
        level_list.append(player[0])

    print level_list


def tupception():
    """

    >>> tupception()
    [(0, u'Reality'), (1, u'Warehouse'), (2, u'Hotel'), (3, u'Fortress'), (4, u'Limbo')]
    """

    level_tups = db.session.query(Level.level_num, Level.level_name).all()

    return level_tups


def setception():
    """Do set math with listception.

    >>> setception()

    """
    pass


def dictception():
    """Nested dictionary model of dream(ers) within a dream(er).

    # each team member is a key in the base dict.
    # at each level, the dreamer's value is a dict of the team members on that level.
    # build recursively?

    >>> dictception()

    """
    real_world = {}



    print real_world


def graphception():
    """map who knows who - will need another association table.

    >>> graphception()

    """
    pass


def treeception():
    """

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


def linkception():
    """Doubly-linked list of dream order.

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
