from flask_script import Manager
from flask_migrate import MigrateCommand

from application.app import create_app
from application.extensions import db
from models.model import User, Post


app = create_app('application.config.Config')
manager = Manager(app)


@manager.command
def create_db():
    """
    Create Database
    """
    db.create_all()


@manager.command
def drop_db():
    """
    Drop Database
    """
    db.drop_all()


manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()

