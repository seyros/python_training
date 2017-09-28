# -*- coding: utf-8 -*-
__author__ = 'ivanov'
from model.group import Group
from random import randrange

def test_delete_some_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    app.group.delete_group_by_index(index)
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)  # проверка, что новый список групп на 1 элемент короче
    old_groups[index:index+1] = []  # удаляем случайный элемент из старого списка групп
    assert old_groups == new_groups # проверяем, что новый список групп равен старому списку, из которого удалили один элемент
