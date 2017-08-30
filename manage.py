from flask_migrate import Migrate, MigrateCommand, Manager
from app import db
from run import app


migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()