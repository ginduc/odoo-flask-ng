#!/usr/bin/python
# -*- coding: utf-8 -*-

import xmlrpclib

url = "http://192.168.59.103:18069"
db = "umamidb"
username = "admin"
password = "admin"

common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url))
uid = common.authenticate(db, username, password, {})

models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url))
partners = models.execute_kw(db, uid, password,
    'res.partner', 'search_read',
        [[['is_company', '=', True], ['customer', '=', True]]],
            {'fields': ['name', 'country_id', 'customer'], 'limit': 10})

for p in partners:
        print("Partners --> " + str(p['name']) + " | Country: " + str(p['country_id'][1]))
