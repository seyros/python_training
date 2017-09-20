# -*- coding: utf-8 -*-
__author__ = 'ivanov'



from model.group import Group

def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test_name", header="test_header"))
    app.group.modify_first_group(Group(name = "New group"))

def test_modify_group_header(app):
    app.group.modify_first_group(Group(header = "New header"))