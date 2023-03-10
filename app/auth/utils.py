import hashlib
from flask_login import LoginManager, current_user

from app.auth.models import UserAuth


def create_login_manager():
    """"""
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    return login_manager


login_manager = create_login_manager()


@login_manager.user_loader
def load_user(user_id):
    """Load user."""
    return UserAuth.select().where(UserAuth.id == user_id).first()


def check_permissions(current_user_id: int, user_id=None):
    if user_id is not None and current_user == UserAuth.select().where(UserAuth.id == user_id).first():
        return True

    user = UserAuth.select().where(UserAuth.id == current_user_id).first()
    if user.role.name != 'admin':
        return False

    return True


def get_avatar(email: str, size: int = 100):
    digest = hashlib.md5(email.lower().encode('utf-8')).hexdigest()
    url = f'https://www.gravatar.com/avatar/{digest}?d=identicon&s={size}'
    return url
