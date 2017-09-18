# -*- coding: utf-8 -*-
__author__ = 'ivanov'




import pytest

from fixture.application import Application

@pytest.fixture  # (scope = "session") - not worked….
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
