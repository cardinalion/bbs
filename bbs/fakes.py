from bbs.models import User, Category
from bbs.extensions import db


def first_admin():
    admin = User(
        username='admin',
        motto='welcome'
    )
    admin.set_password('ADMIN')
    db.session.add(admin)
    db.session.commit()


def some_categories():
    db.session.add(Category(name='News'), Category(name='Sports'), Category(name='Economics'),
                   Category(name='Technology'), Category(name='Entertainment'), Category(name='Games'),
                   Category(name='Books'), Category(name='Health'), Category(name='Cars'), Category(name='Music'),
                   Category(name='History'), Category(name='Travel'), Category(name='Lifestyle'))
    db.session.commit()
