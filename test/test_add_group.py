# -*- coding: utf-8 -*-
__author__ = 'ivanov'



from model.group import Group

def test_add_group(app):
    app.session.login(username="admin", password="secret")
    i = 1
    while i < 2:
        app.group.create(Group(name="testgroup1", header="test1", footer= "test1"))
        i += 1
    app.session.logout()

def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
