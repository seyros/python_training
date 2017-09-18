# -*- coding: utf-8 -*-
__author__ = 'ivanov'

def test_delete_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.delete_first_groupe()
    app.session.logout()
