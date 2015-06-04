import tempfile
db_file = tempfile.NamedTemporaryFile()


class Config(object):
    SECRET_KEY = 'secret key'


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../database.db'

    ODOO_HOST = 'http://192.168.59.103:18069'
    ODOO_DB = 'umamidb'
    ODOO_USER = 'admin'
    ODOO_PASS = 'admin'

    CACHE_TYPE = 'simple'


class DevConfig(Config):
    DEBUG = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    SQLALCHEMY_DATABASE_URI = 'sqlite:///../database.db'

    ODOO_HOST = 'http://192.168.59.103:18069'
    ODOO_DB = 'umamidb'
    ODOO_USER = 'admin'
    ODOO_PASS = 'admin'

    CACHE_TYPE = 'null'
    ASSETS_DEBUG = True


class TestConfig(Config):
    DEBUG = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + db_file.name
    SQLALCHEMY_ECHO = True

    ODOO_HOST = 'http://192.168.59.103:18069'
    ODOO_DB = 'umamidb'
    ODOO_USER = 'admin'
    ODOO_PASS = 'admin'

    CACHE_TYPE = 'null'
    WTF_CSRF_ENABLED = False
