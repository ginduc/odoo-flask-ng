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
	id = models.execute_kw(conn.db, conn.uid, conn.password, 'res.partner', 'create', [{
    	'name': partner.name,
	}])

	return id

def get_partner(conn, partner_id):
	models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(conn.url))
	p = models.execute_kw(conn.db, conn.uid, conn.password, 'res.partner', 'read', [partner_id])
	
	if p:
		return Sender(p['name'])
	else:
		return None

def delete_partner(conn, partner_id):
	models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(conn.url))
	p = models.execute_kw(conn.db, conn.uid, conn.password, 'res.partner', 'read', [partner_id])
	
	if p:
		models.execute_kw(db, uid, password, 'res.partner', 'unlink', [[partner_id]])
		search = models.execute_kw(db, uid, password, 'res.partner', 'search', [[['id', '=', partner_id]]])
		return len(search) == 0
	else:
		return False

def search_partner(conn, keyword):
	models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(conn.url))
	partners = models.execute_kw(conn.db, conn.uid, conn.password,
    	'res.partner', 'search_read', [[['name', '=', keyword]]])

	senders = []
	if partners is not None:
		for p in partners:
			senders.append(Sender(p['name']))
		
	return senders