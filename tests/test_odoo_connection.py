#! ../env/bin/python
# -*- coding: utf-8 -*-

import pytest
from sd5 import create_app
from odoorpc import Connection


class TestOdooConnection:
    def test_connection(self):
        """ Test successful connection to Odoo RPC """

        app = create_app('sd5.settings.TestConfig', env='dev')
        conn = Connection(app.config)
        uid = conn.uid
        db = conn.db
        url = conn.url
        username = conn.username
        password = conn.password

        assert uid is not None
        assert db is not None
        assert url is not None
        assert username is not None
        assert password is not None
