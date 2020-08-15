from app import create_app, db
from app.models import User, Post, Message, Notification


app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post,
            'Message': Message, 'Notification': Notification}

# TODO: Add user search
# TODO: Make the form more user-friendly by adding error message
# TODO: Fix 500 page
