#! ../../env/bin/python
# -*- coding: UTF-8 -*-

import xmlrpclib


class Connection:

	def __init__(self, config):
		self.url = config['ODOO_HOST']
		self.db = config['ODOO_DB']
		self.username = config['ODOO_USER']
		self.password = config['ODOO_PASS']
		
		common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(self.url))
		self.uid = common.authenticate(self.db, self.username, self.password, {})
