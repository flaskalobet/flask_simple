import os
from app import create_app
from flask.ext.script import Manager, Shell

app = create_app(os.getenv('FLASK_CONFIG') or 'development')
manager = Manager(app)

if __name__ == '__main__':
    manager.run()
