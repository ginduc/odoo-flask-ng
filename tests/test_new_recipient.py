#! ../env/bin/python
# -*- coding: utf-8 -*-

import pytest

@pytest.mark.usefixtures("testapp")
class TestNewRecipient:
    def test_submission(self, testapp):
        """ Tests if the new recipient form functions """

        rv = testapp.post('/recipient/new', data=dict(
            firstname = 'Ned',
            lastname = 'Flanders',
            mobileNo = '+639176215342',
            address = '123 Main st'
        ), follow_redirects=True)

        assert rv.status_code == 200
        assert rv.data

    def test_submission_failed(self, testapp):
        """ Tests if the search form validates keyword correctly """

        rv = testapp.post('/recipient/new', data=dict(
            firstname = 'Clancy',
            lastname = 'Wiggum',
            #mobileNo = '+639196215342',
            address = '456 Main st'
        ), follow_redirects=True)

        assert rv.status_code == 200
        assert 'This field is required' in str(rv.data)
