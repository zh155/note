import os

from flask_migrate import MigrateCommand
from flask_script import Manager

from flask_tpp import create_app

env = os.environ.get('FLASK_ENV', 'default')

app = create_app(env)

manager = Manager(app)
manager.add_command("db", MigrateCommand)


@app.route('/')
def index():
    return 'hello'


if __name__ == '__main__':
    manager.run()
