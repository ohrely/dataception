from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Player(db.Model):
    """Individual team members.
    """
    __tablename__ = "players"

    name = db.Column(db.String(24), primary_key=True)

    def __repr__(self):

        return "<Player name={}>".format(self.name)


class Level(db.Model):
    """Information about each level of the dream.
    """
    __tablename__ = "levels"

    level_num = db.Column(db.Integer, primary_key=True)
    level_name = db.Column(db.String(24))
    dreamer = db.Column(db.String(24), db.ForeignKey('players.name'))

    dreamer_rel = db.relationship('Player', foreign_keys='Level.dreamer')

    def __repr__(self):

        return "<Level level_name={} dreamer={}>".format(self.level_name, self.dreamer)


class PlayerLevel(db.Model):
    """Relational table to track players' level of depth in dreams.
    """
    __tablename__ = "playerlevels"

    tracker = db.Column(db.Integer, primary_key=True, autoincrement=True)
    level_num = db.Column(db.Integer, db.ForeignKey('levels.level_num'))
    player = db.Column(db.String(24), db.ForeignKey('players.name'))

    def __repr__(self):

        return "<Level level_num={} player={}>".format(self.level_num, self.player)


def connect_to_db(app):
    """Connect the database to the Flask app"""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inception.db'
    db.app = app
    db.init_app(app)
    db.create_all()


if __name__ == "__main__":

    from server import app
    connect_to_db(app)
    print "Connected to DB."
