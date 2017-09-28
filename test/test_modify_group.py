# -*- coding: utf-8 -*-
__author__ = 'ivanov'



from model.group import Group

def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test_name", header="test_header"))
    old_groups = app.group.get_group_list()
    group = Group(name = "New group")
    app.group.modify_first_group(group)
    group.id = old_groups[0].id
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max) # сравним отсортированные списки групп

# def test_modify_group_header(app):
#     old_groups = app.group.get_group_list()
#     app.group.modify_first_group(Group(header = "New header"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)