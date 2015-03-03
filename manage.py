from flask.ext.script import Manager, prompt_bool
from www import app

##### GLOBALS
manager = Manager(app)

if __name__ == '__main__':
	manager.run()