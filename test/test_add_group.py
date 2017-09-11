# -*- coding: utf-8 -*-
__author__ = 'ivanov'


import pytest

from fixture.application import Application
from model.group import Group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.login(username="admin", password="secret")
    i = 1
    while i < 2:
        app.create_group(Group(name="testgroup1", header="test1", footer= "test1"))
        i += 1
    app.logout()

def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()
