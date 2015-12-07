from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Player(db.Model):
    """Individual team members.
    """
    __tablename__ = "players"

    name = db.Column(db.String(24), primary_key=True)

    def __repr__(self):

        return "<Player name={}>".format(self.name)


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
