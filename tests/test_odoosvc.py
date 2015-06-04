#! ../env/bin/python
# -*- coding: utf-8 -*-

import pytest
from sd5 import create_app
from odoorpc import Connection
from odoorpc.partner_svc import list_partners
import logging
log = logging.getLogger('werkzeug')

class TestOdooSvc:
    def test_sender_lookup(self):
        """ Test sender lookup on Odoo RPC """

        app = create_app('sd5.settings.TestConfig', env='dev')
        conn = Connection(app.config)
        partners = list_partners(conn)

        app.logger.error("=-=-=-=-=-=-=-=-=-=-> " + str(partners))

        assert partners is not None
        assert len(partners) > 0
