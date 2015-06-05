#! ../env/bin/python
# -*- coding: utf-8 -*-

import pytest


@pytest.mark.usefixtures("testapp")
class TestSenderRoutes:
    def test_search(self, testapp):
        """ Tests if the search form functions """

        rv = testapp.get('/sender/search', data=dict(
            keyword='123'
        ), follow_redirects=True)

        assert rv.status_code == 200
        assert rv.data

    def test_search_fail_invalid_keyword_length(self, testapp):
        """ Tests if the search form validates keyword correctly """

        rv = testapp.get('/sender/search', data=dict(
            keyword='12'
        ), follow_redirects=True)

        assert rv.status_code == 200
        assert 'Search keywords must have at least three (3) characters' in str(rv.data)

    def test_listing(self, testapp):
        """ Tests if the sender listing functions """

        rv = testapp.get('/senders', None, follow_redirects=True)

        assert rv.status_code == 200
        assert len(rv.data) > 0