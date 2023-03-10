import os
from app import create_app, db
from app.models import User, Post, Comment, Message, Notification, Task
from flask_migrate import Migrate


app = create_app(os.getenv("FLASK_CONFIG"))
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return {
        "db": db,
        "User": User,
        "Post": Post,
        "Comment": Comment,
        "Message": Message,
        "Notification": Notification,
        "Task": Task,
    }


@app.cli.command()
def test():
    """Run the unit tests."""

    import unittest

    tests = unittest.TestLoader().discover("tests")
    unittest.TextTestRunner(verbosity=2).run(tests)
