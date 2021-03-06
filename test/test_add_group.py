# -*- coding: utf-8 -*-
__author__ = 'ivanov'



from model.group import Group
import pytest
import random
import string


def random_string(prefix, maxlen):
#    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 20))
    for i in range(5)
]

@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
    old_groups = app.group.get_group_list()
#    group = Group(name="testgroup1", header="test1", footer= "test1")
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count() # проверка что длина старого списка групп на 1 меньше длины нового списка
    new_groups = app.group.get_group_list()
    old_groups.append(group) # к старому списку групп добавляем новую группу
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max) # сравним отсортированные списки групп
#
# def test_add_empty_group(app):
#     old_groups = app.group.get_group_list()
#     group = Group(name="", header="", footer="")
#     app.group.create(group)
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) + 1 == len(new_groups)
#     old_groups.append(group) # к старому списку групп добавляем новую группу
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max) # сравним отсортированные списки групп
