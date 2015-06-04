#! ../../env/bin/python
# -*- coding: UTF-8 -*-

import xmlrpclib
from odoo import Connection
from sd5.models import Sender

import logging
log = logging.getLogger('werkzeug')

def list_partners(conn):
	models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(conn.url))
	partners = models.execute_kw(conn.db, conn.uid, conn.password,
    	'res.partner', 'search_read',
    	[[['is_company', '=', True], ['customer', '=', True]]])

	senders = []
	if partners is not None:
		for p in partners:
			senders.append(Sender(p['name']))
		
	return senders

def create_partner(conn, partner):
	models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(conn.url))
	id = models.execute_kw(db, uid, password, 'res.partner', 'create', [{
    	'name': "New Partner",
	}])

	return id
