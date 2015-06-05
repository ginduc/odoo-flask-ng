#! ../env/bin/python
# -*- coding: utf-8 -*-

import pytest
from sd5 import create_app
from sd5.models import Sender
from odoorpc import Connection
from odoorpc.partner_svc import (
    list_partners, 
    create_partner,
    get_partner,
    search_partners,
    delete_partner,
    update_partner
) 


@pytest.mark.usefixtures("testappcfg")
class TestOdooSvc:

    def test_lookup_sender(self, testappcfg):
        """ Test sender lookup on Odoo """

        conn = Connection(testappcfg.config)
        partners = list_partners(conn)

        assert partners is not None
        assert len(partners) > 0

    def test_create_update_delete_sender(self, testappcfg):
        """ Test create sender on Odoo """

        test_sender_name = "Ned Flanders"

        conn = Connection(testappcfg.config)
        sender = Sender(None, test_sender_name)
        sender_id = create_partner(conn, sender)

        assert sender_id is not None
        assert sender_id > 0

        persistent = get_partner(conn, sender_id)
        assert persistent is not None
        assert persistent.id is not None
        assert persistent.name is not None

        persistent.name = "Maud Flanders"
        assert update_partner(conn, persistent) is True
        assert len(search_partners(conn, persistent.name)) > 0

        assert delete_partner(conn, persistent.id) is True

    def test_get_partner_fail(self, testappcfg):
        """ Test partner not found on Odoo """

        conn = Connection(testappcfg.config)

        assert get_partner(conn, -1) is None

    def test_update_partner_fail(self, testappcfg):
        """ Test failed update partner on Odoo """

        conn = Connection(testappcfg.config)

        assert update_partner(conn, Sender(-1, None)) is False

    def test_delete_partner_fail(self, testappcfg):
        """ Test failed delete partner on Odoo """

        conn = Connection(testappcfg.config)

        assert delete_partner(conn, -1) is False

    def test_search_partner_fail(self, testappcfg):
        """ Test failed search partner on Odoo """

        conn = Connection(testappcfg.config)

        assert len(search_partners(conn, "Kingslayer Inc")) == 0
