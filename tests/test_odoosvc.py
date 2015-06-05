#! ../env/bin/python
# -*- coding: utf-8 -*-

import pytest
from sd5 import create_app
from sd5.models import Sender
from odoorpc import Connection
from odoorpc.partner_svc import (
	list_partners, 
	create_partner,
	get_partner
) 


@pytest.mark.usefixtures("testappcfg")
class TestOdooSvc:
    def test_lookup_sender(self, testappcfg):
        """ Test sender lookup on Odoo """

        conn = Connection(testappcfg.config)
        partners = list_partners(conn)

        assert partners is not None
        assert len(partners) > 0

    def test_create_sender(self, testappcfg):
    	""" Test create sender on Odoo """

        conn = Connection(testappcfg.config)
        sender = Sender("Ned Flanders")
        sender_id = create_partner(conn, sender)

        assert sender_id is not None
        assert sender_id > 0

        assert get_partner(conn, sender_id) is not None

    def test_get_partner_fail(self, testappcfg):
    	""" Test partner not found on Odoo """

        conn = Connection(testappcfg.config)

        assert get_partner(conn, -1) is None