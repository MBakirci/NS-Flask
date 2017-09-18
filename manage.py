# manage.py

from flask_script import Manager
import ns

app = ns.create_app()
manager = Manager(app)

if __name__ == '__main__':
    manager.run()
