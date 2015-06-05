import pytest

from sd5 import create_app
from sd5.models import db, User


@pytest.fixture()
def testapp(request):
    app = create_app('sd5.settings.TestConfig', env='dev')
    client = app.test_client()

    db.app = app
    db.create_all()

    if getattr(request.module, "create_user", True):
        admin = User('admin', 'supersafepassword')
        db.session.add(admin)
        db.session.commit()

    def teardown():
        db.session.remove()
        db.drop_all()

    request.addfinalizer(teardown)

    return client

@pytest.fixture()
def testappcfg():
    app = create_app('sd5.settings.TestConfig', env='dev')
    return app